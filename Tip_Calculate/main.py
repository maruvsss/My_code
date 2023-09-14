import asyncio
import os
import sqlite3
import calendar
import datetime
from telebot.async_telebot import AsyncTeleBot
from telebot import types
from dotenv import load_dotenv, find_dotenv
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
import locale
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

db = sqlite3.connect('db/tip_bot.db',check_same_thread=False)
sql=db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS tip(
    id integer PRIMARY KEY AUTOINCREMENT,
    tg_id integer,
    tip integer,
    date date
)""")

load_dotenv(find_dotenv())
bot = AsyncTeleBot(os.getenv('TOKEN_BOT'))


cal = calendar.month(2023, 9)
@bot.message_handler(commands=['start'])
async def start_command(message):
    tg_id= message.chat.id
    date = datetime.datetime.now()
    sql.execute(f"SELECT tg_id FROM tip WHERE tg_id={tg_id}")
    data = sql.fetchone()
    if data is None:
        sql.execute("INSERT INTO tip VALUES (?,?,?,?)", (None, tg_id,0, date))
        db.commit()
    await bot.send_message(message.chat.id,'Starting c:')
    calendar, step = DetailedTelegramCalendar().build()
    await bot.send_message(message.chat.id,f'Select {LSTEP[step]}',reply_markup = calendar)


@bot.message_handler(content_types=['text'])
async def text(message):
    await bot.send_message(message.chat.id,'Your tip is saved')

@bot.callback_query_handler(func=DetailedTelegramCalendar.func())

async def cal(c):
    balance = 0
    result, key, step = DetailedTelegramCalendar().process(c.data)

    if not result and key:

        await bot.edit_message_text(f'Select {LSTEP[step]}',c.message.chat.id,c.message.message_id,reply_markup=key)

    elif result:

        await bot.edit_message_text(f'В этот день {result} ваш чай :{balance} ',c.message.chat.id,c.message.message_id)
asyncio.run(bot.polling(non_stop=True))