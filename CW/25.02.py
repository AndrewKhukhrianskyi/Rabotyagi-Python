arr = [1, 2, 3]
arr2 = [4, 5, 6]
print(arr + arr2) # Получаем новый список
print(arr)
print(arr2)

arr3 = arr + arr2
print(arr3)

# Обращение по индексу

arr4 = ['a', 'b', 'c', True, None,
        'doge', 'пудж', 'Где-то в Огайо']
print(arr4[3])

# len() - считает кол-во элементов списка
arr5 = [4, 5, 3, 2]
print(len(arr5))

# min(), max()
list_numbers = [1,6,78,4,3,7,6,4,
                32,2,5,7,8,3,3,4,86]
print('Min value:')
print(min(list_numbers))
print(max(list_numbers))

# .reverse() - переворачивает список
data = ['dog', 'cat', 'aboba']
print(data)
data.reverse()
print(data)
data = [6, 7, 3, 2, 4, 9]
data.sort()
print(data)
data = ['h', 'j', 'b', 'c', 'a']
data.sort()

print(data)
data = ['a', 2, True, None, 'n', 243]
#data.sort()
print(data)

# Tuples (Кортежи)
tup = 1, 2, 3 # Неявно сделает кортеж
tup = (1, 2, 3)
# tup[0] = 4 # Error
# Если нужно поменять, то нужно сделать список из кортежа
tup = list(tup)
print(tup)
tup[0] = 4
print(tup)
# Возвращаем список в кортеж
tup = tuple(tup) # делаем кортеж
print(tup)
print(tup[50])

'''
Homework
1. Почитать о списках и кортежах в питоне:
2. Написать программу, которая будет искать текст в списке с числами
Пример: [1,2,4,5,'dog', 8, 213, 44]
Результат работы: 'dog'
3. Попробуйте перевернуть список разными способами и посмотрите на результат (т.е посмотреть варианты КРОМЕ .reverse())
'''
