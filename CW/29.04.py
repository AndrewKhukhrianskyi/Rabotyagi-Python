from tkinter import *
from random import randint


def save_data():
    text = text_field.get(0.0, END) # get() позволяет достать текст из поля
    print('Saved data!')
    print('------------------')
    print(text)
    print('------------------')
    label['text'] = 'NEW VALUE!' # изменения любого виджета происходит в такой форме

def clear_data():
    text_field.delete(0.0, END) # delete() позволяет удалить данные из поля
    print('Data was cleared!')

def some_meow():
    text = text_field.get(0.0, END)
    if 'meow' in text.lower():
        meow_text = ''
        for meow in range(randint(10, 100)):
            meow_text += 'meow!'
        text_field.delete(0.0, END)
        text_field.insert(0.0, meow_text.upper()) # insert() позволяет вставить данные в поле
    


'''
window = Tk()
# Task - Pad
window.resizable(False, False)
window.title('Some random window')
window.geometry('500x500')


label = Label(width = 20,
              height = 1,
              text = 'Enter your text below:')

text_field = Text(width = 50,
                  height = 20)

save_button = Button(width = 5,
                     height = 1,
                     text = 'Save!',
                     command = save_data)
clear_button = Button(width = 5,
                     height = 1,
                     text = 'Clear!',
                     command = clear_data)
meow_button = Button(width = 5,
                     height = 1,
                     text = 'Meow!',
                     command = some_meow)

widgets = [label, text_field,
           save_button, clear_button, meow_button]
for widget in widgets:
    widget.pack()
'''
# Task - random values
window = Tk()

def generate_numbers():
    pc_number = randint(1, 5)
    player_number = randint(1, 5)
    label1['text'] = f'PC: {pc_number}'
    label2['text'] = f'Player: {player_number}'
    if pc_number == player_number:
        label3['text'] = 'Result: Draw!'
    elif pc_number > player_number:
        label3['text'] = 'Result: PC Win!'
    elif pc_number < player_number:
        label3['text'] = 'Result: Player Win!'
window.resizable(False, False)
window.title('Random value app v.1.0.0')
window.geometry('200x100')

label1 = Label(width = 10,
               height = 1,
               text = 'PC: ')
label2 = Label(width = 10,
               height = 1,
               text = 'Player: ')
label3 = Label(width = 20,
               height = 1,
               text = 'Result: ')
button = Button(width = 5,
                height = 1,
                text = 'Start!',
                command = generate_numbers)

widgets = [label1, label2,
           label3, button]
for widget in widgets:
    widget.pack()
    
window.mainloop()
