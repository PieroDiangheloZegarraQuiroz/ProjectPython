import uuid

from PyQt5.QtCore import *
from PyQt5.QtGui import QFont, QPixmap, QPalette, QBrush
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QMessageBox, QDialog
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
        self.setWindowTitle("Teacher Registration")
        self.setMinimumSize(500, 500)
        self.setMaximumSize(500, 500)
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

        user_image = r"../../Images/Others/IconoTeacher.png"
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
        self.name.setFont(QFont("Arial", 10))
        self.name.setStyleSheet("color: white;")

        self.lastname = QLabel("Apellidos", self)
        self.lastname.setFont(QFont("Arial", 10))
        self.lastname.move(30, 210)
        self.lastname.setStyleSheet("color: white;")

        self.mobile = QLabel("Telefono", self)
        self.mobile.setFont(QFont("Arial", 10))
        self.mobile.move(30, 240)
        self.mobile.setStyleSheet("color: white;")

        self.email = QLabel("Email", self)
        self.email.setFont(QFont("Arial", 10))
        self.email.move(30, 270)
        self.email.setStyleSheet("color: white;")

        self.password = QLabel("Password", self)
        self.password.setFont(QFont("Arial", 10))
        self.password.move(30, 300)
        self.password.setStyleSheet("color: white;")

        self.codel = QLabel("Código", self)
        self.codel.setFont(QFont("Arial", 10))
        self.codel.move(30, 330)
        self.codel.setStyleSheet("color: white;")

        # Text Boxes
        self.nameBox = QLineEdit(self)
        self.nameBox.setAlignment(Qt.AlignCenter)
        self.nameBox.move(150, 180)
        self.nameBox.resize(200, 25)
        self.nameBox.textChanged.connect(self.buttonEnabled)
        self.nameBox.setStyleSheet("border-radius: 10px;"
                                   "background-color: rgba(255, 215, 210, 30);"
                                   "font-weight: bold; ")

        self.lastnameBox = QLineEdit(self)
        self.lastnameBox.setAlignment(Qt.AlignCenter)
        self.lastnameBox.move(150, 210)
        self.lastnameBox.resize(200, 25)
        self.lastnameBox.textChanged.connect(self.buttonEnabled)
        self.lastnameBox.setStyleSheet("border-radius: 10px;"
                                       "background-color: rgba(255, 255, 255, 50);"
                                       "font-weight: bold; ")

        self.mobileBox = QLineEdit(self)
        self.mobileBox.setAlignment(Qt.AlignCenter)
        self.mobileBox.move(150, 240)
        self.mobileBox.resize(200, 25)
        self.mobileBox.textChanged.connect(self.buttonEnabled)
        self.mobileBox.setStyleSheet("border-radius: 10px;"
                                     "background-color: rgba(255, 225, 255, 0.5);"
                                     "font-weight: bold; ")

        self.emailBox = QLineEdit(self)
        self.emailBox.setAlignment(Qt.AlignCenter)
        self.emailBox.move(150, 270)
        self.emailBox.resize(200, 25)
        self.emailBox.textChanged.connect(self.buttonEnabled)
        self.emailBox.setStyleSheet("border-radius: 10px;"
                                    "background-color: rgba(255, 225, 255, 0.5);"
                                    "font-weight: bold; ")

        self.passwordBox = QLineEdit(self)
        self.passwordBox.setAlignment(Qt.AlignCenter)
        self.passwordBox.setEchoMode(QLineEdit.Password)
        self.passwordBox.move(150, 300)
        self.passwordBox.resize(200, 25)
        self.passwordBox.textChanged.connect(self.buttonEnabled)
        self.passwordBox.setStyleSheet("border-radius: 10px;"
                                       "background-color: rgba(255, 225, 255, 0.5);"
                                       "font-weight: bold; ")

        self.codeBox = QLineEdit(self)
        self.codeBox.setAlignment(Qt.AlignCenter)
        self.codeBox.move(150, 330)
        self.codeBox.resize(200, 25)
        self.codeBox.setEnabled(False)
        self.codeBox.textChanged.connect(self.buttonEnabled)
        self.codeBox.setStyleSheet("border-radius: 10px;"
                                   "background-color: rgba(255, 225, 255, 0.5);"
                                   "font-weight: bold; ")

        # Buttons
        self.buttonRegister = QPushButton("Crear Cuenta", self)
        self.buttonRegister.resize(200, 40)
        self.buttonRegister.move(150, 390)
        self.buttonRegister.setEnabled(False)
        self.buttonRegister.clicked.connect(self.registro)
        self.buttonRegister.setStyleSheet("border-radius: 10px;"
                                          "background-color: gray;")

        self.buttonCode = QPushButton("Generar", self)
        self.buttonCode.resize(70, 25)
        self.buttonCode.move(360, 330)
        self.buttonCode.setFont(QFont('Comic Sans MS', 10))
        self.buttonCode.clicked.connect(self.code)
        self.buttonCode.setStyleSheet("border-radius: 10px;"
                                      "background-color: rgb(14, 150, 232);")

    def buttonEnabled(self):
        if self.nameBox.text() != "" and self.lastnameBox.text() != "" and self.mobileBox.text() != "" \
                and self.email.text() != "" and self.passwordBox.text() != "" and self.codeBox.text() != "":
            self.buttonRegister.setEnabled(True)
            self.buttonRegister.setStyleSheet("border-radius: 10px;"
                                              "background-color: #38EB47;")
        else:
            self.buttonRegister.setEnabled(False)
            self.buttonRegister.setStyleSheet("border-radius: 10px;"
                                              "background-color: gray;")

    # Methods
    def registro(self):
        text_name = self.nameBox.text()
        text_lastname = self.lastnameBox.text()
        text_cellphone = self.mobileBox.text()
        text_email = self.emailBox.text()
        text_password = self.passwordBox.text()
        text_perfil = 'perfil.png'
        text_code = self.codeBox.text()
        ConnectionDB.Connection().insertUser(text_email, text_password, text_perfil, text_code, 1)
        lastId = ConnectionDB.Connection().getLastIdUser()
        ConnectionDB.Connection().insertUser_Teacher(text_name, text_lastname, text_cellphone, lastId)
        QMessageBox.information(self, "Succeful", "Registro exitoso", QMessageBox.Ok, QMessageBox.Ok)
        self.sendEmail()
        QMessageBox.information(self, "Aviso", "Se le ha enviado un correo", QMessageBox.Ok, QMessageBox.Ok)
        self.close()

    def sendEmail(self):
        email = 'proyectPython2021@gmail.com'
        password = 'python2021'
        destination = self.emailBox.text()
        subject = 'Registro exitoso'

        mensaje = MIMEMultipart("alternativa")
        mensaje["Subject"] = subject
        mensaje["From"] = email
        mensaje["To"] = destination

        html = f"""

                        <html>
                            <head>
                            </head>
                        <body>

                            <div>
                                <center>   
                                    <h2>Hola   {self.nameBox.text()}</h2>
            
                                    <h4>Recuerda que para ingresar a la plataforma de aprendizaje .... tiene que ingresar sus datos: </h2>
                                    <h5>
                                    <form>
                                        Correo:
                                        <input type="email" name="email" required value="{destination}">
                
                                        <label>
                                        Contraseña:
                                        <input type="email" name="email" required value="{self.passwordBox.text()}">
                                        </h3>
                                        </label>
                
                                        <label>
                                        Código de profesor:
                                        <input type="code" name="code" required value="{self.codeBox.text()}">
                                        </h3>
                                        </label>
                
                                        <p>Que tenga un buen día</p>
                                        <br>
                                    </form>
                                    <h8> PD: Si no realizó esta acción, ignore este correo electrónico.
                                    <br>
                                    Tus amigos de Equipo Wisdom </h8>
                                </center>
                                  
                            </div>
                             <div>
                              <center><img src="https://i.ibb.co/pjHnYYg/Loguito.png"></center>
                           </div>
                        </body>
                        </html>
                        """

        parte_html = MIMEText(html, "html")
        mensaje.attach(parte_html)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(email, password)
            server.sendmail(email, destination, mensaje.as_string())

    def code(self):
        self.codeBox.setEnabled(True)
        u = uuid.uuid1()
        rs = str(u)
        rs2 = rs.replace('-', '')
        self.codeBox.setText(rs2[:12])
        self.codeBox.setEnabled(False)

    def login(self):
        self.close()
