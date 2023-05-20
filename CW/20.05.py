from tkinter import *

import tkinter.messagebox as mb
'''
def open_new_window():
    new_window = Toplevel() # Триггер на создание нового окна
    # Toplevel имеет те же свойства что и обычное окно
    new_window.title('New window')
    new_window.geometry('200x200')
    new_window.resizable(False, False)
    # Если не задавать конкретное окно - крепится к основному
    label = Label(new_window,
                  width = 10,
                  height = 1,
                  text = 'Hello!')
    label.pack()

window = Tk()

window.geometry('150x300')
window.resizable(False, False)
window.title('Window')

btn = Button(width = 5,
             height = 1,
             text = 'Тык',
             command = open_new_window)

btn.pack()

window.mainloop()
'''

# Task - Calculator
def add_window():
    try:
        number_1 = int(field_1.get(0.0, END).strip())
        number_2 = int(field_2.get(0.0, END).strip())
        result_win = Toplevel()
        result_win.geometry('300x50')
        result_win.resizable(False, False)
        result_win.title('Result')

        label = Label(result_win,
                  width = 20,
                  height = 1,
                  text = f'{number_1} + {number_2} = {number_1 + number_2}')
        label.pack()
    except ValueError:
        mb.showerror(title = 'Error',
                     message = 'You are debil, my friend :)')
        
    

def div_window():
    try:
        number_1 = int(field_1.get(0.0, END).strip())
        number_2 = int(field_2.get(0.0, END).strip())
        
        result_win = Toplevel()
        result_win.geometry('300x50')
        result_win.resizable(False, False)
        result_win.title('Result')
        

        label = Label(result_win,
                  width = 20,
                  height = 1,
                  text = f'{number_1} : {number_2} = {number_1 / number_2}')
        label.pack()
    except ValueError:
        mb.showerror(title = 'Error',
                     message = 'You are debil, my friend :)')
    

def mul_window():
    try:
        number_1 = int(field_1.get(0.0, END).strip())
        number_2 = int(field_2.get(0.0, END).strip())
        
        result_win = Toplevel()
    
        result_win.geometry('300x50')
        result_win.resizable(False, False)
        result_win.title('Result')
        label = Label(result_win,
                  width = 20,
                  height = 1,
                  text = f'{number_1} x {number_2} = {number_1 * number_2}')
        label.pack()
        
    except ValueError:
        mb.showerror(title = 'Error',
                     message = 'You are debil, my friend :)')
    

def min_window():
    try:
        number_1 = int(field_1.get(0.0, END).strip())
        number_2 = int(field_2.get(0.0, END).strip())
        result_win = Toplevel()
    
        result_win.geometry('300x50')
        result_win.resizable(False, False)
        result_win.title('Result')

        label = Label(result_win,
                  width = 20,
                  height = 1,
                  text = f'{number_1} - {number_2} = {number_1 - number_2}')
        label.pack()
    except ValueError:
        mb.showerror(title = 'Error',
                     message = 'You are debil, my friend :)')
        
    
    
window = Tk()
window.geometry('200x250')
window.resizable(False, False)
window.title('Calculator')

label_1 = Label(width = 10,
                height = 1,
                text = 'Field 1:')
field_1 = Text(width = 5,
               height = 1)
label_2 = Label(width = 10,
                height = 1,
                text = 'Field 2:')
field_2 = Text(width = 5,
               height = 1)
add_button = Button(width = 5,
                height = 1,
                text = '+',
                command = add_window)
div_button = Button(width = 5,
                height = 1,
                text = ':',
                command = div_window)
mul_button = Button(width = 5,
                height = 1,
                text = 'X',
                command = mul_window)
min_button = Button(width = 5,
                height = 1,
                text = '-',
                command = min_window)
widgets = [label_1, field_1,
           label_2, field_2,
           add_button, div_button,
           mul_button, min_button]

for widget in widgets:
    widget.pack()
window.mainloop()

'''
Home work:
1. Почитать, что такое тестирование:
https://qalight.ua/ru/baza-znaniy/chto-takoe-testirovanie-programmnogo-obespecheniya/
2. Почитать о принципах тестирования:
https://habr.com/ru/articles/699990/
3. Почитать о тестовой документации
https://habr.com/ru/companies/otus/articles/588923/
'''
