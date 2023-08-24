from aiogram import Bot, Dispatcher, executor, types
import aiohttp
import re

token = "6697800196:AAHCmTjokC_iE97W9grQYY3KAajgIHNs4rA"

bot = Bot(token=token)
dp = Dispatcher(bot)

async def download(url):
    async with aiohttp.ClientSession() as session:
        request_url = f'https://api.douyin.wtf/api?url={url}'
        async with session.get(request_url) as response:
            data = await response.json()
            video = data['video_data']['nwm_video_url_HQ']
            return video

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('<b>Привет! Добро пожаловать к нам в видеобот TikTok! 🎉</b>\n\nМы рады видеть тебя здесь. Просто дайте мне ссылку на видео с TikTok, и я отправлю вам это видео без водяных знаков отправителя. Наслаждайтесь просмотром! Если у тебя есть какие-либо вопросы или запросы, не стесняйся спрашивать. 😊📹',parse_mode="html")

@dp.message_handler()
async def process(message: types.Message):
    if re.compile('https://[a-zA-Z]+.tiktok.com/').match(message.text):
        m = await message.reply('🕗 Ожидайте видео скачивается...')
        video = await download(message.text)
        await bot.delete_message(message.chat.id, m['message_id'])
        await message.answer_video(video, caption=f'🎉 <b>Готово!</b>',parse_mode='html')
    else:
        await message.reply('⛔️ В данный момент возможность загрузки видео доступна только из <b>TikTok</b>',parse_mode='html')

if __name__ == "__main__":
    executor.start_polling(dp)
