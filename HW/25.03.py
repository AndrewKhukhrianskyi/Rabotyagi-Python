# Task 1 - Палиндром 
from random import randint 

random_numbers = [randint(11, 22) for elem in range(10)]
result = []

for elem in random_numbers:
    if str(elem) == str(elem)[::-1]:
        result.append(1)
    else:
        result.append(0)
print(random_numbers)
print(result)

# Task 2 - No space

string = input('Введи слово с пробелами: ')
print(string.replace(' ', ''))

