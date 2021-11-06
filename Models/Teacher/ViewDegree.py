from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QPushButton
from Models.Teacher import ShowStudent, ShowStudent1, ShowStudent2


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
        self.cuarto = ShowStudent1.ShowStudentFive1(self.idCode)
        self.sexto = ShowStudent2.ShowStudentFive2(self.idCode)

        # Buttons
        self.btnAbrir = QPushButton("6to", self)
        self.btnAbrir.move(170, 90)
        self.btnAbrir.resize(150, 30)
        self.btnAbrir.setFont(QFont("Comic Sans MS", 12))
        self.btnAbrir.clicked.connect(self.openAbrir)
        self.btnAbrir.setStyleSheet("border-radius: 5px;"
                                    "background-color: rgb(14, 150, 232);"
                                    "color: white;")
        self.btnAbrir1 = QPushButton("5to", self)
        self.btnAbrir1.move(170, 140)
        self.btnAbrir1.resize(150, 30)
        self.btnAbrir1.setFont(QFont("Comic Sans MS", 12))
        self.btnAbrir1.clicked.connect(self.openAbrir1)
        self.btnAbrir1.setStyleSheet("border-radius: 5px;"
                                    "background-color: rgb(14, 150, 232);"
                                    "color: white;")

        self.btnAbrir2 = QPushButton("4to", self)
        self.btnAbrir2.move(170, 190)
        self.btnAbrir2.resize(150, 30)
        self.btnAbrir2.setFont(QFont("Comic Sans MS", 12))
        self.btnAbrir2.clicked.connect(self.openAbrir2)
        self.btnAbrir2.setStyleSheet("border-radius: 5px;"
                                     "background-color: rgb(14, 150, 232);"
                                     "color: white;")

        # self.btnAbrir3 = QPushButton("3ro", self)
        # self.btnAbrir3.move(170, 240)
        # self.btnAbrir3.resize(150, 30)
        # self.btnAbrir3.setFont(QFont("Comic Sans MS", 12))
        # self.btnAbrir3.clicked.connect(self.open)
        # self.btnAbrir3.setStyleSheet("border-radius: 5px;"
        #                              "background-color: rgb(14, 150, 232);"
        #                              "color: white;")

    def openAbrir(self):
        self.sexto.show()
        pass
    def openAbrir1(self):
        self.quinto.show()
        pass
    def openAbrir2(self):
        self.cuarto.show()
        pass

