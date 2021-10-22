from Connection import ConnectionDB
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QTextEdit, QLineEdit, QMessageBox
from urllib import request


class Url(QWidget):
    def __init__(self):
        super(Url, self).__init__()

    def downloadUrl(self, urls):
        remote_url = urls
        local_file = QFileDialog.getSaveFileName(self, "Seleccionar ruta", "", "Archivo PDF (*.pdf)")
        request.urlretrieve(remote_url, local_file[0])
        if local_file:
            QMessageBox.information(self, "Succeful", f"Se ha descargado el archivo", QMessageBox.Ok, QMessageBox.Ok)
