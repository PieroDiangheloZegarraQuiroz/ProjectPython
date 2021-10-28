from PyQt5.QtCore import QDir
from urllib import request
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QTextEdit, QLineEdit, QMessageBox
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
        self.setWindowTitle("Download")
        self.display_widgets()

    def display_widgets(self):
        self.buttonDownload = QPushButton("Descargar nomvbre", self)
        self.buttonDownload.move(100, 00)
        self.buttonDownload.setEnabled(False)
        self.buttonDownload.clicked.connect(self.download)

        self.buttonUpload = QPushButton("Subir link", self)
        self.buttonUpload.move(250, 0)
        self.buttonUpload.setEnabled(False)
        self.buttonUpload.clicked.connect(self.upload)

        self.buttonClear = QPushButton("Limpiar", self)
        self.buttonClear.move(350, 57)
        self.buttonClear.setEnabled(False)
        self.buttonClear.clicked.connect(self.clear)

        self.urlBox = QLineEdit(self)
        self.urlBox.resize(300, 20)
        self.urlBox.move(10, 60)
        self.urlBox.textChanged.connect(self.buttonEnabled)

        files, quantity = ConnectionDB.Connection().listFile()

        # Iteración de los nombres para guardarlos en arreglo
        self.names = []
        for f in files:
            self.names.append(f[2])
        print(self.names)

        # Iteración de los links para guardarlos en arreglo
        self.urls = []
        for f in files:
            self.urls.append(f[1])
        print(self.urls)

        # Iteración de los id para guardarlos en arreglo
        self.ids = []
        for f in files:
            self.ids.append(f[0])
        print(self.ids)

        # Iteración del nombre y botoón para que se repita segun la cantidad
        self.value = None
        self.buttonNum = []
        for m in range(quantity):
            self.buttonNum.append(f"ButtonFile{m + 1}")
        print(self.buttonNum)

        for self.n in range(quantity):
            boton = self.buttonNum[self.n]
            boton = QPushButton(f"{boton}", self)
            boton.move(100, 100 * (self.n + 1))
            boton.clicked.connect(self.download)
            print(self.n)

    def buttonEnabled(self):
        if self.urlBox.text() != "":
            self.buttonDownload.setEnabled(True)
            self.buttonUpload.setEnabled(True)
            self.buttonClear.setEnabled(True)
        else:
            self.buttonDownload.setEnabled(False)
            self.buttonUpload.setEnabled(False)
            self.buttonClear.setEnabled(False)

    def download(self):
        print(self.value)
        files, quantity = ConnectionDB.Connection().listFile()
        self.urlClass.downloadUrl(self.urls[self.n])
        # remote_url = files[1][1]
        # local_file = QFileDialog.getSaveFileName(self, "Seleccionar uta", "", "Archivo PDF (*.pdf)")
        # request.urlretrieve(remote_url, local_file[0])
        # if local_file:
        #     QMessageBox.information(self, "Succeful", f"Se ha descargado el archivo", QMessageBox.Ok, QMessageBox.Ok)

    def upload(self):
        remote_url = self.urlBox.text()
        saved = ConnectionDB.Connection().insertFile(remote_url, "Aprendijzae", "Pruebades", 1)

    def clear(self):
        self.urlBox.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Download()
    window.show()
    sys.exit(app.exec_())
