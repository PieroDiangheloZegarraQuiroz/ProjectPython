from PyQt5.QtCore import *
from urllib import request

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QTextEdit, QLineEdit, QMessageBox, QLabel, \
    QScrollArea, QVBoxLayout, QFormLayout, QGroupBox, QDialog
import Test.urlDow
from Connection import ConnectionDB
import sys


class QLabelClick(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        url = self.text()
        indice0 = url.index('https')
        indicef = url.index("'><img")
        subcadena = url[indice0:indicef]

        remote_url = subcadena
        local_file = QFileDialog.getSaveFileName(self, "Seleccionar uta", "", "Archivo PDF (*.pdf)")
        request.urlretrieve(remote_url, local_file[0])
        if local_file[0] != "":
            QMessageBox.information(self, "Succeful", f"Se ha descargado el archivo", QMessageBox.Ok, QMessageBox.Ok)
        elif local_file[0] == "":
            QMessageBox.warning(self, "Message", f"No se ha descargado el archivo", QMessageBox.Ok, QMessageBox.Ok)


class Download(QDialog):
    def __init__(self):
        super(Download, self).__init__()
        self.initialize()
        self.urlClass = Test.urlDow.Url()

    def initialize(self):
        self.setStyleSheet("background-color: white;")
        # self.resize(600, 500)
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("Lecturas recomendadas")
        self.display_widgets()

    def display_widgets(self):

        formLayout = QFormLayout()
        groupBox = QGroupBox()

        files, quantity = ConnectionDB.Connection().listFile()
        #
        self.urls = []
        for u in files:
            self.urls.append(u[1])
        #
        self.names = []
        for n in files:
            self.names.append(n[2])
        #
        self.descriptions = []
        for d in files:
            self.descriptions.append(d[3])
        #
        self.vars = []
        for i in range(quantity):
            self.vars.append(f'labs{i + 1}')
        #
        self.descs = []
        for i in range(quantity):
            self.descs.append(f'des{i + 1}')
        #
        self.varsu = []
        for i in range(quantity):
            self.varsu.append(f'lab{i + 1}')

        for i in range(quantity):
            self.vars = QLabel(f'<b>Titulo</b>: {self.names[i]}', self)
            self.vars.setFont(QFont("Comic Sans MS", 10))
            self.vars.move(30, 50 * (i + 1))

            self.descs = QLabel(f'{self.descriptions[i]}', self)
            self.descs.move(120, 50 * (i + 1))

            image = r'../../Images/Others/icono.png'
            self.varsu = QLabelClick(f"<a href='{self.urls[i]}'><img src='{image}' alt='Los Tejos' /></a>", self)
            self.varsu.move(210, 50 * (i + 1))

            formLayout.setContentsMargins(50, 10, 5, 5)
            formLayout.setHorizontalSpacing(200)
            formLayout.setVerticalSpacing(50)
            formLayout.addRow(self.vars, self.varsu)
            formLayout.setAlignment(Qt.AlignCenter)

        groupBox.setLayout(formLayout)

        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)

        layout = QVBoxLayout(self)
        layout.addWidget(scroll)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Download()
    window.show()
    sys.exit(app.exec_())
