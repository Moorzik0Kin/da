from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox

app = QApplication([])
win=QWidget()
# Конкурс від Crazy People
win.setWindowTitle("81+ (Кадри)")
win.resize(400, 200)
# В якому році канал отримав" золоту кнопку "від YouTube?
queshion=QLabel('У якому рокі по який, дєди голодали?')
# 2005, 2015, 2010, 2020
option1=QRadioButton("1945-Зараз")
option2=QRadioButton("1945-2000")
option3=QRadioButton("2000-2020")
option4=QRadioButton("100-2024")

line=QVBoxLayout()
line.addWidget(queshion, alignment=Qt.AlignCenter )

line_H1=QHBoxLayout()
line_H1.addWidget(option1, alignment=Qt.AlignCenter )
line_H1.addWidget(option2, alignment=Qt.AlignCenter )

line_H2=QHBoxLayout()
line_H2.addWidget(option3, alignment=Qt.AlignCenter )
line_H2.addWidget(option4, alignment=Qt.AlignCenter )

line.addLayout(line_H1)
line.addLayout(line_H2)
win.setLayout(line)

def show_win():
    win_win=QMessageBox()
    win_win.setWindowTitle("1945-Зараз")
    win_win.setText('Правильно! \n Ви виграли Гіроскутер!')
    win_win.exec_()

def loser_win(a):
    loser_win=QMessageBox()
    loser_win.setWindowTitle(a)
    loser_win.setText('Не правильно! \n Ви виграли Плакат!')
    loser_win.exec_()

option1.clicked.connect(show_win)
option2.clicked.connect(loser_win,a=1900)
option3.clicked.connect(loser_win)
option4.clicked.connect(loser_win)

win.show()
app.exec_()