from PyQt5.QtCore import QDir
from urllib import request

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QTextEdit, QLineEdit, QMessageBox, QLabel
import Test.urlDow
from Connection import ConnectionDB
from Test import *
import sys


class Download(QWidget):
    def __init__(self):
        super(Download, self).__init__()
        self.initialize()
        self.urlClass = Test.urlDow.Url()  # Llamando a otra clase

    def initialize(self):
        self.resize(500, 500)
        self.setStyleSheet("background-color: white;")
        self.setWindowTitle("Download")
        self.display_widgets()

    def display_widgets(self):
        # Label
        self.label1 = QLabel("Subir Archivo", self)
        self.label1.setFont(QFont("Arial", 18, QFont.Bold))
        self.label1.move(170, 20)
        # Text Boxes
        self.nameBox = QLineEdit(self)
        self.nameBox.resize(300, 40)
        self.nameBox.move(90, 100)
        self.nameBox.setPlaceholderText("Nombre")
        self.nameBox.setStyleSheet("background-color: rgba(0, 0, 0, 0);"
                                   "border: none;"
                                   "border-bottom: 2px solid rgba(46, 82, 101, 200);"
                                   "color: rgba(0, 0, 0, 240);"
                                   "padding-bottom: 5px;")

        self.urlBox = QLineEdit(self)
        self.urlBox.resize(300, 40)
        self.urlBox.move(90, 150)
        self.urlBox.setPlaceholderText("Url")
        self.urlBox.setStyleSheet("background-color: rgba(0, 0, 0, 0);"
                                  "border: none;"
                                  "border-bottom: 2px solid rgba(46, 82, 101, 200);"
                                  "color: rgba(0, 0, 0, 240);"
                                  "padding-bottom: 5px;")
        self.urlBox.textChanged.connect(self.buttonEnabled)

        self.descriptionBox = QTextEdit(self)
        self.descriptionBox.resize(300, 100)
        self.descriptionBox.move(90, 230)
        self.descriptionBox.setPlaceholderText("Descripción...")
        self.descriptionBox.setStyleSheet(
            "border-radius: 8px;"
            "border: 2px solid rgba(46, 82, 101, 200);"
            "color: rgba(0, 0, 0, 240);"
            "padding-bottom: 5px;")

        # Buttons
        self.buttonUpload = QPushButton("Subir", self)
        self.buttonUpload.move(120, 350)
        self.buttonUpload.setEnabled(False)
        self.buttonUpload.setFont(QFont("Bookman Old Style", 12))
        self.buttonUpload.clicked.connect(self.upload)
        self.buttonUpload.setStyleSheet("background-color: rgb(30, 218, 230);"
                                        "color: white;")

        self.buttonClear = QPushButton("Limpiar", self)
        self.buttonClear.move(280, 350)
        self.buttonClear.setEnabled(False)
        self.buttonClear.clicked.connect(self.clear)

    def buttonEnabled(self):
        if self.urlBox.text() != "":
            self.buttonUpload.setEnabled(True)
            self.buttonClear.setEnabled(True)
        else:
            self.buttonUpload.setEnabled(False)
            self.buttonClear.setEnabled(False)

    def upload(self):
        name = self.nameBox.text()
        description = self.descriptionBox
        remote_url = self.urlBox.text()
        saved = ConnectionDB.Connection().insertFile(remote_url, "Aprendijzae", "Pruebades", 1)

    def clear(self):
        self.urlBox.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Download()
    window.show()
    sys.exit(app.exec_())
