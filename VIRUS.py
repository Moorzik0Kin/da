# print("Hello World! (Я взламаю твій пк раніше чим ти подихаєш...)")
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint
app = QApplication([])

win=QWidget()
win.setWindowTitle("Virus.Hack")
win.resize(400, 200)
# Натисни "Замахати", щоб замахати програму
text=QLabel('Натисни щоб дізнатися переможця! ')
winner=QLabel(":)")
button=QPushButton("Згенерувати")
# Замахати
line=QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter )
line.addWidget(winner, alignment=Qt.AlignCenter )
line.addWidget(button, alignment=Qt.AlignCenter )
win.setLayout(line)
# ЗАДРАВ
def show_winner():
    text.setText("Переможець")
    winner.setText(str(randint(1,100)))

button.clicked.connect(show_winner)

win.show()
app.exec_()