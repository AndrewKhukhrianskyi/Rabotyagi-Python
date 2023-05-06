# Викторина
from tkinter import *
from random import choice
# Константа - постоянное выражение
# Константы пишутся с больших букв и видны везде!
QUESTION_LIST = {"Зимой и летом одним цветом:" : "Елка",
                 "Висит груша, нельзя скушать" : "Лампочка"}

window = Tk()
window.geometry('300x150')
window.resizable(False, False)
window.title('Викториныч')

def loser():
    print('LOSER!')

def check_answer():
    answer = text_field.get(0.0, END).strip().lower()
    label_text = question_label.cget('text')
    value_border = label_text.find(' ')
    value = QUESTION_LIST.pop(label_text[value_border + 1::]).lower()
    if answer == value:
        score = score_label.cget('text')
        border = score.find(' ')
        score_number = int(score[border::])
        score_number += 1
        score_label['text']=f'Score: {score_number}'
        question_label['text'] = 'Question: ' + choice(list(QUESTION_LIST.keys()))
    else:
        score_label['text']='GAME OVER!'
        answer_button['command'] = loser

            

question_label = Label(width = 40,
                       height = 1,
                       text = f'Question: {choice(list(QUESTION_LIST.keys()))}')
score_label = Label(width = 40,
                    height = 1,
                    text = f'Score: 0')
text_field = Text(width = 20,
                  height = 1)

answer_button = Button(width = 5,
                       height = 1,
                       text = 'Click!',
                       command = check_answer)

widgets = [question_label,
           score_label,
           text_field,
           answer_button]

for widget in widgets:
    widget.pack()

window.mainloop()
