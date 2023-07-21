import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math

link_one = "https://stepik.org/lesson/236895/step/1"
list_of_links = ('https://stepik.org/lesson/236895/step/1',
                 'https://stepik.org/lesson/236896/step/1',
                 'https://stepik.org/lesson/236897/step/1',
                 'https://stepik.org/lesson/236898/step/1',
                 'https://stepik.org/lesson/236899/step/1',
                 'https://stepik.org/lesson/236903/step/1',
                 'https://stepik.org/lesson/236904/step/1',
                 'https://stepik.org/lesson/236905/step/1)',
                 )
failed_tests = []

@pytest.mark.parametrize('link', list_of_links)
def test_autorization(browser, link):
    browser.implicitly_wait(10)
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '.navbar__auth_login').click()
    browser.find_element(By.CSS_SELECTOR, "[name='login']").send_keys('login')
    browser.find_element(By.CSS_SELECTOR, "[name='password']").send_keys('password')
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login_form [type='submit']"))).click()
    #browser.find_element(By.CSS_SELECTOR, "#login_form [type='submit']").click()
    #browser.find_element(By.CSS_SELECTOR, "[alt='User_avatar']")
    #WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[alt='User_avatar']")))
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Profile']")))
    #text_area = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'textarea')))
    text_area = browser.find_element(By.TAG_NAME, 'textarea')
    number = math.log(int(time.time()))
    #text_area.clear()
    #time.sleep(5)
    text_area.send_keys(number)
    flag = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.TAG_NAME, 'textarea'), number))
    #time.sleep(5)
    if flag.text == number:
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.attempt__actions [class*="submit"]'))).click()
    result = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.attempt__message p'))).text()
    #result = browser.find_element(By.CSS_SELECTOR, '.attempt__message p').text
    assert 'Correct!' in result, result

if __name__ == '__main__':
    pytest.main()