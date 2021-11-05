import time

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap, QPalette, QBrush, QWindow, QImage
from PyQt5.QtWidgets import QLabel, QPushButton, QMainWindow, QMessageBox

from Connection import ConnectionDB
from Models.General import Login
from Models.Student import SaveFile
from Models.General import Profile


class General_Interface(QMainWindow):
    def __init__(self, idUser):
        super(General_Interface, self).__init__()
        self.idUser = str(idUser)

        self.initialize()

    def initialize(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setGeometry(350, 150, 800, 650)
        self.setWindowTitle("General Interface Student")
        window_palette = QPalette()
        window_palette.setBrush(self.backgroundRole(), QBrush(QPixmap("Images/")))
        self.setPalette(window_palette)
        self.display_widgets()

    def display_widgets(self):
        # Imports
        self.saveFile = SaveFile.Download()

        # Labels
        self.booleanJuegos = False
        self.lblJuegos = QLabel(self)
        self.lblJuegos.setGeometry(550, 250, 500, 650)
        self.lblJuegos.move(300, 0)
        self.lblJuegos.show()

        self.booleanTarea = False
        self.lblTarea = QLabel(self)
        self.lblTarea.setGeometry(550, 250, 500, 650)
        self.lblTarea.move(300, 0)
        self.lblTarea.hide()

        self.booleanLectura = False
        self.lblLecutra = QLabel(self)
        self.lblLecutra.setGeometry(550, 250, 500, 650)
        self.lblLecutra.move(300, 0)
        self.lblLecutra.hide()

        self.results = ConnectionDB.Connection().getDataUserStudent(self.idUser)
        self.perfil = str(self.results[9])
        self.names = (self.results[1] + "\n" + self.results[2])
        self.user_image = f"../../Images/Profile/{self.perfil}"
        try:
            with open(self.user_image):
                self.etiqueta_imagen = QLabel(self)
                # self.pixmap = QPixmap(self.user_image)
                # self.etiqueta_imagen.setPixmap(self.pixmap)
                self.etiqueta_imagen.move(60, 40)
                self.etiqueta_imagen.resize(180, 120)
                self.etiqueta_imagen.setStyleSheet(f" \
                                                   border-image: url('{self.user_image}'); \
                                                   background-color: black; \
                                                   border-radius: 50%; \
                                                   ")
                self.etiqueta_imagen.setMargin(20)
                self.etiqueta_imagen.setScaledContents(True)
                self.etiqueta_imagen.show()

        except FileNotFoundError:
            print("Nose encontro el archivo")

        self.user = QLabel(f'{self.names}', self)
        self.user.setAlignment(Qt.AlignCenter)
        self.user.setFont(QFont("Arial", 12))
        self.user.move(60, 180)
        self.user.resize(150, 50)
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
                                        "font-weight: bold;")

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
        self.btn_cProfile = QPushButton("+", self)
        self.btn_cProfile.setFont(QFont("Arial", 14))
        self.btn_cProfile.setGeometry(190, 10, 25, 25)
        self.btn_cProfile.clicked.connect(self.enviarAbrir)
        self.btn_cProfile.setStyleSheet("border: 1px solid gray;"
                                        "border-radius: 10px;"
                                        "background-color : gray;"
                                        "color : white;")

    def enviarAbrir(self):
        Profile.selectProfile(self.idUser).exec_()
        General_Interface.display_widgets(self)

    def Action1(self):
        self.booleanJuegos = True
        if self.booleanJuegos:
            self.lblJuegos.show()
            self.lblLecutra.hide()
            self.lblTarea.hide()
        self.booleanJuegos = False
        print("boton juego")

    def Action2(self):
        self.booleanTarea = True
        if self.booleanTarea:
            self.lblJuegos.hide()
            self.lblLecutra.hide()
            self.lblTarea.show()
            self.saveFile.hide()
        self.booleanTarea = False
        print("boton tarea")

    def Action3(self):
        self.booleanLectura = True
        if self.booleanLectura:
            self.lblJuegos.hide()
            self.lblLecutra.show()
            self.lblTarea.hide()
            self.saveFile.show()
        self.booleanLectura = False

        print("boton lectura")

    def sessionClose(self):
        self.saveFile.hide()
        General_Interface.hide(self)
        self.logincito = Login.Login()
        self.logincito.showNormal()

    # def closeEvent(self, event):
    #     cuadro = QMessageBox.warning(self, "Cerrar", "¿Estas seguro de cerrar la ventana?",
    #                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    #
    #     if cuadro == QMessageBox.Yes:
    #         print("Se ha cerrado la ventana")
    #         self.saveFile.hide()
    #         event.accept()
    #     elif cuadro == QMessageBox.No:
    #         event.ignore()
