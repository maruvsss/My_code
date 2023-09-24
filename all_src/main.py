import asyncio
import os
import sqlite3
import datetime
from telebot.async_telebot import AsyncTeleBot
from telebot import types
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
bot = AsyncTeleBot(os.getenv('TOKEN_BOT'))
admin_id = [198542281,1900666417]

db = sqlite3.connect('db/database.db',check_same_thread=False)
sql = db.cursor()


sql.execute("""CREATE TABLE IF NOT EXISTS database(
    id integer PRIMARY KEY AUTOINCREMENT,
    tg_id integer,
    username text,
    date date
)""")

@bot.message_handler(commands=['users'])
async def all_users(message):
    if message.chat.id == admin_id[0] or message.chat.id == admin_id[1]:
        sql.execute("SELECT tg_id FROM database;")
        users = sql.fetchall()
        await bot.send_message(message.chat.id, f'👻 Общее количество пользователей: <b>{len(users)}</b>',
                               parse_mode='html')
    else:
        await bot.send_message(message.chat.id, f'🚫 Вы не является администратором')


@bot.message_handler(commands=['sendall'])
async def send_all_message(message: types.Message):
    sql.execute("SELECT tg_id FROM database;")
    users = sql.fetchall()
    if message.chat.id == admin_id[0] or message.chat.id == admin_id[1]:
        await bot.send_message(message.chat.id, '💌 Starting')
        for i in users:
            try:
                print("Send to: ", str(i[0]))
                await bot.send_message(i[0], message.text[message.text.find(' '):], parse_mode='html')
            except Exception as error:
                print("Blocked bot: ", str(i[0]))
            # await bot.send_message(i[0],message.text[message.text.find(' '):],parse_mode='html')
        await bot.send_message(message.chat.id, '✅ Successfully')
    else:
        await bot.send_message(message.chat.id, 'Вы не являетесь администратором!')

@bot.message_handler(commands=['download_db'])
async def command_download_db(message):
    if message.chat.id == admin_id[0] or message.chat.id == admin_id[1]:
        db = open('db/database.db', 'rb')
        await bot.send_document(message.chat.id, db)
    else:
        await bot.send_message(message.chat.id, 'Вы не являетесь администратором!')


