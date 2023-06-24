from selenium import webdriver # ЭТО ВАЖНО!
from selenium.webdriver.common.by import By # By - поиск элементов на сайте ПО ОПЦИИ
from selenium.webdriver.common.keys import Keys # Keys - работа с клавишами

import pytest
import time

@pytest.fixture
def open_browser():
    browser = webdriver.Chrome() # Подключаемся к браузеру Chrome()
    browser.get('https://rozetka.com.ua/') # .get(ссылка) - открывает сайт
    yield browser
    browser.close()

def test_send_data(open_browser):
    browser = open_browser
    search_field = browser.find_element(By.XPATH, "//div/input[@name='search']")
    search_field.send_keys('Asus', Keys.RETURN)
    try:
        no_results = browser.find_element(By.XPATH, "//div/span")
        assert False
    except:
        assert True
    item = browser.find_element(By.XPATH,
                                "//div/div[@data-goods-id='380878761']")
    time.sleep(2)
    item.click()
    time.sleep(2)
    buy_button = browser.find_element(By.XPATH,
                                      "//app-buy-button[1]")
    buy_button.click()
    time.sleep(2)
    shopping_cart = browser.find_element(By.XPATH,
                                         "//rz-shopping-cart")
    assert shopping_cart.is_displayed()
        




