from PyQt5.QtCore import QDir
from urllib import request
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QTextEdit, QLineEdit, QMessageBox
from Connection import ConnectionDB
import sys


class Download(QWidget):
    def __init__(self):
        super(Download, self).__init__()
        self.initialize()

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

        self.buttonFile = QPushButton(f"Descargar Aprendizaje 1", self)
        self.buttonFile.move(160, 120)
        self.buttonFile.clicked.connect(self.download)

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
        files, quantity, name = ConnectionDB.Connection().listFile()
        remote_url = str(files[1][1])
        local_file = QFileDialog.getSaveFileName(self, "Seleccionar ruta", "", "Archivo PDF (*.pdf)")
        request.urlretrieve(remote_url, local_file[0])

        if local_file:
            QMessageBox.information(self, "Succeful", f"Se ha descargado el archivo", QMessageBox.Ok, QMessageBox.Ok)

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
