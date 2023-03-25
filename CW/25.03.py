# Arrays (Lists) - Списки. Выражение позволяет хранить БОЛЬШЕ элементов и работать с ними
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print(list_numbers)

for number in list_numbers: # перебираем список по числам
    print(number)

# Списки можно склеивать друг с другом и формировать новый список
print([1, 2, 3] + ['a', 'b', 'c'])

# У многих динамических выражений можно работать с ИНДЕКСАМИ
print(list_numbers[2])

word = 'dog'

# Слова (или строки) - это совокупность сложенных между собой символов
# dog = d + o + g
print(list(word)) # Разбивает по 1 символу

# Task 1 - Достать четные числа
old_list = [1,4,5,6,7,9,10,11,26,10,25]
new_list = []

for number in old_list:
    if number % 2 == 0:
        # команды формируются так: список.команда(опционально - выражение)
        new_list.append(number)
print(new_list)


# Loop (Цикл)
summa = 0

for number in new_list:
    summa += number
print(summa)

# sum
print(f'Result: {sum(new_list)}')

# Можем вырезать выражения из списка по индексам
print(new_list[::-1]) # прочитаем список с конца

# Кортеж - список, которые не изменяется
tup = (1, 2, 3)
# Если через запятую записать несколько параметров без скобок -> не явно создадим кортеж
tup2 = 4, 5, 6
print(tup)
print(tup2)
print(tup + tup2)
print(tup)
print(tup2)
# tup[0] = 3
# Как изменить кортеж?
# Способ 1 - через list
tup = list(tup)
print(tup)
# Способ 2 - через создание нового списка
copy_list = []
for elem in tup2:
    copy_list.append(elem)
print(copy_list)

# Task - Trianlge perimeters
triangles = [[5, 10, 15], [5, 12, 13], [10, 25, 40]]
perimeter_list = []

for triangle in triangles:
    perimeter_list.append(sum(triangle))

print(perimeter_list)

# Task - Chaotic numbers

arr = [[1, 5, 6, 1, 0, 5], [25, 3, 1, 1, 11, 10, 1], [25, 3, 1, 1, 0]]

# Part 1 - Count
new_value = 0

for elem in arr:
    new_value += elem.count(1)
print(new_value)

# Part 2 - Count

new_value2 = 0

for sub_arr in arr:
    for value in sub_arr:
        if value == 1:
            new_value2 += 1
            
print(new_value2)

# Генератор списков (List comprehension)
# Syntax sugar - это способы писать код быстрее

from random import randint
# [действие for выражение in динамический_объект]
random_numbers = [randint(1, 10) for elem in range(100)]
print(random_numbers)

# Задача - палиндром
random_text = ['казак', 'abba', 'dsdssadasd', 'text', 'мадам', 'Мадам'] # .lower()

for text in random_text:
    text = text.lower()
    # path 1 - [::-1]
    if text == text[::-1]:
        print(f'{text} - палиндром!')
    else:
        print(f'{text} - NO палиндром!')
'''
HW
1. Почитать о списках: https://www.w3schools.com/python/python_lists.asp
2. Task: https://www.codewars.com/kata/5838a66eaed8c259df000003
3. Task: https://www.codewars.com/kata/57eae20f5500ad98e50002c5/train/python
'''
