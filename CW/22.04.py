from tkinter import * # подключаем ткинтер
from random import choice

def generate_button():
    new_button = Button(width = 15,
                        height = 1,
                        text = 'NEW BUTTON')
    packs = 'n', 's', 'w', 'e'
    new_button.pack(anchor = choice(packs))

def get_wolf_text():
    random_wolf_phrases = ['Если волк голоден - он ест.',
                           'Если волк молчит, то лучше его не перебивать',
                           'Я купил 1% кефир и поставил его на зарядку',
                           'Моего друга сбила машина и он мне не друг, ведь друзья на дороге не валяются']
    print(choice(random_wolf_phrases))

random_names = ['Окно', "Окошечко", "Снова окно.", "Вау. Окно."]
# root или window
window = Tk() # Tk() подключает работу с ОСНОВНЫМ окном
'''
window.title(choice(random_names)) # .title() меняет название приложение

window.geometry('300x300') # .geometry выставляет размер экрана в формате ширинахвысота
window.resizable(False, False) # resizable разрешает или запрещает изменять размер экрана по ширине или высоте
# Task - написать программу, которая будет рандомно менять название экрана приложения


btn = Button(width = 8,
             height = 2,
             text = 'BUTTON!',
             bg = 'red',
             command = get_wolf_text)
btn2 = Button(width = 10,
              height = 2,
              text = 'NEW BUTTON!',
              command = generate_button)

# pack(NSWE)
btn2.pack(anchor = 'n')
btn.pack(anchor='n')

# Task - написать программу, которая будет плодить новые кнопки на экране
window.mainloop() # mainloop() позволяет "переиспользовать" приложение, не закрывая его
'''

'''
Homework
1. Игра больше\меньше.
Написать приложение, где будут 3 кнопки (Старт, Больше, Меньше)
При нажатии кнопки старт, пользователя просят написать число в промежутках
от 1 до 100 и установить границу

Кнопки "Больше" и "Меньше" будут определять, больше будет число или меньше

2. Сделать защииту от дурака в приложении. Нужно сделать проверку, если человек
загадает число меньше 0 или больше 100

3. Почитать о кнопках in Tkinter
'''
