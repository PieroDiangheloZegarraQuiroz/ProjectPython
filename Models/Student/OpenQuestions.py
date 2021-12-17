import sys
from urllib import request

from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox, QLabel, QScrollArea, QVBoxLayout, QFormLayout, \
    QGroupBox, QDialog, QLineEdit, QPushButton

from Connection import ConnectionDB


class OpenQuestions(QDialog):
    def __init__(self, idForm):
        super(OpenQuestions, self).__init__()
        self.idForm = str(idForm)
        self.initialize()

    def initialize(self):
        self.setStyleSheet("background-color: white;")
        # self.resize(600, 500)
        self.setGeometry(550, 250, 500, 650)
        self.move(650, 150)
        self.setWindowTitle("Lecturas recomendadas")
        self.display_widgets()

    def display_widgets(self):

        formLayout = QFormLayout()
        groupBox = QGroupBox()

        results, quantity = ConnectionDB.Connection().readQuestions(self.idForm)
        #
        self.urls = []
        for u in results:
            self.urls.append(u)

        self.vars = []
        for i in range(quantity):
            self.vars.append(f'labs{i + 1}')

        self.input = []
        for i in range(quantity):
            self.input.append(f'in{i + 1}')

        self.buttonSave = QPushButton("Responder", self)
        self.buttonSave.resize(100, 30)
        self.buttonSave.move(50, 80)
        self.buttonSave.setEnabled(False)
        self.buttonSave.setFont(QFont("Comic Sans MS", 12))
        self.buttonSave.clicked.connect(self.saveResponse)
        self.buttonSave.setStyleSheet("border-radius: 5px;"
                                      "background-color: rgb(14, 150, 232);"
                                      "color: white;")

        for i in range(10):
            self.vars = QLabel(f'<b>{i + 1}) {self.urls[i]}</b>', self)
            self.vars.setFont(QFont("Comic Sans MS", 10))
            self.vars.move(30, 50 * (i + 1))

            self.input = QLineEdit(self)
            self.input.resize(300, 30)
            self.input.move(30, 60 * (i + 1))
            self.input.setFont(QFont("Comic Sans MS", 8))

            formLayout.setContentsMargins(50, 10, 5, 5)
            formLayout.setHorizontalSpacing(100)
            formLayout.setVerticalSpacing(50)
            formLayout.addRow(self.vars)
            formLayout.addRow(self.input)
            formLayout.setAlignment(Qt.AlignCenter)

        formLayout.addRow(self.buttonSave)
        groupBox.setLayout(formLayout)

        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)

        layout = QVBoxLayout(self)
        layout.addWidget(scroll)

    def saveResponse(self):
        pass


