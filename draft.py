# Сначала берём инфу из файлов
# Создаём цикл
# В нём прогружаются вступление, правила каждый раз одинакого поэтому они не входят в цикл
# Но! На каждой иттерации поле вопроса меняется, а поле ответа очищается (возможно что-то с кнопкой ДАЛЕЕ)
# Переход на следующую иттерацию осуществляется только после нажатия кнопки

import random
from tkinter import *

root = Tk()
root.title('Викторина')
root.geometry('1600x300')#+800+200')

f_Questions = open('Questions.txt', 'r+', encoding='utf-8')
Questions = f_Questions.readlines()
f_Questions.close()
New_Questions = []
for Question in Questions:
	if Question.endswith('\n'):
		New_Questions.append(Question[:-1])
	else:
		New_Questions.append(Question)
Questions.clear()
f_Answers= open('Answers.txt', 'r+', encoding='utf-8')
Answers = f_Answers.readlines()
f_Answers.close()
New_Answers = []
for Answer in Answers:
	if Answer.endswith('\n'):
		New_Answers.append(Answer[:-1])
	else:
		New_Answers.append(Answer)
Answers.clear()

text_1 = Label(root, font=("Gotham Pro Black", 20),text = "Приветствую дорогой друг, это проект Анатолия Солдатова и Михаила Семенова.\n В нём тебе предстоит пройти проверку на знание английских неправильных глаголов.")
text_1.grid(column = 0, row = 0)
text_2 = Label(root, font=('Gotham Pro Regular',12), text = "Правила просты: \n 1) При получении вопроса нужно ввести 2-ую и 3-ию форму глагола через пробел и каждое слово с заглавной буквы\n 2) Если есть 2 формы, зависящие от лица, их надо писать через '/' без пробела")
text_2.grid(column = 0,row = 1)

def _check():
	global numQA
	global Points
	global New_Answer
	New_Answer = f'{INPUT.get()}'
	check = New_Answer == New_Answers[n]
	if check == True:
		Points += 1
		New_Questions.remove(New_Question)
		New_Answers.remove(New_Answer)
		msg_lbl.configure(text = 'Верно')
		numQA -= 1

		LIST1.configure(text = f'{New_Questions}')
		LIST2.configure(text = f'{New_Answers}')
	elif check == False:
		msg_lbl.configure(text =  'Неверно')
		# Увелечение вероятности
	points_lbl.configure(text=f'Points: {Points}')

	CHECK1.configure(text = f'New_Question: {New_Question}') #t
	CHECK2.configure(text = f'New_Answer: {New_Answer}') #t


def _nextMove():
	msg_lbl.configure(text = '')
	global New_Answer
	New_Answer = ''
	n = random.randint(0,numQA)
	Que_lbl.configure(text = f'{New_Questions[n]}')
	New_Question = f'{New_Questions[n]}'
	INPUT.delete(0,END)

	CHECK1.configure(text=f'New_Question: {New_Question}') #t
	CHECK2.configure(text=f'New_Answer: {New_Answer}') #t

Points = 0
numQA = 2

n = random.randint(0,numQA)
New_Question = New_Questions[n]

Que_lbl = Label(root, font=("Gotham Pro Black", 20), text = f'{New_Question}', padx = 25, pady = 25)
Que_lbl.grid(column = 0, row = 2)

INPUT = Entry(root, width = 25)
INPUT.grid(column = 1, row = 2)
INPUT.focus()

btn_check = Button(root, text = 'Check', padx = 25, command = _check)
btn_check.grid(column = 2, row = 2)

btn_next = Button(root, text = 'Next', padx = 25, command = _nextMove)
btn_next.grid(column = 3, row = 2)

msg_lbl = Label(root, text = 'Hi!')
msg_lbl.grid(column = 0, row = 3)

points_lbl = Label(root, text = 'Points: 0')
points_lbl.grid(column = 2, row = 3)

#t_1
CHECK1 = Label(root, text = 'New_Question: ')
CHECK1.grid(column = 0,row = 4)
CHECK2 = Label(root, text = 'New_Answer: ')
CHECK2.grid(column = 2,row = 4)
LIST1 = Label(root, font = ('Gotham Pro Regular',10),text= f'{New_Questions}')
LIST1.grid(column = 0, row = 5)
LIST2 = Label(root, font = ('Gotham Pro Regular',10), text= f'{New_Answers}')
LIST2.grid(column = 0, row = 6)
#t_1


root.mainloop()