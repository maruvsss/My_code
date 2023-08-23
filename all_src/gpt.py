import os
import openai
import asyncio
from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot("6480636180:AAGsu2fusbzjRM1hBNH5UtGSVcWKNpc_Hoc")
openai.organization = "org-jYPBmx4I02yL8Pvxf0EU56I7"
openai.api_key = "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"


@bot.message_handler(commands=['start'])
async def start(message):
    print(message.from_user.id)
    await bot.send_message(message.chat.id,
                           '🎬 Привет! Я - твой помощник по поиску фильмов. Просто напиши мне краткое описание фильма, и я постараюсь найти его название для тебя. 😊\n\n🔍 Давай начнем! Просто отправь мне описание фильма, а я постараюсь найти его название.\n\nВот пример корректного запроса :\n<b>Пожалуйста, найди фильм, в котором главный герой путешествует во времени и пытается изменить прошлое, чтобы спасти свою семью</b>',
                           parse_mode='html')


@bot.message_handler()
async def message(message):
    user_message = message.text  # Получаем сообщение пользователя
    username = message.from_user.username
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Вы — помощник по поиску фильмов."},
                  {"role": "user", "content": user_message}],
        temperature=0.5,
        max_tokens=256
    )

    bot_response = response.choices[0]['message']['content']
    await bot.send_message(message.chat.id, bot_response)


asyncio.run(bot.polling(non_stop=True))
