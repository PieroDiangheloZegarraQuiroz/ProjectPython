import random
import sys
import matplotlib.pyplot as plt
import numpy as np
from Models.Student import GraphicGameYactayo
from PyQt5 import QtTest
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QMovie
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QMessageBox, QLabel, QDialog, QWidget


class GameOne(QDialog):
    def __init__(self):
        super(GameOne, self).__init__()
        self.initialize()

    def initialize(self):
        self.resize(500, 500)
        self.setStyleSheet("background-color: white;")
        self.setWindowTitle("Game 1")
        self.display_widgets()

    def display_widgets(self):
        # Data
        self.step = 20
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_func)

        self.contador = 5
        self.intentos = 1
        self.numRan = random.randint(1, 10)

        # Gif
        self.labelGif = QLabel(self)
        self.movie = QMovie('../../Images/Gif/num.gif')
        self.labelGif.setMovie(self.movie)
        self.labelGif.move(150, 100)
        self.movie.start()

        # Labels
        self.label1 = QLabel(f'Adivina el número', self)
        self.label1.setFont(QFont("Comic Sans MS", 18, QFont.Bold))
        self.label1.move(140, 50)

        self.labelTime = QLabel('0', self)
        self.labelTime.setFont(QFont("Comic Sans MS", 12))
        self.labelTime.move(30, 10)
        self.labelTime.resize(40, 20)

        self.labelLess = QLabel(f'<b>Pista:</b> Número menor', self)
        self.labelLess.setFont(QFont("Comic Sans MS", 10))
        self.labelLess.move(130, 320)
        self.labelLess.hide()

        self.labelGreater = QLabel(f'<b>Pista:</b> Número mayor', self)
        self.labelGreater.setFont(QFont("Comic Sans MS", 10))
        self.labelGreater.move(130, 320)
        self.labelGreater.hide()

        self.labelContador = QLabel(self)
        self.labelContador.setText(f'Le quedan 5 intentos')
        self.labelContador.setFont(QFont("Comic Sans MS", 10))
        self.labelContador.move(360, 10)

        # Text Boxes
        self.numberBox = QLineEdit(self)
        self.numberBox.resize(50, 40)
        self.numberBox.move(225, 280)
        self.numberBox.setFont(QFont("Comic Sans MS", 8))
        self.numberBox.textChanged.connect(self.changedText)
        self.numberBox.setAlignment(Qt.AlignCenter)
        self.numberBox.setStyleSheet("background-color: rgba(0, 0, 0, 0);"
                                     "border: none;"
                                     "border-bottom: 2px solid rgba(46, 82, 101, 200);"
                                     "color: rgba(0, 0, 0, 240);"
                                     "padding-bottom: 5px;")

        # Button
        self.buttonCheck = QPushButton("Comprobar", self)
        self.buttonCheck.move(202, 360)
        self.buttonCheck.resize(100, 30)
        self.buttonCheck.setEnabled(False)
        self.buttonCheck.setFont(QFont("Comic Sans MS", 12))
        self.buttonCheck.clicked.connect(self.checkNumber)
        self.buttonCheck.clicked.connect(self.timeV)
        self.buttonCheck.setStyleSheet("border-radius: 5px;"
                                       "background-color: gray;"
                                       "color: white;")

    def changedText(self):
        if self.numberBox.text() != "":
            self.buttonCheck.setEnabled(True)
            self.buttonCheck.setStyleSheet("border-radius: 5px;"
                                           "background-color: rgb(232, 93, 97);"
                                           "color: white;")
        else:
            self.buttonCheck.setEnabled(False)
            self.buttonCheck.setStyleSheet("border-radius: 5px;"
                                           "background-color: gray;"
                                           "color: white;")

    def timeV(self):
        if not self.timer.isActive():
            self.timer.start(1000)

    def update_func(self):
        if self.step > 0:
            self.step -= 1
        elif self.step == 0:
            QMessageBox.information(self, "Lose", "Usted ha perdido.", QMessageBox.Ok, QMessageBox.Ok)
            self.numRan = random.randint(1, 10)
            self.contador = 5
            self.intentos = 1
            self.step = 20
            self.timer.stop()
            self.labelContador.setText(f"Le quedan <b>{self.contador}</b> intentos")
        self.labelTime.setText(str(self.step))

    def checkNumber(self):
        self.text_num = int(self.numberBox.text())
        self.text_ran = self.numRan

        if self.contador > 0 and self.text_num <= 10:
            if self.text_num == self.text_ran:
                rpt = QMessageBox.information(self, "Success",
                                              f"!Felicitaciones¡ adivinaste el número {self.text_ran} en "
                                              f"\n{self.intentos} intento(s)", QMessageBox.Yes | QMessageBox.No,
                                              QMessageBox.Yes)
                if rpt == QMessageBox.Yes:
                    graphic = GraphicGameYactayo.Graphic()
                    graphic.exec_()
                elif rpt == QMessageBox.No:
                    print("Reiniciando Juego o pasando")
                self.numRan = random.randint(0, 10)
                self.contador = 5
                self.intentos = 1
                self.step = 20
                self.numberBox.clear()
                self.labelContador.setText(f"Le quedan <b>{self.contador}</b> intentos")

            elif self.text_num > self.text_ran:
                self.labelLess.show()
                QtTest.QTest.qWait(1000)
                self.labelLess.hide()
                self.contador = self.contador - 1
                self.intentos = self.intentos + 1
                self.numberBox.clear()
                self.labelContador.setText(f"Le quedan <b>{self.contador}</b> intentos")

            elif self.text_num < self.text_ran:
                self.labelGreater.show()
                QtTest.QTest.qWait(1000)
                self.labelGreater.hide()
                self.contador = self.contador - 1
                self.intentos = self.intentos + 1
                self.numberBox.clear()
                self.labelContador.setText(f"Le quedan <b>{self.contador}</b> intentos")

        elif self.text_num > 10 and self.contador > 0:
            QMessageBox.warning(self, "Error", "Ha ingresado un numero fuera del rango", QMessageBox.Ok,
                                QMessageBox.Ok)
            self.contador = self.contador - 1
            self.intentos = self.intentos + 1
            self.numberBox.clear()
            self.labelContador.setText(f"Le quedan <b>{self.contador}</b> intentos")

        else:
            QMessageBox.information(self, "Lose", "Usted ha perdido.", QMessageBox.Ok, QMessageBox.Ok)
            self.numRan = random.randint(0, 10)
            self.contador = 5
            self.intentos = 1
            self.step = 20
            self.numberBox.clear()
            self.labelContador.setText(f"Le quedan <b>{self.contador}</b> intentos")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameOne()
    window.show()
    sys.exit(app.exec_())
