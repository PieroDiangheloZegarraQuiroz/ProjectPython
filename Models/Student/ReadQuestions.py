import sys
from urllib import request

from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox, QLabel, QScrollArea, QVBoxLayout, QFormLayout, \
    QGroupBox, QDialog

from Connection import ConnectionDB
from Models.Student import OpenQuestions


class QLabelClick(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        textId = str(self.text())
        indice0 = textId.index(' ')
        indicef = textId.index('</label>')
        self.idForm = textId[indice0:indicef].strip()
        self.openQes = OpenQuestions.OpenQuestions(self.idForm)
        self.openQes.show()


class ReadQuestions(QDialog):
    def __init__(self, codeId):
        super(ReadQuestions, self).__init__()
        self.codeId = str(codeId)
        self.initialize()

    def initialize(self):
        self.setStyleSheet("background-color: white;")
        # self.resize(600, 500)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setGeometry(550, 250, 500, 650)
        self.move(650, 150)
        self.setWindowTitle("Lecturas recomendadas")
        self.display_widgets()

    def display_widgets(self):

        formLayout = QFormLayout()
        groupBox = QGroupBox()

        results, quantity = ConnectionDB.Connection().listQuestions(self.codeId)
        #
        self.urls = []
        for u in results:
            self.urls.append(u[0])
        print(results)
        #

        self.vars = []
        for i in range(quantity):
            self.vars.append(f'labs{i + 1}')

        for i in range(quantity):
            self.vars = QLabelClick(f'<b>Tarea\t{i + 1}</b><label\tstyle="color:white;"> {self.urls[i]}</label>', self)
            self.vars.setFont(QFont("Comic Sans MS", 10))
            self.vars.move(30, 50 * (i + 1))

            formLayout.setContentsMargins(50, 10, 5, 5)
            formLayout.setHorizontalSpacing(100)
            formLayout.setVerticalSpacing(50)
            formLayout.addRow(self.vars)
            formLayout.setAlignment(Qt.AlignCenter)

        groupBox.setLayout(formLayout)

        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)

        layout = QVBoxLayout(self)
        layout.addWidget(scroll)


