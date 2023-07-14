from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    link_bag = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    value = WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element(By.CSS_SELECTOR, 'button#book').click()

    value = browser.find_element(By.CSS_SELECTOR, '#input_value')
    browser.find_element(By.CSS_SELECTOR, 'input').send_keys(calc(int(value.text)))
    browser.find_element(By.CSS_SELECTOR, 'button#solve').click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()