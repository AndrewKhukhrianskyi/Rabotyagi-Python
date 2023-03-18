#number = int(input('Введите число: '))

#if number >= 0: if - ЕСЛИ
#    print('+')
#else: else - ВО ВСЕХ ОСТАЛЬНЫХ СЛУЧАЯХ
#    print('-')

# % - остача (остаток от деления)
#print(5 % 2)

#num  = int(input('Число: '))

#if num % 2 == 0:
#    print('Число четное!')
#else:
#    print('Число нечетное!')

"""
word = input('Введите слово: ')

if word == word[::-1]:
    print(True)
else:
    print(False)


number = int(input('Введите число: '))
if number > 0:
    print('+')
elif number == 0:
    print('0')
else: # else может быть не всегда
    print('-')


word = input('Text: ').lower()
vowels = 'aeouiy'
consonants = 'qwrtpsdfghjklzxcvbnm'
vowels_count = 0
consonants_count = 0
for letter in word:
    if letter in vowels: # in - есть ли что-то в чем-то
        vowels_count += 1
    elif letter in consonants:
        consonants_count += 1
    else:
        print('Символ не является буквой!', letter)

print('Кол-во гласных:', vowels_count)
print('Кол-во согласных:', consonants_count)


from random import randint

sheeps = []

sheep_count = 0

for sheep in range(randint(5, 100)):
    sheeps.append(bool(randint(0, 1)))

print(sheeps)
        
for sheep in sheeps:
    if int(sheep) == 1:
        sheep_count += 1
    else:
        print(False)



print(sheep_count)
        

print((True + True + True + True) // 2)


passwords = ['qwerty',
             '33112211',
             '123456',
             '1q2w3e4r',
             '123456789',
             '11111',
             '123456',
             'admin',
             '123123',
             '1234567890',
             'Мурзик',
             'Мурзик1970']

correct_password = "Мурзик1970"

for password in passwords:
    if password == correct_password:
        print("Добро пожаловать!")
    else:
        print("Пароль", password, "неверен!")

count = 0
while count < 10: # Для регулирования поведения создаем счетчик
    print(count)
    count += 1
"""

"""
Домашняя работа:
1. Почитать об условиях и цикле while в питоне
2. Написать программу, которая будет подсчитывать кол-во пробелов в тексте.
Решить через цикл for
3. Бегун. У бегуна есть 20 л воды. За 1 круг бегун выпивает 0.5 л воды
сколько кругов может пробежать бегун? Решить через цикл!
"""