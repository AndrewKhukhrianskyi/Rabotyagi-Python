def divide_on_2():# def создает функцию
    number = int(input('Enter a number: '))
    print('Result:',number // 2)

# Для того, чтобы вызвать логику ф-и, нужно
# обратиться к ней по имени

# Обращение к ф-и
# divide_on_2()

def find_perimeter():
    # Part simple (Pt1)
    side1 = int(input('Side 1: '))
    side2 = int(input('Side 2: '))
    side3 = int(input('Side 3: '))
    print('Perimeter:', side1+ side2 + side3)
    # Part Advanced (Pt2)
    perimeter = 0
    for side in range(3):
        perimeter += int(input('Enter a side: '))
    print('ADV perimeter:', perimeter)
#find_perimeter()
def find_distance(speed, time): # То, что передается в скобках = аргументы
    # аргументы - параметры, которые нужны для работы функции
    distance = speed * time
    print('Distance:', distance)

# Аргументов нужно передавать точное кол-во
#find_distance(20, 3)
#find_distance(80, 6)

# return - команда, которая дотает выражение из функции

def add_2(number):
    return number + 2
#result = add_2(5)

# Пример с к return
# Задача: Найти периметр прямоугольника при известной стороне и площади
def find_side(area, side):
    return area // side

def find_square_perimeter(side, side_2):
    return side + side_2 + side + side_2

area = 50
side = 25
side_2 = find_side(area, side)
print('Perimeter:',find_square_perimeter(side, side_2))

'''
HW

1. Почитать о стилях программирования: https://ru.wikipedia.org/wiki/Парадигма_программирования
2. О функциях: https://www.w3schools.com/python/python_functions.asp
3. Task: https://www.codewars.com/kata/56530b444e831334c0000020
'''
