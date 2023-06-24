from selenium import webdriver # ЭТО ВАЖНО!
from selenium.webdriver.common.by import By # By - поиск элементов на сайте ПО ОПЦИИ
from selenium.webdriver.common.keys import Keys # Keys - работа с клавишами
from selenium.webdriver.common.action_chains import ActionChains # Цепь действий

import time
import pytest


@pytest.fixture
def open_browser():
    browser = webdriver.Chrome()
    browser.get('https://theuselessweb.com/')
    yield browser
    browser.close()

def test_chain_button(open_browser):
    browser = open_browser
    button = browser.find_element(By.XPATH,
                                  "//h5/button[@id='button']")
    action_button = ActionChains(browser)
    action_button.move_to_element(button)
    assert button.is_enabled()
    action_button.click()
    action_button.perform()
    time.sleep(3)
    action_button.key_down(Keys.ALT)
    action_button.key_down(Keys.TAB)
    action_button.key_up(Keys.ALT)
    action_button.key_up(Keys.TAB)
    action_button.perform()

# Task
# На сайте Rozetka вписать в поле поиска текст, с применением ActionChains
# Проверить, что текст в поле был написан с большой буквы
'''
1. Почитать об Action Chains
2. Почитать о методах
3. На сайте Rozetka вписать в поле поиска текст, с применением ActionChains
Проверить, что текст в поле был написан с большой буквы
'''
    


