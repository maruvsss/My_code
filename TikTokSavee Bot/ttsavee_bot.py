import re
import sqlite3
import asyncio
import os
import aiohttp
from telebot.async_telebot import AsyncTeleBot
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
bot = AsyncTeleBot(os.getenv('TOKEN_BOT'))


async def download(url):
    async with aiohttp.ClientSession() as session:
        request_url = f'https://api.douyin.wtf/api?url={url}'
        async with session.get(request_url) as response:
            data = await response.json()
            video = data['video_data']['nwm_video_url_HQ']
            return video


@bot.message_handler(commands=['start'])
async def command_start(message):
    await bot.send_message(message.chat.id,
                           '<b>Привет! Добро пожаловать к нам в видеобот TikTok! 🎉</b>\n\nМы рады видеть тебя здесь. Просто дайте мне ссылку на видео с TikTok, и я отправлю вам это видео без водяных знаков отправителя. Наслаждайтесь просмотром! Если у тебя есть какие-либо вопросы или запросы, не стесняйся спрашивать. 😊📹',
                           parse_mode='html')


@bot.message_handler()
async def process(message):
    if re.compile('https://[a-zA-Z]+.tiktok.com/').match(message.text):
        loading = await bot.send_message(message.chat.id, '🕗 Ожидайте видео скачивается...')
        video = await download(message.text)
        await bot.delete_message(message.chat.id, loading.message_id)
        await bot.send_video(message.chat.id, video,caption='🎉 Поздравляю, видео успешно скачено!')
    else:
        await bot.send_message(message.chat.id,
                               '⛔️ В данный момент возможность загрузки видео доступна только из <b>TikTok</b>',
                               parse_mode='html')


asyncio.run(bot.polling(non_stop=True))
