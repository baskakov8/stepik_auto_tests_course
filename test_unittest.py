from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestWebsite(unittest.TestCase):

    def test_first(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.case_for_tests(link)

    def test_second(self):
        link = 'http://suninjuly.github.io/registration2.html'
        self.case_for_tests(link)

    def case_for_tests(self, link):
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        element = browser.find_element(By.CSS_SELECTOR, "[placeholder*='first name']")
        element.send_keys("LOL")
        element = browser.find_element(By.CSS_SELECTOR, "[placeholder*='last name']")
        element.send_keys("LOL")
        element = browser.find_element(By.CSS_SELECTOR, "[placeholder*='email']")
        element.send_keys("LOL")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        correct_text = "Congratulations! You have successfully registered!"
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(correct_text, welcome_text, f'{welcome_text} should equal {correct_text}')

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    unittest.main()