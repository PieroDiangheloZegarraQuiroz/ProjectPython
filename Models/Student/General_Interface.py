from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap, QPalette, QBrush
from PyQt5.QtWidgets import QLabel, QPushButton, QDialog, QMainWindow, QApplication, QMessageBox
from Connection import ConnectionDB
from Models.General import Login
from Models.Student import SaveFile


class General_Interface(QMainWindow):
    def __init__(self, idUser):
        super(General_Interface, self).__init__()
        self.idUser = str(idUser)
        self.initialize()

    def initialize(self):
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

        user_image = r"../../Images/Profile/perfil.png"
        try:
            with open(user_image):
                etiqueta_imagen = QLabel(self)
                pixmap = QPixmap(user_image)
                etiqueta_imagen.setPixmap(pixmap)
                etiqueta_imagen.move(100, 40)
                etiqueta_imagen.resize(180, 120)
        except FileNotFoundError:
            print("Nose encontro el archivo")

        results = ConnectionDB.Connection().getDataUserStudent(self.idUser)
        names = (results[1] + "\n" + results[2])
        self.user = QLabel(f'{names}', self)
        self.user.setAlignment(Qt.AlignCenter)
        self.user.setFont(QFont("Arial", 15))
        self.user.move(60, 180)
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

    def closeEvent(self, event):
        cuadro = QMessageBox.warning(self, "Cerrar", "¿Estas seguro de cerrar la ventana?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if cuadro == QMessageBox.Yes:
            print("Se ha cerrado la ventana")
            self.saveFile.hide()
            event.accept()
        elif cuadro == QMessageBox.No:
            event.ignore()
