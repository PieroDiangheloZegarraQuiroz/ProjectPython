import random
import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QMovie, QPixmap
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QComboBox
from PyQt5.QtWidgets import QLabel, QPushButton, QDialog, QTextEdit, QLineEdit
from Models.Student import GraphicSoocer

class SoocerGame(QDialog):
    def __init__(self):
        super(SoocerGame, self).__init__()
        self.initialize()

    def initialize(self):
        self.resize(700, 600)
        self.setStyleSheet("background-color: white;")
        self.setWindowTitle("Soocer")
        self.display_widgets()
        window_palette = QPalette()
        self.setPalette(window_palette)

    def display_widgets(self):
        self.accountant = 5
        # Title
        self.TitleTables = QLabel("Football Championship", self)
        self.TitleTables.move(225, 30)
        self.TitleTables.setFont(QFont("roboto", 17))
        self.TitleTables.setStyleSheet("border: 5px outset coral;")
        # Logo - left
        self.LogoLeft = QLabel(self)
        self.LogoLeft.setPixmap(
            QPixmap('../../Images/Others/LogoSoocer.jpg').scaled(170, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.LogoLeft.setGeometry(125, 30, 100, 50)
        # Logo - right
        self.LogoRight = QLabel(self)
        self.LogoRight.setPixmap(
            QPixmap("../../Images/Others/LogoSoocer.jpg").scaled(170, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.LogoRight.setGeometry(475, 30, 100, 50)
        # Title - Tables
        self.TitleTables = QLabel("Promedio de los equipos", self)
        self.TitleTables.move(265, 85)
        self.TitleTables.setFont(QFont("roboto", 13))
        self.TitleTables.setStyleSheet("text-decoration: underline;")

        # Tabla Equipos - Derrotas
        self.TableLosses = QLabel(self)
        self.TableLosses.setPixmap(QPixmap("../../Images/Others/TableLosses.PNG").scaled(200, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.TableLosses.setGeometry(90, 120, 169, 105)

        # Tabla Equipos - Empates
        self.TableDraw = QLabel(self)
        self.TableDraw.setPixmap(
            QPixmap("../../Images/Others/TableDraw.PNG").scaled(203, 103, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.TableDraw.setGeometry(275, 120, 169, 105)

        # Tabla Equipos - Victorias
        self.TableWins = QLabel(self)
        self.TableWins.setPixmap(QPixmap("../../Images/Others/TableWin.PNG").scaled(203, 103, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.TableWins.setGeometry(455, 120, 169, 105)

        # Gif
        self.labelGif = QLabel(self)
        self.movie = QMovie("../../Images/Gif/Gol.gif")
        self.labelGif.setMovie(self.movie)
        self.labelGif.move(125, 230)
        self.movie.start()

        # Instrucciones para jugar - Título
        self.InstructionsTittle = QLabel("Instrucciones del Juego:", self)
        self.InstructionsTittle.move(90, 335)
        self.InstructionsTittle.setFont(QFont("roboto", 10, QFont.Bold))
        # Instruccion 1
        self.Instruction1 = QLabel("1.- Analisa el promedio de los equipos", self)
        self.Instruction1.move(90, 355)
        self.Instruction1.setFont(QFont("roboto", 10))
        # Instruccion 2
        self.Instruction2 = QLabel("2.- Elige un equipo ganador del Campeonato", self)
        self.Instruction2.move(90, 375)
        self.Instruction2.setFont(QFont("roboto", 10))
        # Instruccion 3
        self.Instructions3 = QLabel("3.- Ingresa el número del equipo para averiguar el resultado", self)
        self.Instructions3.move(90, 395)
        self.Instructions3.setFont(QFont("roboto", 10))

        # Punto del juego
        self.Point = QLabel("Elige un equipo ganador del campeonato", self)
        self.Point.move(185, 425)
        self.Point.setFont(QFont("roboto", 12, QFont.Bold))
        self.Point.setStyleSheet("border: 1px black;"
                                 "border-color: gray blue;"
                                 "border-width: 3px;"
                                 "border-style: solid;"
                                 "border-radius: 10px;")

        # Número de intentos
        self.accountant = 5
        self.labelaccountant = QLabel(self)
        self.labelaccountant.setText(f'Le quedan 5 intentos')
        self.labelaccountant.setFont(QFont("roboto", 10))
        self.labelaccountant.move(70, 468)


        # Insertar el equipo (número)
        self.lbl_InsertTeam = QLabel("Ingrese el número de un Equipo: ", self)
        self.lbl_InsertTeam.move(70, 495)
        self.lbl_InsertTeam.setFont(QFont("roboto", 10))
        # QEdit
        # Número de equipo
        self.number = QLineEdit(self)
        self.number.setGeometry(255, 493, 30, 25)
        self.number.textChanged.connect(self.ActivateButton)
        self.number.setFont(QFont("roboto", 10, QFont.Bold))
        self.number.setStyleSheet("border-radius: 10px;"
                                  "background-color: rgba(201, 84, 84, 0.16);")
        self.number.setAlignment(QtCore.Qt.AlignCenter)

        # Muestra de Resultados
        self.text = QTextEdit(self)
        self.text.setStyleSheet("border-radius: 10px;"
                                "background-color: rgba(201, 84, 84, 0.16);")
        self.text.setGeometry(296, 475, 380, 80)
        self.text.setFont(QFont("roboto", 8))

        # Buttons
        self.button = QPushButton("Jugar", self)
        self.button.setGeometry(77, 530, 80, 30)
        self.button.clicked.connect(self.throw)
        self.button.setEnabled(False)
        self.button.clicked.connect(self.ActivateButton)
        self.button.setStyleSheet("color: white;"
                                  "border-radius: 10px;"
                                  "background: #C95454;")
        self.button.setFont(QFont("roboto", 10, QFont.Bold))

        #=====
        self.buttonR = QPushButton("Ver gráfico \n Estadístico", self)
        self.buttonR.setGeometry(167, 525, 100, 40)
        self.buttonR.setEnabled(False)
        self.buttonR.clicked.connect(self.show_Graph)
        self.buttonR.setStyleSheet("color: white;"
                                   "border-radius: 10px;"
                                   "background-color: #C95454;")
        self.buttonR.setFont(QFont("roboto", 9, QFont.Bold))

    def throw(self):
        self.numb = str(self.number.text())
        self.lis = []
        for i in range(1, 7):
            self.lis.append(i)
        self.list = self.lis
        self.num_rand = random.choice((self.lis))

        self.r = int(self.num_rand)
        self.s = int(self.numb)
        self.lis_j = ['Equipo 1', 'Equipo 2', 'Equipo 3', 'Equipo 4', 'Equipo 5', 'Equipo 6']

        if self.accountant > 0 and self.s <= 6:

            if self.r == self.s:
                self.accountant = 5
                self.number.clear()
                self.buttonR.setEnabled(True)
                self.buttonR.setStyleSheet("color: black;"
                                            "border-radius: 10px;"
                                           "background-color: #FAD474;")
                self.text.setText(
                    str(f'Lista de Equipos: {self.lis_j} '
                        f'\n Equipo Ganador -> Equipo{self.num_rand} \n Equipo ingresado -> Equipo {self.numb} '
                        f'\n      ¡ Felicitaciones tu Equipo {self.numb} es el ganador !'))
                self.labelaccountant.setText(f"Le quedan <b>{self.accountant}</b> intentos")

            elif self.r > self.s:
                self.accountant = self.accountant - 1
                self.number.clear()
                self.text.setText(
                    str(f'Lista de Equipos: {self.lis_j} '
                        f'\n Equipo Ganador -> Equipo {self.num_rand} \n Equipo ingresado -> Equipo {self.numb} '
                        f'\n  --------El Equipo {self.numb} no ganó el campeonato -------'))
                self.labelaccountant.setText(f"Le quedan <b>{self.accountant}</b> intentos")
                self.buttonR.setEnabled(False)
                self.buttonR.setStyleSheet("color: gray;"
                                           "border-radius: 10px;"
                                           "background-color: #FAD474;")

            elif self.r < self.s:
                self.accountant = self.accountant - 1
                self.number.clear()
                self.text.setText(
                    str(f'Lista de Equipos: {self.lis_j} '
                        f'\n Equipo Ganador -> Equipo {self.num_rand} \n Equipo ingresado -> Equipo {self.numb} '
                        f'\n  --------El Equipo {self.numb} no ganó el campeonato -------'))
                self.labelaccountant.setText(f"Le quedan <b>{self.accountant}</b> intentos")
                self.buttonR.setEnabled(False)
                self.buttonR.setStyleSheet("color: gray;"
                                           "border-radius: 10px;"
                                           "background-color: #FAD474;")

        elif self.s > 6 and self.accountant > 0:
            self.text.setText('Equipo fuera del rango')
            self.accountant = self.accountant - 1
            self.labelaccountant.setText(f"Le quedan <b>{self.accountant}</b> intentos")


        else:
            self.accountant = 5
            self.number.clear()
            self.text.setText(
                str(f"Lista de Equipos: {self.lis_j} "
                    f"\n Equipo Ganador -> Equipo {self.num_rand} \n Equipo ingresado -> Equipo {self.numb} "
                    f'\n              ¡Usted ha perdido!     '))
            self.labelaccountant.setText(f"Le quedan <b>{self.accountant}</b> intentos")

    def ActivateButton(self):
        if self.number.text() != "":
            self.button.setEnabled(True)
            self.button.setStyleSheet("color: black;"
                                           "border-radius: 10px;"
                                           "background-color: #FAD474;")
        else:
            self.button.setEnabled(False)
            self.button.setStyleSheet("color: black;"
                                           "border-radius: 10px;"
                                           "background-color: #FAD474;")
    #
    def show_Graph(self):
        grafic = GraphicSoocer.Graphic1()
        grafic.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SoocerGame()
    window.show()
    sys.exit(app.exec_())