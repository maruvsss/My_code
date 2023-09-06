import requests

# URL страницы
url = "https://douyin.wtf/"

# Данные, которые нужно отправить
data = {
    "url": "https://vm.tiktok.com/ZMj8HCaM1/"  # Ваша ссылка TikTok
}

# Отправляем POST запрос
response = requests.get(url, data=data)

with open("ttsavee.html", "wb") as file:
    file.write(response.content)
# Выводим содержимое ответа
print(response.text)
