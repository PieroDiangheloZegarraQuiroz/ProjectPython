import sys
import subprocess
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QLabel
from PyQt5.QtWidgets import QPushButton


class Games(QDialog):
    def __init__(self):
        super(Games, self).__init__()
        self.initialize()

    def initialize(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setGeometry(550, 250, 500, 650)
        self.setStyleSheet("background-color: white;")
        self.move(650, 150)
        self.display_widgets()

    def display_widgets(self):
        # Buttons
        self.lbl_Title = QLabel("Select Game: ", self)
        self.lbl_Title.setGeometry(200, 70, 150, 30)
        self.lbl_Title.setFont(QFont("Comic Sans MS", 12))
        self.lbl_Title.setStyleSheet("color: black;")

        self.btnAbrir = QPushButton("Stacks", self)
        self.btnAbrir.move(170, 130)
        self.btnAbrir.resize(150, 30)
        self.btnAbrir.setFont(QFont("Comic Sans MS", 12))
        self.btnAbrir.clicked.connect(self.openAbrir)
        self.btnAbrir.setStyleSheet("border-radius: 5px;"
                                    "background-color: rgb(14, 150, 232);"
                                    "color: white;")

        self.btnAbrir1 = QPushButton("Second Game", self)
        self.btnAbrir1.move(170, 180)
        self.btnAbrir1.resize(150, 30)
        self.btnAbrir1.setFont(QFont("Comic Sans MS", 12))
        self.btnAbrir1.clicked.connect(self.openAbrir1)
        self.btnAbrir1.setStyleSheet("border-radius: 5px;"
                                     "background-color: rgb(14, 150, 232);"
                                     "color: white;")

        self.btnAbrir2 = QPushButton("Third Game", self)
        self.btnAbrir2.move(170, 230)
        self.btnAbrir2.resize(150, 30)
        self.btnAbrir2.setFont(QFont("Comic Sans MS", 12))
        self.btnAbrir2.clicked.connect(self.openAbrir2)
        self.btnAbrir2.setStyleSheet("border-radius: 5px;"
                                     "background-color: rgb(14, 150, 232);"
                                     "color: white;")

        self.btnAbrir3 = QPushButton("Fourth Game", self)
        self.btnAbrir3.move(170, 280)
        self.btnAbrir3.resize(150, 30)
        self.btnAbrir3.setFont(QFont("Comic Sans MS", 12))
        self.btnAbrir3.clicked.connect(self.openAbrir3)
        self.btnAbrir3.setStyleSheet("border-radius: 5px;"
                                     "background-color: rgb(14, 150, 232);"
                                     "color: white;")

        self.btnAbrir4 = QPushButton("Fifth Game", self)
        self.btnAbrir4.move(170, 330)
        self.btnAbrir4.resize(150, 30)
        self.btnAbrir4.setFont(QFont("Comic Sans MS", 12))
        self.btnAbrir4.clicked.connect(self.openAbrir4)
        self.btnAbrir4.setStyleSheet("border-radius: 5px;"
                                     "background-color: rgb(14, 150, 232);"
                                     "color: white;")

    def openAbrir(self):
        GamePiero = subprocess.run([sys.executable, '../Student/GamePiero.py'])
        pass

    def openAbrir1(self):
        # Game2 =
        pass

    def openAbrir2(self):
        # Game3 =
        pass

    def openAbrir3(self):
        # Game4 =
        pass

    def openAbrir4(self):
        # Game5 =
        pass