from selenium import webdriver

import requests

driver = webdriver.Chrome()

driver.get("https://boymoney.cfd/ads.php")

# Получаем элемент с капчей

captcha_element = driver.find_element_by_css_selector('#captcha')

# Извлекаем URL изображения капчи

captcha_image_url = captcha_element.get_attribute('https://boymoney.cfd/images/captcha/?5079459')

# Отправляем запрос на решение капчи с помощью requests

api_key = 'your_api_key'

captcha_solution = requests.post('https://capha.guru/in.php', data={'key': api_key, 'method': 'base64', 'body': captcha_image_url}).text

# Вводим решение капчи в соответствующее поле

captcha_solution_element = driver.find_element_by_css_selector('#captcha-input"')

captcha_solution_element.send_keys(captcha_solution)

# Отправляем форму

submit_button = driver.find_element_by_css_selector('#card-btn')

submit_button.click()