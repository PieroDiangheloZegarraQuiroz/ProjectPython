import sys
from urllib import request

from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox, QLabel, QScrollArea, QVBoxLayout, QFormLayout, \
    QGroupBox, QDialog

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

        for i in range(10):
            self.vars = QLabel(f'<b>{i + 1}) {self.urls[i]}</b>', self)
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

    def openQuestions(self):
        pass


