import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QMessageBox, QLabel, QDialog
from PyQt5.QtCore import *

from Connection import ConnectionDB


class Form(QDialog):
    def __init__(self, idUser):
        super(Form, self).__init__()
        self.idUser = str(idUser)
        self.initialize()

    def initialize(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setGeometry(550, 250, 500, 650)
        self.move(650, 150)
        self.setStyleSheet("background-color: white;")
        self.display_widgets()

    def display_widgets(self):
        # Var
        self.contador = 0

        # Label
        self.label1 = QLabel("Formulario", self)
        self.label1.setFont(QFont("Comic Sans MS", 18, QFont.Bold))
        self.label1.move(170, 20)

        # Buttons
        self.buttonInsert = QPushButton("Añadir", self)
        self.buttonInsert.resize(100, 30)
        self.buttonInsert.move(100, 80)
        self.buttonInsert.clicked.connect(self.insertForm)
        self.buttonInsert.clicked.connect(self.buttonEnabled)
        self.buttonInsert.setFont(QFont("Comic Sans MS", 12))
        self.buttonInsert.setStyleSheet("border-radius: 5px;"
                                        "background-color: rgb(14, 150, 232);"
                                        "color: white;")

        self.buttonSave = QPushButton("Insertar", self)
        self.buttonSave.resize(100, 30)
        self.buttonSave.move(260, 80)
        self.buttonSave.setEnabled(False)
        self.buttonSave.setFont(QFont("Comic Sans MS", 12))
        self.buttonSave.clicked.connect(self.saveForm)
        self.buttonSave.setStyleSheet("border-radius: 5px;"
                                      "background-color: gray;"
                                      "color: white;")

    def insertForm(self):
        self.contador = self.contador + 1
        self.stylo = "background-color: rgba(0, 0, 0, 0);" \
                     "border: none;" \
                     "border-bottom: 2px solid rgba(46, 82, 101, 200);" \
                     "color: rgba(0, 0, 0, 240);" \
                     "padding-bottom: 5px;"

        if self.contador == 1:
            self.textBox1 = QLineEdit(self)
            self.textBox1.setPlaceholderText("Pregunta 1")
            self.textBox1.resize(300, 30)
            self.textBox1.move(100, 150)
            self.textBox1.setFont(QFont("Comic Sans MS", 8))
            self.textBox1.setStyleSheet(self.stylo)
            self.textBox1.show()
            self.textBox1.textChanged.connect(self.buttonEnabled)
        elif self.contador == 2:
            self.textBox2 = QLineEdit(self)
            self.textBox2.setPlaceholderText("Pregunta 2")
            self.textBox2.resize(300, 30)
            self.textBox2.move(100, 200)
            self.textBox2.setFont(QFont("Comic Sans MS", 8))
            self.textBox2.setStyleSheet(self.stylo)
            self.textBox2.show()
            self.textBox2.textChanged.connect(self.buttonEnabled)
        elif self.contador == 3:
            self.textBox3 = QLineEdit(self)
            self.textBox3.setPlaceholderText("Pregunta 3")
            self.textBox3.resize(300, 30)
            self.textBox3.move(100, 250)
            self.textBox3.setFont(QFont("Comic Sans MS", 8))
            self.textBox3.setStyleSheet(self.stylo)
            self.textBox3.show()
            self.textBox3.textChanged.connect(self.buttonEnabled)
        elif self.contador == 4:
            self.textBox4 = QLineEdit(self)
            self.textBox4.setPlaceholderText("Pregunta 4")
            self.textBox4.resize(300, 30)
            self.textBox4.move(100, 300)
            self.textBox4.setFont(QFont("Comic Sans MS", 8))
            self.textBox4.setStyleSheet(self.stylo)
            self.textBox4.show()
            self.textBox4.textChanged.connect(self.buttonEnabled)
        elif self.contador == 5:
            self.textBox5 = QLineEdit(self)
            self.textBox5.setPlaceholderText("Pregunta 5")
            self.textBox5.resize(300, 30)
            self.textBox5.move(100, 350)
            self.textBox5.setFont(QFont("Comic Sans MS", 8))
            self.textBox5.setStyleSheet(self.stylo)
            self.textBox5.show()
            self.textBox5.textChanged.connect(self.buttonEnabled)
        elif self.contador == 6:
            self.textBox6 = QLineEdit(self)
            self.textBox6.setPlaceholderText("Pregunta 6")
            self.textBox6.resize(300, 30)
            self.textBox6.move(100, 400)
            self.textBox6.setFont(QFont("Comic Sans MS", 8))
            self.textBox6.setStyleSheet(self.stylo)
            self.textBox6.show()
            self.textBox6.textChanged.connect(self.buttonEnabled)
        elif self.contador == 7:
            self.textBox7 = QLineEdit(self)
            self.textBox7.setPlaceholderText("Pregunta 7")
            self.textBox7.resize(300, 30)
            self.textBox7.move(100, 450)
            self.textBox7.setFont(QFont("Comic Sans MS", 8))
            self.textBox7.setStyleSheet(self.stylo)
            self.textBox7.show()
            self.textBox7.textChanged.connect(self.buttonEnabled)
        elif self.contador == 8:
            self.textBox8 = QLineEdit(self)
            self.textBox8.setPlaceholderText("Pregunta 8")
            self.textBox8.resize(300, 30)
            self.textBox8.move(100, 500)
            self.textBox8.setFont(QFont("Comic Sans MS", 8))
            self.textBox8.setStyleSheet(self.stylo)
            self.textBox8.show()
            self.textBox8.textChanged.connect(self.buttonEnabled)
        elif self.contador == 9:
            self.textBox9 = QLineEdit(self)
            self.textBox9.setPlaceholderText("Pregunta 9")
            self.textBox9.resize(300, 30)
            self.textBox9.move(100, 550)
            self.textBox9.setFont(QFont("Comic Sans MS", 8))
            self.textBox9.setStyleSheet(self.stylo)
            self.textBox9.show()
            self.textBox9.textChanged.connect(self.buttonEnabled)
        elif self.contador == 10:
            self.textBox10 = QLineEdit(self)
            self.textBox10.setPlaceholderText("Pregunta 10")
            self.textBox10.resize(300, 30)
            self.textBox10.move(100, 600)
            self.textBox10.setFont(QFont("Comic Sans MS", 8))
            self.textBox10.setStyleSheet(self.stylo)
            self.textBox10.show()
            self.textBox10.textChanged.connect(self.buttonEnabled)

            self.buttonInsert.setEnabled(False)
            self.buttonInsert.setStyleSheet("border-radius: 5px;"
                                            "background-color: gray;"
                                            "color: white;")

            QMessageBox.information(self, "Message",
                                    "Ya no se podran añadir mas cajas de texto",
                                    QMessageBox.Ok, QMessageBox.Ok)

    def limpiar(self):
        if self.contador == 1:
            self.textBox1.clear()
        elif self.contador == 2:
            self.textBox1.clear()
            self.textBox2.clear()
        elif self.contador == 3:
            self.textBox1.clear()
            self.textBox2.clear()
            self.textBox3.clear()
        elif self.contador == 4:
            self.textBox1.clear()
            self.textBox2.clear()
            self.textBox3.clear()
            self.textBox4.clear()
        elif self.contador == 5:
            self.textBox1.clear()
            self.textBox2.clear()
            self.textBox3.clear()
            self.textBox4.clear()
            self.textBox5.clear()
        elif self.contador == 6:
            self.textBox1.clear()
            self.textBox2.clear()
            self.textBox3.clear()
            self.textBox4.clear()
            self.textBox5.clear()
            self.textBox6.clear()
        elif self.contador == 7:
            self.textBox1.clear()
            self.textBox2.clear()
            self.textBox3.clear()
            self.textBox4.clear()
            self.textBox5.clear()
            self.textBox6.clear()
            self.textBox7.clear()
        elif self.contador == 8:
            self.textBox1.clear()
            self.textBox2.clear()
            self.textBox3.clear()
            self.textBox4.clear()
            self.textBox5.clear()
            self.textBox6.clear()
            self.textBox7.clear()
            self.textBox8.clear()
        elif self.contador == 9:
            self.textBox1.clear()
            self.textBox2.clear()
            self.textBox3.clear()
            self.textBox4.clear()
            self.textBox5.clear()
            self.textBox6.clear()
            self.textBox7.clear()
            self.textBox8.clear()
            self.textBox9.clear()
        elif self.contador == 10:
            self.textBox1.clear()
            self.textBox2.clear()
            self.textBox3.clear()
            self.textBox4.clear()
            self.textBox5.clear()
            self.textBox6.clear()
            self.textBox7.clear()
            self.textBox8.clear()
            self.textBox9.clear()
            self.textBox10.clear()

    def saveForm(self):
        if self.contador == 1:
            ConnectionDB.Connection().insertQuestions(self.textBox1.text(), '', '', '', '', '', '', '', '',
                                                      '', self.idUser)
        elif self.contador == 2:
            ConnectionDB.Connection().insertQuestions(self.textBox1.text(), self.textBox2.text(), '', '', '', '', '',
                                                      '', '',
                                                      '', self.idUser)
        elif self.contador == 3:
            ConnectionDB.Connection().insertQuestions(self.textBox1.text(), self.textBox2.text(), self.textBox3.text(),
                                                      '', '', '', '', '', '',
                                                      '', self.idUser)
        elif self.contador == 4:
            ConnectionDB.Connection().insertQuestions(self.textBox1.text(), self.textBox2.text(), self.textBox3.text(),
                                                      self.textBox4.text(), '', '', '', '', '',
                                                      '', self.idUser)
        elif self.contador == 5:
            ConnectionDB.Connection().insertQuestions(self.textBox1.text(), self.textBox2.text(), self.textBox3.text(),
                                                      self.textBox4.text(), self.textBox5.text(), '', '', '', '',
                                                      '', self.idUser)
        elif self.contador == 6:
            ConnectionDB.Connection().insertQuestions(self.textBox1.text(), self.textBox2.text(), self.textBox3.text(),
                                                      self.textBox4.text(), self.textBox5.text(), self.textBox6.text(),
                                                      '', '', '', '', self.idUser)
        elif self.contador == 7:
            ConnectionDB.Connection().insertQuestions(self.textBox1.text(), self.textBox2.text(), self.textBox3.text(),
                                                      self.textBox4.text(), self.textBox5.text(), self.textBox6.text(),
                                                      self.textBox7.text(), '', '', '', self.idUser)
        elif self.contador == 8:
            ConnectionDB.Connection().insertQuestions(self.textBox1.text(), self.textBox2.text(), self.textBox3.text(),
                                                      self.textBox4.text(), self.textBox5.text(), self.textBox6.text(),
                                                      self.textBox7.text(), self.textBox8.text(), '', '', self.idUser)
        elif self.contador == 9:
            ConnectionDB.Connection().insertQuestions(self.textBox1.text(), self.textBox2.text(), self.textBox3.text(),
                                                      self.textBox4.text(), self.textBox5.text(), self.textBox6.text(),
                                                      self.textBox7.text(), self.textBox8.text(), self.textBox9.text(),
                                                      '', self.idUser)
        elif self.contador == 10:
            ConnectionDB.Connection().insertQuestions(self.textBox1.text(), self.textBox2.text(), self.textBox3.text(),
                                                      self.textBox4.text(), self.textBox5.text(), self.textBox6.text(),
                                                      self.textBox7.text(), self.textBox8.text(), self.textBox9.text(),
                                                      self.textBox10.text(), self.idUser)

        QMessageBox.information(self, "Succeful",
                                "Se ha ingresado el formulario",
                                QMessageBox.Ok, QMessageBox.Ok)
        self.limpiar()

    def buttonEnabled(self):
        self.stylo2 = "border-radius: 5px;" \
                      "background-color: rgb(232, 93, 97);" \
                      "color: white;"
        if self.textBox1.text() != "" and self.contador == 1:
            self.buttonSave.setEnabled(True)
            self.buttonSave.setStyleSheet(self.stylo2)
        elif self.textBox1.text() != "" and self.textBox2.text() != "" and self.contador == 2:
            self.buttonSave.setEnabled(True)
            self.buttonSave.setStyleSheet(self.stylo2)

        elif self.textBox1.text() != "" and self.textBox2.text() != "" and self.textBox3.text() != "" and \
                self.contador == 3:
            self.buttonSave.setEnabled(True)
            self.buttonSave.setStyleSheet(self.stylo2)

        elif self.textBox1.text() != "" and self.textBox2.text() != "" and self.textBox3.text() != "" and \
                self.textBox4.text() != "" and self.contador == 4:
            self.buttonSave.setEnabled(True)
            self.buttonSave.setStyleSheet(self.stylo2)

        elif self.textBox1.text() != "" and self.textBox2.text() != "" and self.textBox3.text() != "" and \
                self.textBox4.text() != "" and self.textBox5.text() != "" and self.contador == 5:
            self.buttonSave.setEnabled(True)
            self.buttonSave.setStyleSheet(self.stylo2)

        elif self.textBox1.text() != "" and self.textBox2.text() != "" and self.textBox3.text() != "" and \
                self.textBox4.text() != "" and self.textBox5.text() != "" and self.textBox6.text() != "" \
                and self.contador == 6:
            self.buttonSave.setEnabled(True)
            self.buttonSave.setStyleSheet(self.stylo2)

        elif self.textBox1.text() != "" and self.textBox2.text() != "" and self.textBox3.text() != "" and \
                self.textBox4.text() != "" and self.textBox5.text() != "" and self.textBox6.text() != "" \
                and self.textBox7.text() != "" and self.contador == 7:
            self.buttonSave.setEnabled(True)
            self.buttonSave.setStyleSheet(self.stylo2)

        elif self.textBox1.text() != "" and self.textBox2.text() != "" and self.textBox3.text() != "" and \
                self.textBox4.text() != "" and self.textBox5.text() != "" and self.textBox6.text() != "" \
                and self.textBox7.text() != "" and self.textBox8.text() != "" and self.contador == 8:
            self.buttonSave.setEnabled(True)
            self.buttonSave.setStyleSheet(self.stylo2)

        elif self.textBox1.text() != "" and self.textBox2.text() != "" and self.textBox3.text() != "" and \
                self.textBox4.text() != "" and self.textBox5.text() != "" and self.textBox6.text() != "" \
                and self.textBox7.text() != "" and self.textBox8.text() != "" and self.textBox9.text() != "" and \
                self.contador == 9:
            self.buttonSave.setEnabled(True)
            self.buttonSave.setStyleSheet(self.stylo2)

        elif self.textBox1.text() != "" and self.textBox2.text() != "" and self.textBox3.text() != "" and \
                self.textBox4.text() != "" and self.textBox5.text() != "" and self.textBox6.text() != "" \
                and self.textBox7.text() != "" and self.textBox8.text() != "" and self.textBox9.text() != "" and \
                self.textBox10.text() != "" and self.contador == 10:
            self.buttonSave.setEnabled(True)
            self.buttonSave.setStyleSheet(self.stylo2)

        else:
            self.buttonSave.setEnabled(False)
            self.buttonSave.setStyleSheet("border-radius: 5px;"
                                          "background-color: gray;"
                                          "color: white;")
