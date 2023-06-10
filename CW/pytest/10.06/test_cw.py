from selenium import webdriver # ЭТО ВАЖНО!
from selenium.webdriver.common.by import By # By - поиск элементов на сайте ПО ОПЦИИ

browser = webdriver.Chrome() # Подключаемся к браузеру Chrome()
browser.get('https://theuselessweb.com/') # .get(ссылка) - открывает сайт
#assert 'The Useless Web' in browser.title
# By
# find_element выполняет поиск элемента на сайте
button = browser.find_element(By.XPATH, "//h5/button[@id='button']")
#is_displayed() проверяет находится ли элемент на странице
assert button.is_displayed()
button.click() # click() - клик на кнопку
browser.close() # close() - закрывает сайт

"""
1. Найти на сайте The Useless Web баннер внизу при помощи XPATH
2. Проверить, что баннер внизу отображается
3. (*) Установить селениум и chromedriver (Версия брауера должна совпадать
с версией драйвера
4. Тыкнуть на баннер через команду click()
"""
