import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(1)

# Метод get сообщает бра
# узеру, что нужно открыть сайт по указанной ссылке
driver.get("https://vk.com/")
time.sleep(1)

# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Ищем поле для ввода текста
#textarea = driver.find_element_by_css_selector("input.index_email.big_text")
a = driver.find_element_by_id("index_email")
# Напишем текст ответа в найденное поле
#textarea.send_keys("get()")
a.send_keys("get()")
time.sleep(5)

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element_by_css_selector(".submit-submission")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(5)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()
