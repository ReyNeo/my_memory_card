from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel)
from random import shuffle

class Question():
    ''' содержит вопрос, правильный ответ и три неправильных'''
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def ask(q):
	lb_question.setText(q.question)
	shuffle(answers)
	answers[0].setText(q.right_answer)
	answers[1].setText(q.wrong1)
	answers[2].setText(q.wrong2)
	answers[3].setText(q.wrong3)

def check_question(q):
	global current_question
	if answers[0].isChecked():
		lb_result.setText('верно!\nэто')
		lb_correct.setText(q.right_answer)
	else:
		lb_result.setText('Неа, \nэто')
		lb_correct.setText(q.right_answer)
	if len(popable_q_list) == 0:
		lb_result.setText('вопросы закончились')
		lb_correct.setText('Мне лень считать')
		lb_question.setText("победила дружба")
		btn_NEXT.setEnabled(False)
def click_1():
	global current_question
	check_question(current_question)
	button_group.hide()
	btn_OK.hide()
	answer_group.show()
	btn_NEXT.show()

def click_2():
	global current_question
	answer_group.hide()
	btn_NEXT.hide()
	button_group.show()
	btn_OK.show()
	print(len(popable_q_list))
	if popable_q_list:
		current_question = popable_q_list.pop()
		ask(current_question)


app = QApplication([])

# BUTTON CREATING
lb_question = QLabel('Most hard question in world!')
lb_result = QLabel('result here')
lb_correct = QLabel('answer here')
btn_OK = QPushButton('Answer')
btn_NEXT = QPushButton('next')
rbtn_1 = QRadioButton('1')
rbtn_2 = QRadioButton('2')
rbtn_3 = QRadioButton('3')
rbtn_4 = QRadioButton('4')
answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

#Questions
q1 = Question('Кто первым полетел в космос?', 'Юрий Гагарин', "Сенатор Армстронг", "Илон Маск", "Питер Паркер")
q2 = Question('Луна это...', "СЫРР!", "планета", "Астероид", "Спутник")
q3 = Question('Вторая мировая война началась в...', "1939", "1941", "1945", "2077")
q4 = Question('Мона Лиза была написана...', "Да Винчи", "Данилом", "Мон Дью Ли Бифштекс", "Гудини")
q_list = [q1,q2,q3,q4]
shuffle(q_list)
popable_q_list = q_list.copy()

#boxgroup
box = QButtonGroup()
box.addButton(rbtn_1)
box.addButton(rbtn_2)
box.addButton(rbtn_3)
box.addButton(rbtn_4)

#button group set
button_group = QGroupBox("ответы:")
button_layout = QHBoxLayout()
button_layout_2 = QVBoxLayout()
button_layout_3 = QVBoxLayout()
button_layout_2.addWidget(rbtn_1)
button_layout_2.addWidget(rbtn_2)
button_layout_3.addWidget(rbtn_3)
button_layout_3.addWidget(rbtn_4)
button_layout.addLayout(button_layout_2)
button_layout.addLayout(button_layout_3)
button_group.setLayout(button_layout)

#answer Layout
answer_group = QGroupBox()
answer_layout = QVBoxLayout()
answer_layout.addWidget(lb_result)
answer_layout.addWidget(lb_correct)
answer_group.setLayout(answer_layout)
answer_group.hide()

#main layout
layout_line = QVBoxLayout()
layout_line.addWidget(lb_question)
layout_line.addWidget(button_group)
layout_line.addWidget(answer_group)
layout_line.addWidget(btn_OK)
layout_line.addWidget(btn_NEXT)
btn_NEXT.hide()

btn_OK.clicked.connect(click_1)
btn_NEXT.clicked.connect(click_2)

if popable_q_list:
    current_question = popable_q_list.pop()
    ask(current_question)

window = QWidget()
window.setLayout(layout_line)
window.setWindowTitle('Memo Card')

window.show()
app.exec()