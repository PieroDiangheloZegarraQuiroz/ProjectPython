from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QTextEdit
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
        self.btnAbrir = QPushButton("Abrir", self)
        self.btnAbrir.clicked.connect(self.upload)

        self.btnSave = QPushButton("Guardar", self)
        self.btnSave.move(100, 00)
        self.btnSave.clicked.connect(self.save)

        self.text_editor = QTextEdit(self)
        self.text_editor.resize(280, 350)
        self.text_editor.move(10, 60)

    def upload(self):

        file_name, ok = QFileDialog.getOpenFileName(self, "Elegir archivo", "C:\\",
                                                    "Archivo PDF (*.pdf)")
        if ok:
            saved = ConnectionDB.Connection().insertFile(file_name, "PDF", "DesPDF", 1)
            print(file_name)

    def save(self):
        ruta, tipo = QFileDialog.getSaveFileName(self, "Guardar Archivo", "../../../../Sebas/Desktop",
                                                 "Archivo PDF (*.pdf)")
        try:
            with open(ruta, "w") as r:
                r.write(self.file_name)
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Download()
    window.show()
    sys.exit(app.exec_())
