import pytest

from random import randint

# Фикстура - действие перед тестом
@pytest.fixture
def generate_numbers():
    number_1 = randint(1, 10)
    number_2 = randint(1, 10)
    return number_1 + number_2

# Применение фикстуры записывается как аргумент теста
def test_sum(generate_numbers):
    result = generate_numbers
    assert result > 0

# Task
'''
Написать фикстуру, которая создает случайное
число от -100 до 100
Написать тест, который будет проверять, что
если число отрицательное и нечетное -> True
На все остальное - False
'''
@pytest.fixture
def generate_negative():
    number = randint(-100, 100)
    return number

@pytest.mark.example
def test_example(generate_negative):
    number = generate_negative
    if number % 2 != 0 and number < 0:
        assert True
    else:
        assert False

# Task 
'''
Написать фикстуру которая будет создавать число палиндром
Написать тест, который будет проверять, а палиндром ли
мы получили.
'''

@pytest.fixture
def generate_palindrome():
    palindrome = randint(10, 11)
    return str(palindrome)

def test_palindrome(generate_palindrome):
    palindrome = generate_palindrome
    if palindrome == palindrome[::-1]:
        assert True
    else:
        assert False
# yield in fixture
# yield - умный return, который может поставить функцию "на паузу"
# yield может также НИЧЕГО не возвращать
'''
В контексте фикстур позволяет поставить логику на паузу
и исполнить ПОСЛЕ теста
'''

@pytest.fixture
def assert_fuckup():
    number = 1
    yield number # return
    assert False

@pytest.mark.fuckup
def test_fuckup(assert_fuckup):
    number = assert_fuckup
    assert number

# skip - пропускает тест
# skipif - пропускает тест при определенных условиях
@pytest.mark.skip
def test_smth():
    assert True

import sys
@pytest.mark.skipif(sys.version_info < (3, 10),
                    reason = 'Not working with Python 3.10 and upper')
def test_smth2():
    assert True

# parametrize - перезапуск теста
@pytest.mark.square
@pytest.mark.parametrize('side, expected_result', [(4, 16),
                                                   (5, 20),
                                                   (7, 28),
                                                   (9, 32)])
def test_square(side, expected_result):
    assert side * 4 == expected_result

# pi * радиус ** 2
@pytest.mark.parametrize('radius, expected_result', [(4, 50.24)])
@pytest.mark.radius
def test_radius(radius, expected_result):
    result = 3.14 * (radius ** 2)
    assert result == expected_result
