import random
import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QMovie
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel, QPushButton, QDialog, QTextEdit, QLineEdit
from Models.Student import GraphicStef2


class Game2(QDialog):
    def __init__(self):
        super(Game2, self).__init__()
        self.initialize()

    def initialize(self):
        self.resize(500, 500)
        self.setStyleSheet("background-color: white;")
        self.setWindowTitle("Juego de jankenpón")
        self.display_widgets()
        window_palette = QPalette()
        self.setPalette(window_palette)

    def display_widgets(self):
        self.accountant = 5
        # # -------------------------------------------------------------------
        # Labels

        self.name = QLabel("Ingrese un \n número: ", self)
        self.name.move(160, 330)
        self.name.setFont(QFont("Comic Sans MS", 8))

        self.labelGif = QLabel(self)
        self.movie = QMovie('../../Images/Gif/pieda-papel-tijera.gif')
        self.labelGif.setMovie(self.movie)
        self.labelGif.move(40, -30)
        self.movie.start()

        self.name1 = QLabel("¿Piedra , papel o tijera?", self)
        self.name1.move(120, 170)
        self.name1.setFont(QFont("Segoe Print", 16, QFont.Bold))

        self.stone = QLabel("1. Piedra", self)
        self.stone.move(120, 220)
        self.stone.setFont(QFont("Segoe Print", 10, QFont.Bold))

        self.paper = QLabel("2. Papel", self)
        self.paper.move(220, 220)
        self.paper.setFont(QFont("Segoe Print", 10, QFont.Bold))

        self.scissor = QLabel("3. Tijera", self)
        self.scissor.move(320, 220)
        self.scissor.setFont(QFont("Segoe Print", 10, QFont.Bold))

        self.labelaccountant = QLabel(self)
        self.labelaccountant.setText(f'Le quedan 5 intentos')
        self.labelaccountant.setFont(QFont("Segoe Print", 10))
        self.labelaccountant.move(350, 11)
        # ----------------------------------------------------------------------

        # button
        self.button = QPushButton("Jugar", self)
        self.button.resize(100, 40)
        self.button.move(120, 260)
        self.button.clicked.connect(self.throw)
        self.button.setEnabled(False)
        self.button.clicked.connect(self.ActivateButton)
        self.button.setStyleSheet("border-radius: 10px;"
                                  "background-color: #0D18EC;")
        self.button.setFont(QFont("Segoe Print", 10, QFont.Bold))

        self.buttonR = QPushButton("Ver gráfica \n Estadística", self)
        self.buttonR.resize(100, 40)
        self.buttonR.move(280, 260)
        self.buttonR.setEnabled(False)
        self.buttonR.clicked.connect(self.show_Graph)
        self.buttonR.setStyleSheet("border-radius: 10px;"
                                   "background-color: #0D18EC;")
        self.buttonR.setFont(QFont("Segoe Print", 9, QFont.Bold))

        # QEdit
        self.text = QTextEdit(self)
        self.text.setStyleSheet("border-radius: 10px;"
                                "background-color: rgba(172, 209, 245, 0.5);")
        self.text.resize(300, 90)
        self.text.move(100, 370)
        self.text.setFont(QFont("Segoe Print", 8))

        self.number = QLineEdit(self)
        self.number.move(240, 330)
        self.number.resize(30, 25)
        self.number.textChanged.connect(self.ActivateButton)
        self.number.setFont(QFont("Comic Sans MS", 10, QFont.Bold))
        self.number.setStyleSheet("border-radius: 10px;"
                                  "background-color: rgba(172, 209, 245, 0.5);")
        self.number.setAlignment(QtCore.Qt.AlignCenter)

    def throw(self):
        self.numb = str(self.number.text())
        self.lis = []
        for i in range(1, 4):
            self.lis.append(i)
        self.list = self.lis
        self.num_rand = random.choice((self.lis))

        self.r = int(self.num_rand)
        self.s = int(self.numb)

        self.lis_j = ['Piedra', 'Papel', 'Tijera']

        if self.accountant > 0 and self.s <= 3:

            if self.r == self.s:
                self.accountant = 5
                self.number.clear()
                self.buttonR.setEnabled(True)
                self.buttonR.setStyleSheet("border-radius: 10px;"
                                           "background-color: #0D18EC;"
                                           "color: white;")
                self.text.setText(
                    str(f'Lista de opciones: {self.lis_j} '
                        f'\n Número Random: {self.num_rand} \n Número ingresado: {self.numb} '
                        f'\n         ¡ Felicitaciones número encontrado !'))
                self.labelaccountant.setText(f"Le quedan <b>{self.accountant}</b> intentos")

            elif self.r > self.s:
                self.accountant = self.accountant - 1
                self.number.clear()
                self.text.setText(
                    str(f'Lista de opciones: {self.lis_j} '
                        f'\n Número Random: {self.num_rand} \n Número ingresado: {self.numb} '
                        f'\n    --------Número Equivocado-------'))
                self.labelaccountant.setText(f"Le quedan <b>{self.accountant}</b> intentos")
                self.buttonR.setEnabled(False)
                self.buttonR.setStyleSheet("border-radius: 10px;"
                                           "background-color: #0D18EC;")

            elif self.r < self.s:
                self.accountant = self.accountant - 1
                self.number.clear()
                self.text.setText(
                    str(f'Lista de opciones: {self.lis_j} '
                        f'\n Número Random: {self.num_rand} \n Número ingresado: {self.numb} '
                        f'\n    --------Número Equivocado-------'))
                self.labelaccountant.setText(f"Le quedan <b>{self.accountant}</b> intentos")
                self.buttonR.setEnabled(False)
                self.buttonR.setStyleSheet("border-radius: 10px;"
                                           "background-color: #0D18EC;")

            else:
                self.accountant = self.accountant - 1
                self.number.clear()
                self.text.setText(
                    str(f'Lista de opciones: {self.lis_j} '
                        f'\n Número Random: {self.num_rand} \n Número ingresado: {self.numb} '
                        f'\n   --------Número Equivocado-------'))
                self.labelaccountant.setText(f"Le quedan <b>{self.intentos}</b> intentos")
                self.buttonR.setEnabled(False)
                self.buttonR.setStyleSheet("border-radius: 10px;"
                                           "background-color: #0D18EC;")

        elif self.s > 3 and self.accountant > 0:
            self.text.setText('Número fuera del rango')
            self.accountant = self.accountant - 1
            self.number.clear()
            self.labelaccountant.setText(f"Le quedan <b>{self.accountant}</b> intentos")

        else:
            self.accountant = 5
            self.number.clear()
            self.text.setText(
                str(f"Lista de opciones: {self.lis_j} "
                    f"\n Número Random: {self.num_rand} \n Número ingresado: {self.numb} "
                    f'\n              ¡Usted ha perdido!     '))
            self.labelaccountant.setText(f"Le quedan <b>{self.accountant}</b> intentos")

    def ActivateButton(self):
        if self.number.text() != "":
            self.button.setEnabled(True)
            self.button.setStyleSheet("border-radius: 10px;"
                                      "background-color: #0D18EC;"
                                      "color: white;")
        else:
            self.button.setEnabled(False)
            self.button.setStyleSheet("border-radius: 10px;"
                                      "background-color: #0D18EC;")

    def show_Graph(self):
        grafic = GraphicStef2.Graphic2()
        grafic.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Game2()
    window.show()
    sys.exit(app.exec_())
