'''
text = input("Введите текст: ")
text = text.title().replace(' ', '')
print('#' + text)

if 5 < 4:
    print('5 > 4')
else:
    print('NO!')

number = int(input('Number 1: '))
number_2 = int(input('Number 2: '))

if number + number_2 > 5:
    print('Kruta')
else:
    print('NIE KRUTA!')
    

number_3 = int(input('number 3: '))

if number_3 > 0:
    print('+')
elif number_3 == 0:
    print('0')
else:
    print('-')
'''

nickname = input('Nickname: ')
pwd = input('Password: ')
correct_pwd = 'admin'

if pwd == correct_pwd:
    print('Welcome', nickname)
else:
    print('ALERT! Incorrect password!')


'''
1. Почитать об условиях: https://dvmn.org/encyclopedia/python_basic_level/conditionals/#:~:text=%D0%A3%D1%81%D0%BB%D0%BE%D0%B2%D0%B8%D1%8F%20%D0%B2%20Python%201%20if%20%D0%97%D0%B0%D0%B3%D0%B0%D0%B4%D0%B0%D0%B9%D1%82%D0%B5%20%D0%BA%D0%B0%D0%BA%D0%BE%D0%B5-%D0%BD%D0%B8%D0%B1%D1%83%D0%B4%D1%8C%20%D0%B6%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D0%BE%D0%B5.,%2C%20%D0%BD%D0%B0%D0%B7%D1%8B%D0%B2%D0%B0%D1%8E%D1%82%20%D0%BF%D1%80%D0%B5%D0%B4%D0%B8%D0%BA%D0%B0%D1%82%D0%BE%D0%BC.%20...%206%20%D0%90%D0%BB%D1%8C%D1%82%D0%B5%D1%80%D0%BD%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D1%8B%D0%B5%20%D0%B8%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8%20
2. Четность числа. Напишите программу, которая определяет четность числа. 
   Если число четное - печатать True иначе False (Подсказка: Погуглите знак % в питоне и что он делает.)
3. С большой или с маленькой? Написать программу, которая определеяет, с каких букв написан текст
    - Если с больших - Печатать True
    - Если с малых - Печатать False
4. Модифицируйте задачу 3, прикрутив условие того, что нужно сделать проверку на числа\буквы (можно сделать отдельным условием)

'''