async def send_delayed_message(chat_id):
    markup = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton(text='Читать статью', callback_data='call_btn1',
                                          url="https://dzen.ru/b/ZQY7ZqIUpDMdW9MA")
    button_2 = types.InlineKeyboardButton(text='Записаться', callback_data='call_kurs',
                                          url='https://taplink.cc/anastasia_expert/p/d17745/')
    markup.add(button_1,button_2)
    await asyncio.sleep(240)  # (4 Минуты - 240) +
    await bot.send_message(chat_id,
                           'Это очень жирная плюшка!\n\nЯ только за эту информацию уже могу с вас деньги брать, но не буду! Угощайтесь\n\nОткрывай статью и приятного аппетита',
                           reply_markup=markup)

    await asyncio.sleep(3600)  # (1 час - 3600)
    photo = open('media/sleep.jpg', 'rb')
    await bot.send_photo(chat_id, photo,
                         caption='Спишь?\n\nТы опять решила все пропустить, слиться, сдаться и пусть все идет туда откуда не возвращаются?\n\nОткрывай видео и смотри до конца, там не долго',
                         reply_markup=markup)

    await asyncio.sleep(3600)  # (1 час - 3600)
    await bot.send_message(chat_id, 'https://youtu.be/zEFky0ro0dU')

    await asyncio.sleep(3600)  # (1 час)
    markup2 = types.InlineKeyboardMarkup()
    button_2 = types.InlineKeyboardButton(text='Смотреть видео', callback_data='call_btn2',
                                          url="https://youtu.be/A1aE0Z04D44")
    markup2.add(button_2)
    await bot.send_message(chat_id,
                           "Надеюсь ты уже поняла, что со мной тусоваться очень выгодно\n\nЯ не жадничаю и выдаю бесплатно то, за что другим бы вы заплатили много тыщ… \n\nВообще все, что вы знали про инстаграм и продвижение - забудьте! \n\nСамый лучший способ проходить подобные интенсивы - убрать весь предыдущий опыт, и учиться как нулевой ученик\n\nРаскройте руки шире и забирайте следующее видео с широкой улыбкой\n\nСмотреть не долго",
                           reply_markup=markup2)
    await asyncio.sleep(240)  # (4 Минуты - 240) +
    markup_bank = types.InlineKeyboardMarkup()
    button_bank = types.InlineKeyboardButton(text='БАНК ИДЕЙ', callback_data='call_btn3',
                                             url="https://t.me/+2X_hST4KtLQ3NzY6")
    markup_bank.add(button_bank)
    photo = open('media/bank.jpg', 'rb')
    await bot.send_photo(chat_id, photo, reply_markup=markup_bank)

    await asyncio.sleep(3600)  # (1 час - 3600)
    photo = open('media/sleep.jpg', 'rb')
    await bot.send_photo(chat_id, photo,
                         caption='Спишь?\n\nТы опять решила все пропустить, слиться, сдаться и пусть все идет туда откуда не возвращаются?\n\nОткрывай видео и смотри до конца, там не долго',
                         reply_markup=markup)
    await asyncio.sleep(3600)  # (1 час - 3600)
    await bot.send_message(chat_id, 'https://youtu.be/A1aE0Z04D44')

    await asyncio.sleep(3600)  # (1 час - 3600)
    markup3 = types.InlineKeyboardMarkup()
    button_3 = types.InlineKeyboardButton(text='Смотреть видео', callback_data='call_btn4',
                                          url="https://youtu.be/SbHVbq06qdk")
    markup3.add(button_3)
    await bot.send_message(chat_id,
                           'Это заключительное! Больше не будет\n\nПотому что слишком много инструментов выдавать без системы - это как обезьяна с гранатой, если ты сама себе ее напоминаешь, когда пытаешься работать онлайн, то ты наверное уже проходишь InstaBeautyUp\n\nЗабирай последнее видео и посмотри его за обедом, это просто мне так захотелось, нет двойного смысла - я поделилась полезным контентом - уважь мое желание\n\nЕшь и смотри !',
                           reply_markup=markup3)

    await asyncio.sleep(240)  # (1 час - 3600)
    markup_finish = types.InlineKeyboardMarkup()
    button_finish = types.InlineKeyboardButton(text='Читать статью', callback_data='call_btn1',
                                               url="https://dzen.ru/b/ZQjZgqi7VjOJjH_W")
    markup_finish.add(button_finish)
    await bot.send_message(chat_id,
                           'Это последняя статья, которая поможет делать тебе исходники так, чтобы не шла кровь из глаз, когда смотришь все это\n\nКлассный инструмент и список оборудования для сьемок - используй его в общей системе о которой я рассказываю на практикуме\n\nСсылка на запись в описании этого канала',
                           reply_markup=markup_finish)

    await asyncio.sleep(3600)  # (1 час - 3600)
    photo = open('media/sleep.jpg', 'rb')
    await bot.send_photo(chat_id, photo,
                         caption='Спишь?\n\nТы опять решила все пропустить, слиться, сдаться и пусть все идет туда откуда не возвращаются?\n\nОткрывай видео и смотри до конца, там не долго',
                         reply_markup=markup)
    await asyncio.sleep(3600)  # (1 час - 3600)
    await bot.send_message(chat_id, 'https://youtu.be/SbHVbq06qdk')


@bot.message_handler(commands=['start'])
async def command_start(message):
    date = datetime.datetime.now()
    tg_id = message.from_user.id
    sql.execute(f"SELECT tg_id FROM database WHERE tg_id={tg_id}")
    data = sql.fetchone()
    username = message.from_user.username



    if data is None:

        if username != None:
            sql.execute("INSERT INTO database VALUES (?,?,?,?)", (None, tg_id,username, date))
            db.commit()
        else:
            username_none = 'None username'
            sql.execute("INSERT INTO database VALUES (?,?,?,?)", (None, tg_id, username_none, date))
            db.commit()

    markup = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton(text='Смотреть видео', callback_data='call_btn1',
                                          url='https://youtu.be/zEFky0ro0dU')
    markup.add(button_1)
    video = open('media/video.mp4', 'rb')
    await bot.send_video_note(message.chat.id, video)
    await bot.send_message(message.chat.id,
                           'Вэлком ту пати!\n\nТы попала на мини интенсив, пройдя который, тебе уже завтра станет легче жить, чем ты жила сегодня\n\nЭтот темный лес Инстаграм тебе станет немного понятнее, а многочасовые потуги с видео и фото своих работ - легче!\n\nОчень четко, системно и с прикладными инструментами, я расскажу, как можно было жить лучше, если бы ты со мной познакомилась раньше\n\nПредставляться я не буду, сами все увидите. Я сама не люблю вот эти нудные курсы, где воды больше, чем воды в воде… поэтому перейдем сразу к делу!\n\nПервая твоя задача - посмотреть видео, ссылка тут ⬇️ нажми и наслаждайся',
                           reply_markup=markup)
    await send_delayed_message(message.chat.id)  # Передаем идентификатор чата для отправки сообщения


asyncio.run(bot.polling(non_stop=True))
