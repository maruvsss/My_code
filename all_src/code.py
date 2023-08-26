import re
import sqlite3
import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
import requests
import aiohttp
import os

TOKEN_BOT = '6697800196:AAHCmTjokC_iE97W9grQYY3KAajgIHNs4rA'

bot = Bot(token=TOKEN_BOT)
dp = Dispatcher(bot)
logging_middleware = LoggingMiddleware()
dp.middleware.setup(logging_middleware)


admin_id = 1900666417


def download(url):
    request_url = f'https://api.douyin.wtf/api?url={url}'
    response = requests.get(request_url)
    if response.status_code == 200:
        data = response.json()
        video_url = data["video_data"]["wm_video_url_HQ"]
        return video_url
    else:
        return None

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):

    await message.reply(
        '<b>Привет! Добро пожаловать к нам в видеобот TikTok! 🎉</b>\n\nМы рады видеть тебя здесь. Просто дайте мне ссылку на видео с TikTok, и я отправлю вам это видео без водяных знаков отправителя. Наслаждайтесь просмотром! Если у тебя есть какие-либо вопросы или запросы, не стесняйся спрашивать. 😊📹',
        parse_mode='html'
    )

@dp.message_handler()
async def process(message: types.Message):
    if re.compile('https://[a-zA-Z]+.tiktok.com/').match(message.text):
        loading = await message.reply('🕗 Ожидайте видео скачивается...')
        video_url = download(message.text)

        if video_url:
            video_filename = await save_video_locally(video_url)

            if video_filename:
                with open(video_filename, 'rb') as video_file:
                    await bot.send_video(message.chat.id, video_file, caption='🎉 Поздравляю, видео успешно скачено!')
                os.remove(video_filename)
            else:
                await message.reply('❌ Произошла ошибка при сохранении видео.')
        else:
            await message.reply('❌ Произошла ошибка при скачивании видео.')

        await bot.delete_message(message.chat.id, loading.message_id)
    else:
        await message.reply(
            '⛔️ В данный момент возможность загрузки видео доступна только из <b>TikTok</b>',
            parse_mode='html'
        )

async def save_video_locally(video_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(video_url) as response:
            if response.status == 200:
                video_filename = 'downloaded_video.mp4'

                with open(video_filename, 'wb') as file:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        file.write(chunk)

                return video_filename
            else:
                return None

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
