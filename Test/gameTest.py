import random
import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QMessageBox, QLabel, QDialog


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
        self.contador = int(5)
        self.intentos = int(1)
        self.numRan = random.randint(0, 10)
        self.label1 = QLabel(f'Adivina el número', self)
        self.label1.setFont(QFont("Comic Sans MS", 18, QFont.Bold))
        self.label1.move(140, 50)

        self.labelMenor = QLabel(f'Ingrese un número menor', self)
        self.labelMenor.setFont(QFont("Comic Sans MS", 12, QFont.Bold))
        self.labelMenor.move(130, 170)
        self.labelMenor.hide()

        self.labelMayor = QLabel(f'Ingrese un número mayor', self)
        self.labelMayor.setFont(QFont("Comic Sans MS", 12, QFont.Bold))
        self.labelMayor.move(130, 170)
        self.labelMayor.hide()

        self.labelContador = QLabel(self)
        self.labelContador.setText('Le quedan 5 intentos')
        self.labelContador.setFont(QFont("Comic Sans MS", 8))
        self.labelContador.move(360, 10)

        # Text Boxes
        self.numberBox = QLineEdit(self)
        self.numberBox.resize(300, 40)
        self.numberBox.move(90, 260)
        self.numberBox.setFont(QFont("Comic Sans MS", 8))
        self.numberBox.setPlaceholderText("Ingresa el número")
        self.numberBox.setStyleSheet("background-color: rgba(0, 0, 0, 0);"
                                     "border: none;"
                                     "border-bottom: 2px solid rgba(46, 82, 101, 200);"
                                     "color: rgba(0, 0, 0, 240);"
                                     "padding-bottom: 5px;")

        # Button
        self.buttonCheck = QPushButton("Comprobar", self)
        self.buttonCheck.move(190, 360)
        self.buttonCheck.resize(100, 30)
        self.buttonCheck.setEnabled(True)
        self.buttonCheck.setFont(QFont("Comic Sans MS", 12))
        self.buttonCheck.clicked.connect(self.checkNumber)
        self.buttonCheck.setStyleSheet("border-radius: 5px;"
                                       "background-color: blue;"
                                       "color: white;")

    def checkNumber(self):
        self.text_num = int(self.numberBox.text())
        self.text_ran = int(self.numRan)
        self.cantidad = len(self.numberBox.text())
        self.text_num2 = self.numberBox.text()
        print("asda:", self.cantidad)
        print("asda:", self.text_num2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UploadUrl()
    window.show()
    sys.exit(app.exec_())
