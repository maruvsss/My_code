import os
import openai
import asyncio
from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot("6656005110:AAGMMMh1dCFYZcbpJE0mwZfYtZnaLMuM0b0")
openai.organization = "org-jYPBmx4I02yL8Pvxf0EU56I7"
openai.api_key = "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"

@bot.message_handler()
async def message(message):
    user_message = message.text  # Get the user's message
    model_input = [{"role": "system", "content": "You are a helpful assistant."},
                   {"role": "user", "content": user_message}]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=model_input,
        temperature=0.5,
        max_tokens=256
    )

    bot_response = response['choices'][0]['message']['content']
    await bot.send_message(message.chat.id,bot_response)

asyncio.run(bot.polling(non_stop=True))