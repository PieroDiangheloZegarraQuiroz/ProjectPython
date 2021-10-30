import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap, QPalette, QBrush
from PyQt5.QtWidgets import QLabel, QPushButton, QDialog, QMainWindow, QApplication
from Connection import ConnectionDB
from Models.General import Login
from Models.Teacher import AddUrl, AddForm, LevelStudent


class General_Interface_Teacher(QMainWindow):
    def __init__(self, idUser):
        super(General_Interface_Teacher, self).__init__()
        self.idUser = str(idUser)
        self.initialize()

    def initialize(self):
        self.setGeometry(350, 150, 800, 650)
        self.setWindowTitle("Interface Teacher")
        window_palette = QPalette()
        window_palette.setBrush(self.backgroundRole(), QBrush(QPixmap("Images/")))
        self.setPalette(window_palette)
        self.display_widgets()

    def display_widgets(self):
        # Imports

        self.addurl = AddUrl.UploadUrl()
        self.addform = AddForm.Form()
        self.lvlstudent = LevelStudent.LvlStudent()

        # Labels
        self.booleanJuegos = False
        self.lblJuegos = QLabel(self)
        self.lblJuegos.setGeometry(550, 250, 500, 650)
        self.lblJuegos.move(300, 0)
        self.lblJuegos.show()

        self.booleanTarea = False
        self.booleanLectura = False

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

        results = ConnectionDB.Connection().getDataUserTeacher(self.idUser)
        names = (results[1] + "\n" + results[2])
        self.user = QLabel(f'{names}', self)
        self.user.setAlignment(Qt.AlignCenter)
        self.user.setFont(QFont("Arial", 14))
        self.user.move(60, 180)
        self.user.resize(150, 50)
        self.user.setStyleSheet("color: white;")

        # Buttons
        self.btn_students = QPushButton("Juegos", self)
        self.btn_students.resize(200, 40)
        self.btn_students.move(50, 240)
        self.btn_students.clicked.connect(self.Action1)
        self.btn_students.setStyleSheet("border-radius: 10px;"
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
            self.addform.hide()
            self.addurl.hide()
            self.lvlstudent.show()
        self.booleanJuegos = False
        print("boton juego")

    def Action2(self):
        self.booleanTarea = True
        if self.booleanTarea:
            self.lblJuegos.hide()
            self.addform.show()
            self.addurl.hide()
            self.lvlstudent.hide()
        self.booleanTarea = False
        print("boton tarea")

    def Action3(self):
        self.booleanLectura = True
        if self.booleanLectura:
            self.lblJuegos.hide()
            self.addurl.show()
            self.addform.hide()
            self.lvlstudent.hide()
        self.booleanLectura = False

        print("boton lectura")

    def sessionClose(self):
        self.addform.hide()
        self.addurl.hide()
        self.lvlstudent.hide()
        General_Interface_Teacher.hide(self)
        self.logincito = Login.Login()
        self.logincito.showNormal()
