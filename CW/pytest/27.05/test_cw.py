import pytest

from random import randint

def test_func():
    assert 2 + 2 == 4

# flaky - плавающий
# flaky bug - баг, который срабатывает не всегда

def test_func2():
    def generate_numbers():
        num_1 = randint(-10, 10)
        num_2 = randint(-10, 10)
        return num_1, num_2
    
    result = generate_numbers()
    assert sum(result) > 0
# Для вызова конкретного теста, нужно
# Способ 1
# ::
# Способ 2
# markers

# Прописать команду pytest название файла::название функции
def test_func3():
    assert True

def test_check_even():
    def is_even():
        number = 7
        result = 'x'
        if number % 2 == 0:
            result = True
        else:
            result = False
        return result
    assert is_even() 
    
# метки - pytest.mark
# метки:
# служебные - те что встроены в pytest
# пользовательские - те, что мы придумали
"""
Команда вызова теста с меткой:
pytest название файла -m метка
"""

# @pytest.mark.метка

@pytest.mark.rabotyaga
def test_a():
    assert True
    
@pytest.mark.rabotyaga
def test_b():
    assert True

def test_c():
    assert False
'''
HW 27.05
1. Почитать о pytest:
https://youtu.be/1HtEPEn4-LY
2. Почитать о техниках тест-дизайна
https://highload.today/blogs/8-tehnik-test-dizajna-s-primerami/
3. Предположим, есть сайт с ограничением по возрасту.
Напишите технику-тест дизайна на проверку возраста, если человек меньше 18 лет - не пускать,
иначе - пускать!
4. Написать тест, который будет проверять, является ли выражение палиндромом
True, если является, False, если нет
5(*). У вас есть интернет магазин одежды, и есть система ручного пошива одежды
человек, может выбрать, что и из какого материала и размера будет одежда
У вас есть 3 опции: одежда (футболка, свитер и тп.), размер(S,M,L..), материал(коттон, шерсть...)
При помощи техники Pairwise рассчитайте кол-во тестов.
'''
