from tkinter import *

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
def result_window():
    result_win = Toplevel()
    
    result_win.geometry('300x150')
    result_win.resizable(False, False)
    result_win.title('Result')
    
    number_1 = int(field_1.get(0.0, END).strip())
    number_2 = int(field_2.get(0.0, END).strip())
    label = Label(result_win,
                  width = 20,
                  height = 1,
                  text = f'{number_1} + {number_2} = {number_1 + number_2}')
    label.pack()
    
window = Tk()
window.geometry('200x150')
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
button = Button(width = 5,
                height = 1,
                text = 'Click!',
                command = result_window)
widgets = [label_1, field_1,
           label_2, field_2,
           button]

for widget in widgets:
    widget.pack()
window.mainloop()
