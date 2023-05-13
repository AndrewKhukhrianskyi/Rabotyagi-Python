from tkinter import *
from random import randint, choice
import tkinter.messagebox as mb # Добавляем коробки с сообщениями
'''
def congratulation():
    mb.showinfo(title = 'Info',
                message = 'Инфо: Вы умный.')
    mb.showerror(title = 'Error',
                 message = "Ошибка: Это ошибка.")
    mb.showwarning(title = 'Warning',
                   message = 'Внимание! Вы - умный.')

# Task 1 - generate numbers app
def generate_numbers():
    pc_number = randint(1, 5)
    player_number = randint(1, 5)
    if player_number > pc_number:
        mb.showinfo(title = 'Win',
                    message = 'Player win!')
    elif player_number < pc_number:
        mb.showerror(title = 'Lose',
                     message = 'PC win!')
    else:
        mb.showwarning(title = 'Draw',
                       message = "It's a draw!")
    mb.showinfo(title = 'Results',
                message = f'Player: {player_number}, PC: {pc_number}')
window = Tk()

window.geometry('100x100')
window.resizable(False, False)
window.title('Window')

btn = Button(width = 8,
             height = 1,
             text = 'Click!',
             command = generate_numbers)
btn.pack()

window.mainloop()

# Приложение должно использовать одинаковые виды запаковки
def packing():
    random_number = randint(1, 1000)
    anchors = 'n', 's', 'e', 'w'
    btn_N = Button(width = 8,
                   height = 1,
                   text = f'BTN #{random_number}')
    
    btn_N.pack(anchor=choice(anchors))

def gridding():
    random_number = randint(1, 1000)
    random_col = randint(1, 10)
    random_row = randint(1, 10)
    btn_N = Button(width = 8,
                   height = 1,
                   text = f'BTN #{random_number}')
    btn_N.grid(column = random_col,
               row = random_row)
def placing():
    random_number = randint(1, 1000)
    random_y = randint(5, 495)
    random_x = randint(5, 495)
    btn_N = Button(width = 8,
                   height = 1,
                   text = f'BTN #{random_number}')
    btn_N.place(y = random_y,
                x = random_x)

window = Tk()
window.geometry('500x500')
window.resizable(False, False)

btn = Button(width = 8,
             height = 1,
             text = 'Btn',
             command = placing)
btn.place(x = 1,
          y = 1)

window.mainloop()
'''
# Task - Login form
def check():
    logins = ['admin','user','qwerty']
    pwds = ['pwd01', 'user123','qwty']
    entry_login = entry_1.get(0.0, END).strip()
    entry_pwd = entry_2.get(0.0, END).strip()
    if entry_login in logins and entry_pwd in pwds:
        mb.showinfo(title = 'OK',
                    message = 'Welcome, user!')
    else:
        mb.showerror(title = 'Error',
                     message = 'Incorrect login or pwd!')

window = Tk()

window.geometry('250x100')
window.title('Login')
window.resizable(False, False)

lab1 = Label(text = 'Login:',
             width = 5,
             height = 1)
lab2 = Label(text = 'Password:',
             width = 10,
             height = 1)
entry_1 = Text(width = 20,
               height = 1)
entry_2 = Text(width = 20,
               height = 1)

btn = Button(width = 5,
             height = 1,
             text = 'Login',
             command = check)

lab1.grid(column = 0,
          row = 0)
lab2.grid(column = 0,
          row = 1)
entry_1.grid(column = 1,
             row = 0)

entry_2.grid(column = 1,
             row = 1)

btn.grid(column = 1,
         row = 2)


window.mainloop()

'''
HW
1. Почитать о pack, grid, place: https://www.pythontutorial.net/tkinter/tkinter-grid/
2. Почитать о messagebox: https://www.pythontutorial.net/tkinter/tkinter-messagebox/
3. Пофиксить код для логина пользователя в систему
   - Проверка в формате логин - пароль
   - Подрихтовать расположение кнопок
   - Сделать проверки на пустые поля
'''


