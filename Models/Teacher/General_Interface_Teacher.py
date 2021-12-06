from PyQt5.QtCore import *
from PyQt5.QtGui import QFont, QPixmap, QPalette, QBrush
from PyQt5.QtWidgets import QLabel, QPushButton, QDialog, QMainWindow, QApplication, QMessageBox
from Connection import ConnectionDB
from Models.General import Login
from Models.General import Profile
from Models.Teacher import AddUrl, AddForm, ViewDegree


class QLabelClick(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()


class General_Interface_Teacher(QMainWindow):
    def __init__(self, idUser):
        super(General_Interface_Teacher, self).__init__()
        self.idUser = str(idUser)
        self.initialize()

    def initialize(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setGeometry(350, 150, 800, 650)
        self.setWindowTitle("General Interface Teacher")
        # window_palette = QPalette()
        # window_palette.setBrush(self.backgroundRole(), QBrush(QPixmap("Images/")))
        # self.setPalette(window_palette)
        self.display_widgets()

    def display_widgets(self):

        # Data
        self.booleanViewStudents = False
        self.booleanUpTask = False
        self.booleanUpRead = False

        # Labels
        self.back = QLabelClick(self)
        self.back.resize(800, 650)
        self.back.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, "
                                "0, 0, 255), stop:1 rgba(255, 255, 255, 255));"
                                "border-radius: 60%;")
        self.back.clicked.connect(self.importadosClose)

        self.results = ConnectionDB.Connection().getDataUserTeacher(self.idUser)
        self.perfil = str(self.results[8])
        self.names = (self.results[1] + "\n" + self.results[2])
        self.code = str(self.results[9])
        self.user_image = f"../../Images/Profile/{self.perfil}"
        try:
            with open(self.user_image):
                self.etiqueta_imagen = QLabel(self)
                self.etiqueta_imagen.move(75, 40)
                self.etiqueta_imagen.resize(140, 140)
                self.etiqueta_imagen.setStyleSheet(f" \
                                                   border-image: url('{self.user_image}'); \
                                                   background-color: black; \
                                                   border-radius: 60%; \
                                                   ")
                self.etiqueta_imagen.setMargin(20)
                self.etiqueta_imagen.setScaledContents(True)
                self.etiqueta_imagen.show()
        except FileNotFoundError:
            print("Nose encontro el archivo")

        self.user = QLabel(f'{self.names}', self)
        self.user.setAlignment(Qt.AlignCenter)
        self.user.setFont(QFont("Arial", 12))
        self.user.move(70, 180)
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
        General_Interface_Teacher.display_widgets(self)

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

    def importadosClose(self):
        self.addurl.close()
        self.addform.close()
        self.orderStudent.close()


Stylesheet = """
    #Custom_Widget {
        border-radius: 20px;
        opacity: 100;
        border: 1px;                   
    }"""