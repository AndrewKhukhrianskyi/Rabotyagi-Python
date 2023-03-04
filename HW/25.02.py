# Task 1 - Find Word
arr = [1, 2, 5, 6, 7, 'dog', 3, 4]
print(arr[-3])

# Task 2 - Reverse Array

# Part 1 - .reverse()
arr2 = [1, 2, 3]
arr2.reverse()
print(arr2)

# Part 2 - [::-1]
arr2 = [1, 2, 4]
print(arr2[::-1])

# Part 3 - reversed() - Работает со строками и формирует новое выражение
arr3 = ['a', 'b', 'c']
print(''.join(reversed(arr3)))
