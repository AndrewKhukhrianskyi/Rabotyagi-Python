# Task 1 - Словарь из двух списков
def create_dict(arr1, arr2):
    result = {}

    for elem in range(len(arr1)):
        try:
            result[arr1[elem]] = arr2[elem]
        except IndexError:
            result[arr1[elem]] = None
    return result

# print(create_dict([1,2,3,4,5], [4,5,6,7]))

# Task 2 - Сортировка словарей
def sort_dict(dictionary):
    result = []
    for par in dictionary:
        result.append((par, dictionary[par]))
    for first in range(len(result)):
        for second in range(first + 1, len(result)):
              if result[first][1] < result[second][1]:
                result[second], result[first] = result[first], result[second]             
    return result

print(sort_dict({1:2, 2:4, 3:6}))