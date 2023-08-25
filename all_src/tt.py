import re
import sqlite3
import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
import aiohttp

TOKEN_BOT = '6697800196:AAHCmTjokC_iE97W9grQYY3KAajgIHNs4rA'

bot = Bot(token=TOKEN_BOT)
dp = Dispatcher(bot)
logging_middleware = LoggingMiddleware()
dp.middleware.setup(logging_middleware)

# db = sqlite3.connect('db/ttsavee.db', check_same_thread=False)
# sql = db.cursor()
#
# sql.execute("""CREATE TABLE IF NOT EXISTS users(
#     id integer PRIMARY KEY AUTOINCREMENT,
#     tg_id integer,
#     date date
# )""")

admin_id = 1900666417

# @dp.message_handler(commands=['sendall'])
# async def send_all_message(message: types.Message):
#     sql.execute("SELECT tg_id FROM users;")
#     users = sql.fetchall()
#     if message.chat.id == admin_id:
#         await message.reply('Starting')
#         for i in users:
#             try:
#                 print("Send to: ", str(i[0]))
#                 await bot.send_message(i[0], message.text[message.text.find(' '):])
#             except Exception as error:
#                 print("Blocked bot: ", str(i[0]))
#     else:
#         await message.reply('Вы не являетесь администратором!')


async def download(url):
    async with aiohttp.ClientSession() as session:
        request_url = f'https://api.douyin.wtf/api?url={url}'
        async with session.get(request_url) as response:
            data = await response.json()
            video = data['video_data']['nwm_video_url_HQ']
            return video


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    # date = datetime.datetime.now()
    # tg_id = message.from_user.id
    #
    # sql.execute(f"SELECT tg_id FROM users WHERE tg_id={tg_id}")
    # data = sql.fetchone()
    # if data is None:
    #     sql.execute("INSERT INTO users VALUES (?,?,?)", (None, tg_id, date))
    #     db.commit()

    await message.reply(
        '<b>xxxxПривет! Добро пожаловать к нам в видеобот TikTok! 🎉</b>\n\nМы рады видеть тебя здесь. Просто дайте мне ссылку на видео с TikTok, и я отправлю вам это видео без водяных знаков отправителя. Наслаждайтесь просмотром! Если у тебя есть какие-либо вопросы или запросы, не стесняйся спрашивать. 😊📹',
        parse_mode='html'
    )


@dp.message_handler()
async def process(message: types.Message):
    if re.compile('https://[a-zA-Z]+.tiktok.com/').match(message.text):
        loading = await message.reply('🕗 Ожидайте видео скачивается...')
        video = await download(message.text)
        await bot.delete_message(message.chat.id, loading.message_id)
        await message.reply_video(video, caption='🎉 Поздравляю, видео успешно скачено!')
    else:
        await message.reply(
            '⛔️ В данный момент возможность загрузки видео доступна только из <b>TikTok</b>',
            parse_mode='html'
        )


if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)