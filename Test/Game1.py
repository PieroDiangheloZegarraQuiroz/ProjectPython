import random
import sys

from PyQt5 import QtCore, QtTest
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QMessageBox, QLabel, QDialog
from PyQt5.QtCore import Qt


class UploadUrl(QDialog):
    def __init__(self):
        super(UploadUrl, self).__init__()
        self.initialize()

    def initialize(self):
        self.resize(500, 500)
        self.setStyleSheet("background-color: white;")
        self.setWindowTitle("Subir Url")
        self.display_widgets()

    def display_widgets(self):
        self.contador = 5
        self.intentos = 1
        self.numRan = random.randint(0, 10)
        print(self.numRan)
        self.label1 = QLabel(f'Adivina el número', self)
        self.label1.setFont(QFont("Comic Sans MS", 18, QFont.Bold))
        self.label1.move(140, 50)

        self.labelMenor = QLabel(f'Pista: Número menor', self)
        self.labelMenor.setFont(QFont("Comic Sans MS", 12, QFont.Bold))
        self.labelMenor.move(130, 170)
        self.labelMenor.hide()

        self.labelMayor = QLabel(f'Pista: Número mayor', self)
        self.labelMayor.setFont(QFont("Comic Sans MS", 12, QFont.Bold))
        self.labelMayor.move(130, 170)
        self.labelMayor.hide()

        self.labelContador = QLabel(self)
        self.labelContador.setText('Le quedan 5 intentos')
        self.labelContador.setFont(QFont("Comic Sans MS", 8))
        self.labelContador.move(360, 10)

        # Text Boxes
        self.numberBox = QLineEdit(self)
        self.numberBox.resize(50, 40)
        self.numberBox.move(210, 260)
        self.numberBox.setFont(QFont("Comic Sans MS", 8))
        self.numberBox.setPlaceholderText("#")
        self.numberBox.textChanged.connect(self.changedText)
        self.numberBox.setAlignment(Qt.AlignCenter)
        self.numberBox.setStyleSheet("background-color: rgba(0, 0, 0, 0);"
                                     "border: none;"
                                     "border-bottom: 2px solid rgba(46, 82, 101, 200);"
                                     "color: rgba(0, 0, 0, 240);"
                                     "padding-bottom: 5px;")

        # Button
        self.buttonCheck = QPushButton("Comprobar", self)
        self.buttonCheck.move(190, 360)
        self.buttonCheck.resize(100, 30)
        self.buttonCheck.setEnabled(False)
        self.buttonCheck.setFont(QFont("Comic Sans MS", 12))
        self.buttonCheck.clicked.connect(self.checkNumber)
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

    def checkNumber(self):
        self.text_num = int(self.numberBox.text())
        self.text_ran = int(self.numRan)
        self.cantidad = len(self.numberBox.text())

        if self.cantidad == 1:
            if self.text_num == self.text_ran and self.contador > 0:
                QMessageBox.information(self, "Success",
                                        f"!Felicitaciones¡ adivinaste el número {self.text_ran} en \n{self.intentos} intentos",
                                        QMessageBox.Ok, QMessageBox.Ok)
                self.numRan = random.randint(0, 10)
                print(self.numRan)
                self.contador = 5
                self.intentos = 0
                self.numberBox.clear()

            elif self.text_num > self.text_ran and self.contador > 0:
                self.labelMenor.show()
                QtTest.QTest.qWait(2000)
                self.labelMenor.hide()
                self.labelMayor.hide()
                self.contador = self.contador - 1
                self.intentos = self.intentos + 1
                self.numberBox.clear()
                self.labelContador.setText(f"Le quedan {self.contador} intentos")

            elif self.text_num < self.text_ran and self.contador > 0:
                self.labelMenor.hide()
                self.labelMayor.show()
                QtTest.QTest.qWait(2000)
                self.labelMayor.hide()
                self.contador = self.contador - 1
                self.intentos = self.intentos + 1
                self.numberBox.clear()
                self.labelContador.setText(f"Le quedan {self.contador} intentos")

            elif self.contador == 0:
                QMessageBox.warning(self, "Lose",
                                    f"Usted ha perdido, vuelva a intentarlo",
                                    QMessageBox.Ok, QMessageBox.Ok)
                self.numRan = random.randint(0, 10)
                print(self.numRan)
                self.contador = 5
                self.intentos = 0
                self.labelMenor.hide()

                self.labelMayor.hide()
                self.numberBox.clear()
                self.labelContador.setText(f"Le quedan {self.contador} intentos")

        elif self.cantidad > 1:
            QMessageBox.warning(self, "Error",
                                f"Ha ingresado un numero fuera del rango",
                                QMessageBox.Ok, QMessageBox.Ok)
            self.contador = self.contador - 1
            self.intentos = self.intentos + 1
            self.numberBox.clear()
            self.labelContador.setText(f"Le quedan {self.contador} intentos")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UploadUrl()
    window.show()
    sys.exit(app.exec_())
