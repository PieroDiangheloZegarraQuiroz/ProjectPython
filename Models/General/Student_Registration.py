import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import QFont, QPixmap, QPalette, QBrush
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QMessageBox, QDialog, QComboBox, QWidget, QApplication
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Connection import ConnectionDB


class QLabelClick(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()


class User_Register(QDialog):
    def __init__(self):
        super(User_Register, self).__init__()
        self.initialize()

    def initialize(self):
        self.setGeometry(500, 250, 500, 500)
        self.setWindowTitle("Student Registration")
        self.display_widgets()
        window_palette = QPalette()
        window_palette.setBrush(self.backgroundRole(), QBrush(QPixmap("../../Images/Others/Rfondo2.jpg")))
        self.setPalette(window_palette)
        self.display_widgets()

    def display_widgets(self):
        # Images
        Icon_Return = r"../../Images/Others/IconoReturn_1.png"
        try:
            with open(Icon_Return):
                Image = QLabelClick(self)
                pixmap = QPixmap(Icon_Return)
                Image.setPixmap(pixmap)
                Image.move(10, -20)
                Image.resize(180, 120)
        except FileNotFoundError:
            print("Nose encontro el archivo")

        Image.clicked.connect(self.login)

        user_image = r"../../Images/Others/IconoStudent2.png"
        try:
            with open(user_image):
                etiqueta_imagen = QLabel(self)
                pixmap = QPixmap(user_image)
                etiqueta_imagen.setPixmap(pixmap)
                etiqueta_imagen.move(200, 40)
                etiqueta_imagen.resize(200, 120)
        except FileNotFoundError:
            print("Nose encontro el archivo")

        # Labels
        self.name = QLabel("Nombres ", self)
        self.name.move(30, 180)
        self.name.setStyleSheet("color: white;")
        self.name.setFont(QFont("Arial", 10))

        self.lastname = QLabel("Apellidos", self)
        self.lastname.setFont(QFont("Arial", 10))
        self.lastname.move(30, 210)
        self.lastname.setStyleSheet("color: white;")

        self.age = QLabel("Edad", self)
        self.age.setFont(QFont("Arial", 10))
        self.age.move(30, 240)
        self.age.setStyleSheet("color: white;")

        self.level = QLabel("Grado ", self)
        self.level.setFont(QFont("Arial", 10))
        self.level.move(30, 270)
        self.level.setStyleSheet("color: white;")

        self.email = QLabel("Email", self)
        self.email.setFont(QFont("Arial", 10))
        self.email.move(30, 300)
        self.email.setStyleSheet("color: white;")

        self.password = QLabel("Password", self)
        self.password.setFont(QFont("Arial", 10))
        self.password.move(30, 330)
        self.password.setStyleSheet("color: white;")

        self.codel = QLabel("Código", self)
        self.codel.setFont(QFont("Arial", 10))
        self.codel.move(30, 360)
        self.codel.setStyleSheet("color: white;")

        # Text Boxes
        self.nameBox = QLineEdit(self)
        self.nameBox.setAlignment(Qt.AlignCenter)
        self.nameBox.move(150, 180)
        self.nameBox.resize(200, 25)
        self.nameBox.setStyleSheet("border-radius: 10px;"
                                   "background-color: rgba(255, 215, 210, 30);"
                                   "font-weight: bold; ")

        self.lastnameBox = QLineEdit(self)
        self.lastnameBox.setAlignment(Qt.AlignCenter)
        self.lastnameBox.move(150, 210)
        self.lastnameBox.resize(200, 25)
        self.lastnameBox.setStyleSheet("border-radius: 10px;"
                                       "background-color: rgba(255, 255, 255, 50);"
                                       "font-weight: bold; ")

        self.ageBox = QLineEdit(self)
        self.ageBox.setAlignment(Qt.AlignCenter)
        self.ageBox.move(150, 240)
        self.ageBox.resize(200, 25)
        self.ageBox.setStyleSheet("border-radius: 10px;"
                                  "background-color: rgba(255, 225, 255, 0.5);"
                                  "font-weight: bold; ")

        self.levelComboBox = QComboBox(self)
        self.levelComboBox.addItems(["Selecciona tu grado", "4toº Primaria", "5toº Primaria", "6toº Primaria"])
        self.levelComboBox.setFont(QFont("Arial", 8, QFont.Bold))
        self.levelComboBox.move(150, 270)
        self.levelComboBox.resize(200, 25)
        self.levelComboBox.setStyleSheet("background-color: #F4F6F6;"
                                         "color: black")

        self.emailBox = QLineEdit(self)
        self.emailBox.setAlignment(Qt.AlignCenter)
        self.emailBox.move(150, 300)
        self.emailBox.resize(200, 25)
        self.emailBox.setStyleSheet("border-radius: 10px;"
                                    "background-color: rgba(255, 225, 255, 0.5);"
                                    "font-weight: bold; ")

        self.passwordBox = QLineEdit(self)
        self.passwordBox.setAlignment(Qt.AlignCenter)
        self.passwordBox.setEchoMode(QLineEdit.Password)
        self.passwordBox.move(150, 330)
        self.passwordBox.resize(200, 25)
        self.passwordBox.setStyleSheet("border-radius: 10px;"
                                       "background-color: rgba(255, 225, 255, 0.5);"
                                       "font-weight: bold; ")

        self.codeBox = QLineEdit(self)
        self.codeBox.setAlignment(Qt.AlignCenter)
        self.codeBox.move(150, 360)
        self.codeBox.resize(200, 25)
        self.codeBox.setStyleSheet("border-radius: 10px;"
                                   "background-color: rgba(255, 225, 255, 0.5);"
                                   "font-weight: bold; ")

        # Buttons
        self.buttonRegister = QPushButton("Create Account", self)
        self.buttonRegister.resize(200, 40)
        self.buttonRegister.move(150, 390)
        self.buttonRegister.clicked.connect(self.registro)
        self.buttonRegister.setStyleSheet("border-radius: 10px;"
                                          "background-color: #38EB47;")

    # Methods
    def registro(self):
        text_name = self.nameBox.text()
        text_lastname = self.lastnameBox.text()
        text_age = self.ageBox.text()
        text_grade = self.levelComboBox.currentText()
        text_email = self.emailBox.text()
        text_password = self.passwordBox.text()
        text_perfil = 'perfil.png'
        text_code = self.codeBox.text()
        ConnectionDB.Connection().insertUser(text_email, text_password, text_perfil, text_code, 0)
        lastId = ConnectionDB.Connection().getLastIdUser()
        ConnectionDB.Connection().insertUser_Student(text_name, text_lastname, text_age, text_grade, lastId)
        QMessageBox.information(self, "Succeful", "Registro exitoso", QMessageBox.Ok, QMessageBox.Ok)
        self.sendEmail()
        QMessageBox.information(self, "Aviso", "Se le ha enviado un correo", QMessageBox.Ok, QMessageBox.Ok)
        self.close()

    def sendEmail(self):
        email = 'sebastianaronyactayo@gmail.com'  # input("Ingrese su correo: ")
        password = 'Aron2001.'  # input("Ingrese su password: ")
        destination = self.emailBox.text()  # input("Ingrese el destination: ")
        subject = 'Registro exitoso'  # input("Ingrese el subject: ")

        mensaje = MIMEMultipart("alternativa")
        mensaje["Subject"] = subject
        mensaje["From"] = email
        mensaje["To"] = destination

        html = f"""
        <html>
        <body>
        <h1>Hola {self.nameBox.text()}</h1>
        <p>Tu correo es: {destination}</p>
        <p>Tu contraseña es: {self.passwordBox.text()}</p>
        </body>
        </html>
        """

        parte_html = MIMEText(html, "html")
        mensaje.attach(parte_html)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(email, password)
            server.sendmail(email, destination, mensaje.as_string())

    def login(self):
        self.close()
