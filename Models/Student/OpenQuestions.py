import sys
from urllib import request

import quantity as quantity
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QScrollArea, QVBoxLayout, QFormLayout, \
    QGroupBox, QDialog, QLineEdit, QPushButton, QMessageBox

from Connection import ConnectionDB
from Models.General import Login
from Models.Student import General_Interface


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

        results, self.quantity = ConnectionDB.Connection().readQuestions(self.idForm)
        #
        self.urls = []
        for u in results:
            self.urls.append(u)

        self.vars = []
        for i in range(self.quantity):
            self.vars.append(f'labs{i + 1}')

        self.resp = QLabel('Respuestas', self)
        self.resp.setFont(QFont("Comic Sans MS", 10))

        self.input1 = QLineEdit(self)
        self.input1.resize(300, 30)
        self.input1.setText(" ")
        self.input1.setFont(QFont("Comic Sans MS", 8))

        self.input2 = QLineEdit(self)
        self.input2.resize(300, 30)
        self.input2.setText(" ")
        self.input2.setFont(QFont("Comic Sans MS", 8))

        self.input3 = QLineEdit(self)
        self.input3.resize(300, 30)
        self.input3.setText(" ")
        self.input3.setFont(QFont("Comic Sans MS", 8))

        self.input4 = QLineEdit(self)
        self.input4.resize(300, 30)
        self.input4.setText(" ")
        self.input4.setFont(QFont("Comic Sans MS", 8))

        self.input5 = QLineEdit(self)
        self.input5.resize(300, 30)
        self.input5.setText(" ")
        self.input5.setFont(QFont("Comic Sans MS", 8))

        self.input6 = QLineEdit(self)
        self.input6.resize(300, 30)
        self.input6.setText(" ")
        self.input6.setFont(QFont("Comic Sans MS", 8))

        self.input7 = QLineEdit(self)
        self.input7.resize(300, 30)
        self.input7.setText(" ")
        self.input7.setFont(QFont("Comic Sans MS", 8))

        self.input8 = QLineEdit(self)
        self.input8.resize(300, 30)
        self.input8.setText(" ")
        self.input8.setFont(QFont("Comic Sans MS", 8))

        self.input9 = QLineEdit(self)
        self.input9.resize(300, 30)
        self.input9.setText(" ")
        self.input9.setFont(QFont("Comic Sans MS", 8))

        self.input10 = QLineEdit(self)
        self.input10.resize(300, 30)
        self.input10.setText(" ")
        self.input10.setFont(QFont("Comic Sans MS", 8))

        self.buttonSave = QPushButton("Responder", self)
        self.buttonSave.resize(100, 30)
        self.buttonSave.move(50, 80)
        self.buttonSave.setEnabled(True)
        self.buttonSave.setFont(QFont("Comic Sans MS", 12))
        self.buttonSave.clicked.connect(self.saveResponse)
        self.buttonSave.setStyleSheet("border-radius: 5px;"
                                      "background-color: rgb(14, 150, 232);"
                                      "color: white;")

        for i in range(10):
            self.vars = QLabel(f'<b>{i + 1}) {self.urls[i]}</b>', self)
            self.vars.setFont(QFont("Comic Sans MS", 10))
            self.vars.move(30, 50 * (i + 1))
            formLayout.setContentsMargins(50, 10, 5, 5)
            formLayout.setHorizontalSpacing(100)
            formLayout.setVerticalSpacing(50)
            formLayout.addRow(self.vars)

            formLayout.setAlignment(Qt.AlignCenter)

        formLayout.addRow(self.resp)
        formLayout.addRow(self.input1)
        formLayout.addRow(self.input2)
        formLayout.addRow(self.input3)
        formLayout.addRow(self.input4)
        formLayout.addRow(self.input5)
        formLayout.addRow(self.input6)
        formLayout.addRow(self.input7)
        formLayout.addRow(self.input8)
        formLayout.addRow(self.input9)
        formLayout.addRow(self.input10)
        formLayout.addRow(self.buttonSave)
        groupBox.setLayout(formLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)

        layout = QVBoxLayout(self)
        layout.addWidget(scroll)

    def saveResponse(self):
        if self.input1.text() != "" and self.input2.text() != "" and self.input3.text() != "" and self.input4.text() \
                != "" and self.input5.text() != "" and self.input6.text() != "" and self.input7.text() \
                != "" and self.input8.text() != "" and self.input9.text() != "":
            ConnectionDB.Connection().insertAnswer(self.input1.text(), self.input2.text(), self.input3.text(),
                                                   self.input4.text(), self.input5.text(), self.input6.text(),
                                                   self.input7.text(), self.input8.text(), self.input9.text(),
                                                   self.input10.text(), self.idForm, 3)
            QMessageBox.information(self, "Succeful",
                                    "Se han ingresado las respuestas",
                                    QMessageBox.Ok, QMessageBox.Ok)
