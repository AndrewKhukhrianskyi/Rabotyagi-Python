# Dictionaries (Словари)
# Свойства

d = {1:'a', 2:'b'}

print(d[2]) # Обращение идет по ключу

# Обращение к несуществующему ключу приведет к KeyError
# print(d[3])

#добавление в словарь: словарь[новый ключ] = значение

d[3] = 'c'
print(d)
print(d.keys())
print(d.values())
print(d.pop(3))
print(d)

#словарь.команда(действие)

user_database = {'user1' : 'Allan', 'user2' : 'David',
                 'user3' : 'Clementine', 'user4' : 'Morgan',
                 'user5' : 'Kyle', 'user6' : 'Eugene',
                 'user7' : 'Leon', 'user8' : 'Alice'}
surname_database = {'user1' : 'Bekker', 'user2' : 'White',
                 'user3' : 'Rodriguez', 'user4' : 'Blake',
                 'user5' : 'Broslowski', 'user6' : 'Neumann',
                 'user7' : 'Kennedy', 'user8' : 'Black'}
# Задача: Достать имена всех пользователей и подсчитать тех
# людей, имя которых начинается на букву А
names = user_database.values()
count = 0
print(names)
for name in names:
    if name[0] == 'A':
        count += 1
        print(name)

    if name.startswith('A'):
        print(name)

# Задача - вывести нечетных пользователей по порядку
# Подсказка: обратите внимание на последний элемент user

for user, name in user_database.items():
    if int(user[-1]) % 2 == 1:
        print(user, name)
# Задача - вывести на экран имя и фамилию человека из 2х разных словарей
user_numbers = surname_database.keys()
for user_number in user_numbers:
    print(user_database[user_number],surname_database[user_number])
    print(user_number)

'''
HW:
1. О словарях: https://www.w3schools.com/python/python_ref_dictionary.asp
2. Task: https://www.codewars.com/kata/5533c2a50c4fea6832000101
3. Task2: https://www.codewars.com/kata/53da6a7e112bd15cbc000012
'''
