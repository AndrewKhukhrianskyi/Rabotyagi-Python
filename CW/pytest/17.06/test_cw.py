from selenium import webdriver # ЭТО ВАЖНО!
from selenium.webdriver.common.by import By # By - поиск элементов на сайте ПО ОПЦИИ
from selenium.webdriver.common.keys import Keys # Keys - работа с клавишами

import time
import pytest

@pytest.fixture
def open_browser():
    browser = webdriver.Chrome() # Подключаемся к браузеру Chrome()
    browser.get('https://google.com/') # .get(ссылка) - открывает сайт
    yield browser
    browser.close()

# send_keys вписывает данные в поле
# Keys.RETURN = Enter на клаве
def test_send_data(open_browser):
    browser = open_browser
    search_field = browser.find_element(By.XPATH, "//div/textarea[@class='gLFyf']")
    before_url = browser.current_url
    assert search_field.is_displayed()
    values_list = ['cats', 'dogs', 'memes',
                   'anime', 'music', 'Da Vinci',
                   'Volvo', 'Japan']
    for value in values_list:
        search_field = browser.find_element(By.XPATH, "//div/textarea[@class='gLFyf']")
        search_field.send_keys(value, Keys.RETURN)
        after_url = browser.current_url
        assert before_url != after_url
        time.sleep(2)
        clear_button = browser.find_element(By.XPATH,"//div[@aria-label='Очистить']/span")
        assert clear_button.is_displayed()
        clear_button.click()
        
'''
1. Вспомнить об XPATH. Ссылка: https://highload.today/xpath-xml/
2. Написать тест, который будет находить на сайте Rozetka товар и добавлять его в корзину
3. Почитать о конструкции Keys в Python
'''




