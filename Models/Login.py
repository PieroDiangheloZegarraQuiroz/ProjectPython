from PyQt5.QtWidgets import QDialog, QApplication, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox, QWidget
from PyQt5.QtGui import QFont, QPixmap, QPalette, QBrush, QIcon
from PyQt5.QtCore import Qt
from Models import Student_Registration
from Models import Teacher_Registration
from Models import General_Interface

from Connection import ConnectionDB
import sys


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        self.initialize()

    def initialize(self):
        # self.setStyleSheet("background-color: white;")
        self.setGeometry(500, 250, 400, 500)
        self.setWindowTitle("Login")
        self.setMinimumSize(400, 500)
        self.setMaximumSize(400, 500)
        self.setWindowIcon(QIcon("../Images/fondo.jpg"))
        wallpaper = QPalette()
        wallpaper.setBrush(self.backgroundRole(), QBrush(QPixmap("../Images/fondo.jpg")))
        self.setPalette(wallpaper)
        self.display_widgets()

    def display_widgets(self):
        # Images
        user_png = r"../Images/perfil.png"
        try:
            with open(user_png):
                imageLogin = QLabel(self)
                pixmap = QPixmap(user_png)
                imageLogin.setPixmap(pixmap)
                imageLogin.move(150, 50)
                imageLogin.resize(100, 100)
        except FileNotFoundError:
            print("No se encontró la ruta")

        # Text Boxes
        self.emailBox = QLineEdit(self)
        self.emailBox.move(100, 180)
        self.emailBox.resize(200, 30)
        self.emailBox.setFont(QFont("Arial", 10, QFont.Bold))
        self.emailBox.setAlignment(Qt.AlignCenter)
        self.emailBox.setPlaceholderText("Email")
        self.emailBox.setStyleSheet("border-radius: 10px;"
                                    "color: white;"
                                    "background-color: rgba(255, 255, 255, 50);")

        self.passwordBox = QLineEdit(self)
        self.passwordBox.move(100, 230)
        self.passwordBox.resize(200, 30)
        self.passwordBox.setEchoMode(QLineEdit.Password)
        self.passwordBox.setFont(QFont("Arial", 10, QFont.Bold))
        self.passwordBox.setAlignment(Qt.AlignCenter)
        self.passwordBox.setPlaceholderText("Password")
        self.passwordBox.setStyleSheet("border-radius: 10px;"
                                       "color: white;"
                                       "background-color: rgba(255, 255, 255, 50);")

        # Buttons
        self.buttonLoggin = QPushButton("Ingresar", self)
        self.buttonLoggin.setFont(QFont("Arial", 8, QFont.Bold))
        self.buttonLoggin.move(130, 300)
        self.buttonLoggin.resize(150, 30)
        self.buttonLoggin.clicked.connect(self.data)
        self.buttonLoggin.setStyleSheet("border-radius: 10px;"
                                        "background-color: #4286F5;"
                                        "color: white")

        self.comboRegister = QComboBox(self)
        self.comboRegister.addItems(["Registrate", "Estudiante", "Profesor"])
        self.comboRegister.setFont(QFont("Arial", 8, QFont.Bold))
        self.comboRegister.move(130, 350)
        self.comboRegister.resize(150, 30)
        self.comboRegister.activated[str].connect(self.register)
        self.comboRegister.setStyleSheet("background-color: #4286F5;"
                                         "color: white")

    # Methods
    def data(self):
        text_email = self.emailBox.text()
        text_password = self.passwordBox.text()
        validate = ConnectionDB.Connection().validateUser(text_email, text_password)
        if validate == 0:
            dataUser = ConnectionDB.Connection().getDataUserStudent(text_email, text_password)
            QMessageBox.information(self, "Succeful", f"Bienvenido {dataUser}", QMessageBox.Ok, QMessageBox.Ok)
            Login.close(self)
            General_Interface.General_Interface().exec_()

        elif validate == 1:
            dataUser = ConnectionDB.Connection().getDataUserTeacher(text_email, text_password)
            QMessageBox.information(self, "Succeful", f"Bienvenido {dataUser}", QMessageBox.Ok, QMessageBox.Ok)
            Login.close(self)
            Teacher_Registration.User_Register().exec_()
        elif validate is None and len(text_email) != 0 or len(text_password) != 0:
            QMessageBox.warning(self, "Error", "Email o contraseña incorrectas", QMessageBox.Ok, QMessageBox.Ok)
        elif len(text_email) == 0 or len(text_password) == 0:
            QMessageBox.warning(self, "Error", "Campos vacios", QMessageBox.Ok, QMessageBox.Ok)

    def register(self):
        text_register = self.comboRegister.currentText()
        if text_register == "Estudiante":
            Login.close(self)
            Student_Registration.User_Register().exec_()
        elif text_register == "Profesor":
            Login.close(self)
            Teacher_Registration.User_Register().exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec_())
