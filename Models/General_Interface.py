import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QDialog, QMainWindow
from PyQt5.QtGui import QFont, QPixmap, QPalette, QBrush, QIcon
from PyQt5.QtCore import Qt
from Models import Login


class General_Interface(QDialog):
    def __init__(self):
        super(General_Interface, self).__init__()
        self.initialize()

    def initialize(self):
        self.setGeometry(350, 150, 800, 650)
        self.setWindowTitle("Registro Usuario")
        self.display_widgets()
        window_palette = QPalette()
        window_palette.setBrush(self.backgroundRole(), QBrush(QPixmap("Images/")))
        self.setPalette(window_palette)
        self.display_widgets()

    def display_widgets(self):
        # Labels
        self.lbl1 = QLabel(self)
        self.lbl1.setGeometry(550, 250, 500, 650)
        self.lbl1.move(300, 0)
        self.lbl1.setStyleSheet("border-radius: 0px;"
                                "background-color: red;"
                                "font-weight: bold; ")

        user_image = r"../Images/perfil.png"
        try:
            with open(user_image):
                etiqueta_imagen = QLabel(self)
                pixmap = QPixmap(user_image)
                etiqueta_imagen.setPixmap(pixmap)
                etiqueta_imagen.move(100, 40)
                etiqueta_imagen.resize(180, 120)
        except FileNotFoundError:
            print("Nose encontro el archivo")

        self.user = QLabel("Password", self)
        self.user.setFont(QFont("Arial", 10))
        self.user.move(30, 200)
        self.user.setStyleSheet("color: white;")

        # Buttons
        self.btn_games = QPushButton("Juegos", self)
        self.btn_games.resize(200, 40)
        self.btn_games.move(50, 240)
        self.btn_games.clicked.connect(self.Action1)
        self.btn_games.setStyleSheet("border-radius: 10px;"
                                     "background-color: white;"
                                     "font-weight: bold; ")

        self.btn_homework = QPushButton("Tarea", self)
        self.btn_homework.resize(200, 40)
        self.btn_homework.move(50, 300)
        self.btn_homework.clicked.connect(self.Action2)
        self.btn_homework.setStyleSheet("border-radius: 10px;"
                                        "background-color: white;"
                                        "font-weight: bold; ")

        self.btn_read = QPushButton("Lecturas Recomendadas", self)
        self.btn_read.resize(200, 40)
        self.btn_read.move(50, 360)
        self.btn_read.clicked.connect(self.Action3)
        self.btn_read.setStyleSheet("border-radius: 10px;"
                                    "background-color: white;"
                                    "font-weight: bold; ")

        self.btn_closesession = QPushButton("Cerrar Sesión", self)
        self.btn_closesession.resize(200, 40)
        self.btn_closesession.move(50, 420)
        self.btn_closesession.clicked.connect(self.sessionClose)
        self.btn_closesession.setStyleSheet("border-radius: 10px;"
                                            "background-color: white;"
                                            "font-weight: bold; ")

    def Action1(self):

        print("Se ha cerrado la ventana")

    def Action2(self):

        print("Se ha cerrado la ventana")

    def Action3(self):

        print("Se ha cerrado la ventana")

    def sessionClose(self):
        General_Interface.close(self)
        Login.Login().exec_()