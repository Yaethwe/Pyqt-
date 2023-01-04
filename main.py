import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
import webbrowser as wb

widgets = {
    "logo":[],
    "button":[],
    "score":[],
    "question":[],
    "answer1":[],
    "answer2":[],
    "answer3":[],
    "answer4":[],
    "logo_bottom":[],
    "congrat":[],
    "bad":[],
}

stylesheet = """
background: #161219;
"""
btn = """
*{border: 4px solid '#BC006C';
border-radius: 20px;
font-size: 35px;
color: white;
font-family: sans-serif;
padding: 5px;
}
*:hover{
    background: '#BC006C';
}
"""

text_style = """
    font-family: Shanti;
    font-size: 25px;
    color: white;
    padding: 75px;
"""

def create_buttons(answer):
    button = QPushButton(answer)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setFixedWidth(485)
    button.setStyleSheet(btn)
    return button


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Who wants to be a programmer???')
window.setWindowIcon(QtGui.QIcon('img/fav.png'))
window.setFixedWidth(1000)
window.move(100, 100)
window.setStyleSheet(stylesheet)

grid = QGridLayout()

def clear_widgets():
    for widget in widgets:
        if widgets[widget] != []:
           widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()

def start_game():
    clear_widgets()
    frame2()

def end_game():
    clear_widgets()
    frame3()

def bad_game():
    clear_widgets()
    frame4()

def open_website():
    wb.open("https://cooldevs.netlify.app")

def frame1():
    image = QPixmap("img/logo.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 100px;")
    widgets["logo"].append(logo)

    button = QPushButton("PLAY")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(btn)
    button.clicked.connect(start_game)
    widgets["button"].append(button)

    grid.addWidget(widgets["logo"][-1], 0, 0)
    grid.addWidget(widgets["button"][-1], 1, 0)

def frame2():
    score = QLabel("80")
    score.setAlignment(QtCore.Qt.AlignRight)
    score.setStyleSheet("""
        border-radius: 20px;
        color: white;
        font-size: 35px;
        padding: 25px 20px 0px 20px;
        border: 1px solid '#64A314';
        margin: 20px 200px;
        padding: 5px;
    """)
    widgets["score"].append(score)

    question = QLabel(
    """
    YeaeThawe (Cool-Devs) created this App. 
    What programming language did he use to create this App?
    Choose the correct answer in the following.
    """)
    question.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet(text_style)
    widgets["question"].append(question)
    
    button1 = create_buttons("Python")
    button2 = create_buttons("JavaScript")
    button3 = create_buttons("Java")
    button4 = create_buttons("NodeJS")
    button1.clicked.connect(end_game)
    button2.clicked.connect(bad_game)
    button3.clicked.connect(bad_game)
    button4.clicked.connect(bad_game)
    widgets["answer1"].append(button1)
    widgets["answer2"].append(button2)
    widgets["answer3"].append(button3)
    widgets["answer4"].append(button4)

    image = QPixmap("img/logo_bottom.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 75px; margin-bottom: 30px;")
    widgets["logo_bottom"].append(logo)

    grid.addWidget(widgets["score"][-1], 0, 1)
    grid.addWidget(widgets["question"][-1], 1, 0, 1, 2)
    grid.addWidget(widgets["answer1"][-1], 2, 0)
    grid.addWidget(widgets["answer2"][-1], 2, 1)
    grid.addWidget(widgets["answer3"][-1], 3, 0)
    grid.addWidget(widgets["answer4"][-1], 3, 1)
    grid.addWidget(widgets["logo_bottom"][-1], 4, 0, 1, 2)

def frame3():
    congrat = QLabel(
    """
    Congratulations!
    You successfully passed the Programming test! :)
    
    Connect me
        yeaethawe@gmail.com
    """)
    congrat.setAlignment(QtCore.Qt.AlignCenter)
    congrat.setWordWrap(True)
    congrat.setStyleSheet(text_style)
    widgets["congrat"].append(congrat)
    button = QPushButton("Open Cool-Devs in Browser")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(btn)
    button.clicked.connect(open_website)
    widgets["button"].append(button)

    

    grid.addWidget(widgets["button"][-1], 2, 0)
    
    grid.addWidget(widgets["congrat"][-1], 1, 0)

def frame4():
    bad = QLabel(
    """
    Wrong Answer!
    You need to learn more about programming langages! :)
    Try again.
    
    Connect me
        yeaethawe@gmail.com
    """)
    bad.setAlignment(QtCore.Qt.AlignCenter)
    bad.setWordWrap(True)
    bad.setStyleSheet(text_style)
    widgets["bad"].append(bad)

    button = QPushButton("REPLAY")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(btn)
    button.clicked.connect(start_game)
    
    widgets["button"].append(button)

    grid.addWidget(widgets["button"][-1], 2, 0)
    grid.addWidget(widgets["bad"][-1], 1, 0)

frame1()

window.setLayout(grid)

window.show()

sys.exit(app.exec())
