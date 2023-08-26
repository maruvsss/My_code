import re
import sqlite3
import asyncio
import os
import aiohttp
import datetime
import pyshorteners
import requests
from telebot.async_telebot import AsyncTeleBot
from telebot import types
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
bot = AsyncTeleBot(os.getenv('TOKEN_BOT'))

db = sqlite3.connect('db/ttsavee.db', check_same_thread=False)
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users(
    id integer PRIMARY KEY AUTOINCREMENT,
    tg_id integer,
    date date
)""")

admin_id = 1900666417


@bot.message_handler(commands=['sendall'])
async def send_all_message(message: types.Message):
    sql.execute("SELECT tg_id FROM users;")
    users = sql.fetchall()
    if message.chat.id == admin_id:
        await bot.send_message(message.chat.id, 'Starting')
        for i in users:
            try:
                print("Send to: ", str(i[0]))
                await bot.send_message(i[0], message.text[message.text.find(' '):])
            except Exception as error:
                print("Blocked bot: ", str(i[0]))
            # await bot.send_message(i[0],message.text[message.text.find(' '):],parse_mode='html')
    else:
        await bot.send_message(message.chat.id, 'Вы не являетесь администратором!')


async def download(url):
    async with aiohttp.ClientSession() as session:
        request_url = f'https://api.douyin.wtf/api?url={url}'
        async with session.get(request_url) as response:
            data = await response.json()
            video = data['video_data']['nwm_video_url_HQ']
            return video


@bot.message_handler(commands=['start'])
async def command_start(message):
    date = datetime.datetime.now()
    tg_id = message.from_user.id

    sql.execute(f"SELECT tg_id FROM users WHERE tg_id={tg_id}")
    data = sql.fetchone()
    if data is None:
        sql.execute("INSERT INTO users VALUES (?,?,?)", (None, tg_id, date))
        db.commit()

    await bot.send_message(message.chat.id,
                           '<b>Привет! Добро пожаловать к нам в видеобот TikTok! 🎉</b>\n\nМы рады видеть тебя здесь. Просто дайте мне ссылку на видео с TikTok, и я отправлю вам это видео без водяных знаков отправителя. Наслаждайтесь просмотром! Если у тебя есть какие-либо вопросы или запросы, не стесняйся спрашивать. 😊📹',
                           parse_mode='html')


@bot.message_handler()
async def process(message):
    try:
        if re.compile('https://[a-zA-Z]+.tiktok.com/').match(message.text):
            loading = await bot.send_message(message.chat.id, '🕗 Ожидайте видео скачивается...')
            video = await download(message.text)

            await bot.delete_message(message.chat.id, loading.message_id)
            await bot.send_video(message.chat.id, video, caption='🎉 Поздравляю, видео успешно скачено!')
        else:
            await bot.send_message(message.chat.id,
                                   '⛔️ В данный момент возможность загрузки видео доступна только из <b>TikTok</b>',
                                   parse_mode='html')
    except:
        loading = await bot.send_message(message.chat.id, '🕗 Видео немного большое ,ожидайте видео скачивается...')
        video = await download(message.text)
        response = requests.get(video)
        with open("ttsavee.mp4", "wb") as file:
            file.write(response.content)
        document = open("ttsavee.mp4", "wb")

        await bot.delete_message(message.chat.id, loading.message_id)
        await bot.send_document(message.chat.id, document, caption='🎉 Поздравляю, видео успешно скачено!')
        os.remove("ttsavee.mp4")


asyncio.run(bot.polling(non_stop=True))
