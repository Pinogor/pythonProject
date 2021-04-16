from selenium import webdriver
import time
import unittest
link = "http://suninjuly.github.io/registration1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_xpath("//div[1]/div[1]/input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//div[1]/div[2]/input')
    input2.send_keys('Ivanov')
    input3 = browser.find_element_by_xpath('//div[1]/div[3]/input')
    input3.send_keys("ghjgjvh@gml.ru")
    button = browser.find_element_by_xpath('//div/form/button')
    button.click()

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(6)
    browser.quit()

