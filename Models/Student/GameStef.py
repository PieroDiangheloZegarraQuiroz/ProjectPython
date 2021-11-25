import random
import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QMovie
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel, QPushButton, QDialog, QTextEdit, QLineEdit
from Models.Student import GraphicStef


class Game(QDialog):
    def __init__(self):
        super(Game, self).__init__()
        self.initialize()

    def initialize(self):
        self.resize(500, 500)
        self.setStyleSheet("background-color: white;")
        self.setWindowTitle("Juego del dado")
        self.display_widgets()
        window_palette = QPalette()
        self.setPalette(window_palette)

    def display_widgets(self):
        self.accountant = 5
        # # -------------------------------------------------------------------
        #Labels
        self.name = QLabel("Ingrese un \n número: ", self)
        self.name.move(160, 270)
        self.name.setFont(QFont("Comic Sans MS", 8))

        self.labelGif = QLabel(self)
        self.movie = QMovie('../../Images/Gif/dadonew.gif')
        self.labelGif.setMovie(self.movie)
        self.labelGif.move(170, 20)
        self.movie.start()

        self.labelaccountant = QLabel(self)
        self.labelaccountant.setText(f'Le quedan 5 intentos')
        self.labelaccountant.setFont(QFont("Segoe Print", 10))
        self.labelaccountant.move(350, 11)
        # ----------------------------------------------------------------------

        # button
        self.button = QPushButton("Lanzar Dado", self)
        self.button.resize(100, 40)
        self.button.move(120, 200)
        self.button.clicked.connect(self.throw)
        self.button.setEnabled(False)
        self.button.clicked.connect(self.ActivateButton)
        self.button.setStyleSheet("border-radius: 10px;"
                                  "background-color: #EC0D41;")
        self.button.setFont(QFont("Segoe Print", 9, QFont.Bold))

        self.buttonR = QPushButton("Ver gráfica \n Estadística", self)
        self.buttonR.resize(100, 40)
        self.buttonR.move(280, 200)
        self.buttonR.setEnabled(False)
        self.buttonR.clicked.connect(self.show_Graph)
        self.buttonR.setStyleSheet("border-radius: 10px;"
                                   "background-color: #EC0D41;")
        self.buttonR.setFont(QFont("Segoe Print", 10, QFont.Bold))


        #QEdit
        self.text = QTextEdit(self)
        self.text.setStyleSheet("border-radius: 10px;"
                                "background-color: rgba(255, 225, 255, 0.5);")
        self.text.resize(300, 90)
        self.text.move(100, 350)
        self.text.setFont(QFont("Segoe Print", 8))

        self.number = QLineEdit(self)
        self.number.move(240, 270)
        self.number.resize(30, 25)
        self.number.textChanged.connect(self.ActivateButton)
        self.number.setFont(QFont("Comic Sans MS", 10, QFont.Bold))
        self.number.setStyleSheet("border-radius: 10px;"
                                  "background-color: rgba(255, 225, 255, 0.5);")
        self.number.setAlignment(QtCore.Qt.AlignCenter)



    def throw(self):
        self.numb = str(self.number.text())
        self.lis = []
        for i in range(1, 7):
            self.lis.append(i)
        self.list = self.lis
        self.num_rand = random.choice((self.lis))

        self.r = int(self.num_rand)
        self.s = int(self.numb)

        if self.accountant > 0 and self.s <= 6:

            if self.r == self.s:
                self.accountant = 5
                self.number.clear()
                self.buttonR.setEnabled(True)
                self.buttonR.setStyleSheet("border-radius: 10px;"
                                          "background-color: #EC0D41;"
                                          "color: white;")
                self.text.setText(
                    str(f'Lista de números: {self.list} '
                        f'\n Número Random: {self.num_rand} \n Número ingresado: {self.numb} '
                        f'\n         ¡ Felicitaciones número encontrado !'))
                self.labelaccountant.setText(f"Le quedan <b>{self.accountant}</b> intentos")

            elif self.r > self.s:
                self.accountant = self.accountant - 1
                self.number.clear()
                self.text.setText(
                    str(f'Lista de números: {self.list} '
                        f'\n Número Random: {self.num_rand} \n Número ingresado: {self.numb} '
                        f'\n    --------Número Equivocado-------'))
                self.labelaccountant.setText(f"Le quedan <b>{self.accountant}</b> intentos")
                self.buttonR.setEnabled(False)
                self.buttonR.setStyleSheet("border-radius: 10px;"
                                          "background-color: #EC0D41;")

            elif self.r < self.s:
                self.accountant = self.accountant - 1
                self.number.clear()
                self.text.setText(
                    str(f'Lista de números: {self.list} '
                        f'\n Número Random: {self.num_rand} \n Número ingresado: {self.numb} '
                        f'\n    --------Número Equivocado-------'))
                self.labelaccountant.setText(f"Le quedan <b>{self.accountant}</b> intentos")
                self.buttonR.setEnabled(False)
                self.buttonR.setStyleSheet("border-radius: 10px;"
                                          "background-color: #EC0D41;")

            else:
                self.accountant = self.accountant - 1
                self.number.clear()
                self.text.setText(
                    str(f'Lista de números: {self.list} '
                        f'\n Número Random: {self.num_rand} \n Número ingresado: {self.numb} '
                        f'\n   --------Número Equivocado-------'))
                self.labelaccountant.setText(f"Le quedan <b>{self.intentos}</b> intentos")
                self.buttonR.setEnabled(False)
                self.buttonR.setStyleSheet("border-radius: 10px;"
                                          "background-color: #EC0D41;")

        elif self.s > 6 and self.accountant > 0:
            self.text.setText('Número fuera del rango')
            self.accountant = self.accountant - 1
            self.number.clear()
            self.labelaccountant.setText(f"Le quedan <b>{self.accountant}</b> intentos")

        else:
            self.accountant = 5
            self.number.clear()
            self.text.setText(
                str(f"Lista de números: {self.list} "
                    f"\n Número Random: {self.num_rand} \n Número ingresado: {self.numb} "
                    f'\n              ¡Usted ha perdido!     '))
            self.labelaccountant.setText(f"Le quedan <b>{self.accountant}</b> intentos")

    def ActivateButton(self):
        if self.number.text() != "":
            self.button.setEnabled(True)
            self.button.setStyleSheet("border-radius: 10px;"
                                      "background-color: #EC0D41;"
                                      "color: white;")
        else:
            self.button.setEnabled(False)
            self.button.setStyleSheet("border-radius: 10px;"
                                      "background-color: #EC0D41;")

    def show_Graph(self):
        grafic = GraphicStef.Graphic1()
        grafic.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Game()
    window.show()
    sys.exit(app.exec_())
