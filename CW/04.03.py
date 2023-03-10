'''
word = 'hello'
# Way # 1 - Через индексы
#word = word[::-1]
# Way # 2 - reversed()
word = ''.join(reversed(word))
for letter in word: # создаем переменную letter внутри цикла
    print(letter) # буква из слова\

for number in range(1, 10, 4):
    # Way 1 - Умножение
    # print(number * number) # *
    # Way 2 - Возведение в степень
    print(number ** 2)
'''
#for elem in range(5, ...): # range(0,5)
#    print(elem)
from random import randint

sheeps = []   
sheep_count = 0
for sheep in range(1, randint(2, 100)):
    sheeps.append(bool(randint(0, 1)))

print(sheeps)

# Way # 1
for sheep in sheeps:
    if sheep is True:
        sheep_count = sheep_count + 1
print(sheep_count)

# Way # 2 - count

print(sheeps.count(True))

# Way # 3 - sort
sheeps.sort()
sheeps.reverse()
# break - завершить работу цикла
sheep_count_2 = 0
for sheep in sheeps:
    if sheep is False:
        print(sheep_count_2)
        break
    else:
        sheep_count_2 += 1
print(sheeps)

'''
HW
1. О цикле for: https://www.google.com/search?q=for+loop+python&client=opera&hs=CU9&ei=eyoDZKqQBOCawPAPy82wuAM&oq=for+loop&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgAMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgcIABCwAxBDMgcIABCwAxBDMgcIABCwAxBDSgQIQRgAUABYAGC-DmgBcAB4AIABAIgBAJIBAJgBAMgBCsABAQ&sclient=gws-wiz-serp
2. Написать программу, котора будет выводить ТОЛЬКО четные числа из range()
3. Бегун за 1 круг выпивает 0.5 л воды. Сколько кругов он сможет пробежать, пока у него не закончится вода?
Задачу решить через for
'''
