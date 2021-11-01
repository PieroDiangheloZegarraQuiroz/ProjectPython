import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap, QPalette, QBrush
from PyQt5.QtWidgets import QLabel, QPushButton, QDialog, QMainWindow, QApplication, QMessageBox
from Connection import ConnectionDB
from Models.General import Login
from Models.Teacher import AddUrl, AddForm, ViewDegree


class General_Interface_Teacher(QMainWindow):
    def __init__(self, idUser):
        super(General_Interface_Teacher, self).__init__()
        self.idUser = str(idUser)
        self.initialize()

    def initialize(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setGeometry(350, 150, 800, 650)
        self.setWindowTitle("General Interface Teacher")
        window_palette = QPalette()
        window_palette.setBrush(self.backgroundRole(), QBrush(QPixmap("Images/")))
        self.setPalette(window_palette)
        self.display_widgets()

    def display_widgets(self):

        # Data
        self.booleanViewStudents = False
        self.booleanUpTask = False
        self.booleanUpRead = False

        # Labels
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
        self.code = str(results[9])

        self.user = QLabel(f'{names}', self)
        self.user.setAlignment(Qt.AlignCenter)
        self.user.setFont(QFont("Arial", 12))
        self.user.move(60, 180)
        self.user.resize(150, 50)
        self.user.setStyleSheet("color: white;")

        # Imports
        self.addform = AddForm.Form(self.idUser)
        self.addurl = AddUrl.UploadUrl(self.idUser)
        self.orderStudent = ViewDegree.ViewStudents(self.code)

        # Buttons
        self.btn_students = QPushButton("Ver alumnos", self)
        self.btn_students.resize(200, 40)
        self.btn_students.move(50, 240)
        self.btn_students.clicked.connect(self.Action1)
        self.btn_students.setStyleSheet("border-radius: 10px;"
                                        "background-color: white;"
                                        "font-weight: bold; ")

        self.btn_homework = QPushButton("Subir Tarea", self)
        self.btn_homework.resize(200, 40)
        self.btn_homework.move(50, 300)
        self.btn_homework.clicked.connect(self.Action2)
        self.btn_homework.setStyleSheet("border-radius: 10px;"
                                        "background-color: white;"
                                        "font-weight: bold;")

        self.btn_read = QPushButton("Subir Lecturas", self)
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
        self.booleanViewStudents = True
        if self.booleanViewStudents:
            self.orderStudent.show()
            self.addform.hide()
            self.addurl.hide()
        self.booleanViewStudents = False

    def Action2(self):
        self.booleanUpTask = True
        if self.booleanUpTask:
            self.addform.show()
            self.addurl.hide()
            self.orderStudent.hide()
        self.booleanUpTask = False

    def Action3(self):
        self.booleanUpRead = True
        if self.booleanUpRead:
            self.addurl.show()
            self.addform.hide()
            self.orderStudent.hide()
        self.booleanUpRead = False

    def sessionClose(self):
        self.addform.close()
        self.addurl.close()
        self.orderStudent.close()
        General_Interface_Teacher.hide(self)
        self.logincito = Login.Login()
        self.logincito.show()

