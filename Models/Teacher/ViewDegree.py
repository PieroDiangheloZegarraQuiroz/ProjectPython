from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QPushButton
from Models.Teacher import ShowStudent


class ViewStudents(QDialog):
    def __init__(self, idCode):
        super(ViewStudents, self).__init__()
        self.idCode = str(idCode)
        self.initialize()

    def initialize(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setGeometry(550, 250, 500, 650)
        self.setStyleSheet("background-color: white;")
        self.move(650, 150)
        self.display_widgets()

    def display_widgets(self):
        # Data
        self.quinto = ShowStudent.ShowStudentFive(self.idCode)

        # Buttons
        self.btnAbrir = QPushButton("5to", self)
        self.btnAbrir.move(170, 90)
        self.btnAbrir.resize(150, 30)
        self.btnAbrir.setFont(QFont("Comic Sans MS", 12))
        self.btnAbrir.clicked.connect(self.openAbrir)
        self.btnAbrir.setStyleSheet("border-radius: 5px;"
                                    "background-color: rgb(14, 150, 232);"
                                    "color: white;")

        self.btnAbrir1 = QPushButton("4to", self)
        self.btnAbrir1.move(170, 140)
        self.btnAbrir1.resize(150, 30)
        self.btnAbrir1.setFont(QFont("Comic Sans MS", 12))
        self.btnAbrir1.clicked.connect(self.open)
        self.btnAbrir1.setStyleSheet("border-radius: 5px;"
                                     "background-color: rgb(14, 150, 232);"
                                     "color: white;")

        self.btnAbrir2 = QPushButton("3ro", self)
        self.btnAbrir2.move(170, 190)
        self.btnAbrir2.resize(150, 30)
        self.btnAbrir2.setFont(QFont("Comic Sans MS", 12))
        self.btnAbrir2.clicked.connect(self.open)
        self.btnAbrir2.setStyleSheet("border-radius: 5px;"
                                     "background-color: rgb(14, 150, 232);"
                                     "color: white;")

    def openAbrir(self):
        self.quinto.show()
        pass
