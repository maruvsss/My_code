@bot.message_handler(commands=['add_proxy'])
async def add_proxy(message):
    User = Users_Model.getUser(chat_id=message.chat.id)
    if User[4] == 20:
        proxy_data = message.text.replace('/add_proxy ', '').split('\n')

        position_id = proxy_data[0].split(':')[1]

        del proxy_data[0]

        try:
            for proxy_item in proxy_data:
                ip, port, username, password = proxy_item.split(':')

                # await bot.send_message(message.chat.id, f"\n{ip}\n{port}\n{username}\n{password}")

                Proxies_Model.addProxy(proxy_host=ip + ':' + port, proxy_user=username, proxy_password=password,
                                       position_id=position_id)

            await bot.send_message(message.chat.id, '✅ Прокси успешно добавлены')
        except:
            await bot.send_message(message.chat.id, '📛 Прокси некорректны и не могут быть добавлены')
    else:
        await bot.send_message(message.chat.id, '⛔️ Вы не являетесь администратором!')