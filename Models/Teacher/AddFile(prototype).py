import Connection.ConnectionDB
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox, QMainWindow, \
    QFileDialog, QDialog
from PyQt5.QtGui import QFont, QPixmap, QPalette, QBrush, QIcon
import sys

from Connection import ConnectionDB


class insertando(QDialog):

    def __init__(self):
        super(insertando, self).__init__()
        self.initialize()

    def initialize(self):
        self.setWindowTitle("Subir Archivo")
        self.resize(500, 500)
        self.setStyleSheet("background-color: white;")

        # Label
        self.label1 = QLabel("Subir Archivo", self)
        self.label1.setFont(QFont("Comic Sans MS", 18, QFont.Bold))
        self.label1.resize(170, 30)
        self.label1.move(170, 20)

        self.label2 = QLabel("Directorio: ", self)
        self.label2.setFont(QFont("Comic Sans MS", 10, QFont.Bold))
        self.label2.resize(170, 30)
        self.label2.move(50, 140)
        self.label2.hide()

        self.label3 = QLabel("None ", self)
        self.label3.setFont(QFont("Comic Sans MS", 10, QFont.Bold))
        self.label3.resize(400, 30)
        self.label3.move(120, 140)
        self.label3.hide()

        # Buttons
        self.btnAbrir = QPushButton("Seleccionar PDF", self)
        self.btnAbrir.move(170, 90)
        self.btnAbrir.resize(150, 30)
        self.btnAbrir.setFont(QFont("Comic Sans MS", 12))
        self.btnAbrir.clicked.connect(self.open)
        self.btnAbrir.setStyleSheet("border-radius: 5px;"
                                    "background-color: rgb(14, 150, 232);"
                                    "color: white;")

        self.saveButton = QPushButton("Guardar", self)
        self.saveButton.move(180, 300)
        self.saveButton.resize(130, 30)
        self.saveButton.setFont(QFont("Comic Sans MS", 12))
        self.saveButton.clicked.connect(self.save)
        self.saveButton.setStyleSheet("border-radius: 5px;"
                                      "background-color: gray;"
                                      "color: white;")

    def fileToBinary(self, file):
        if file:
            with open(file, 'rb') as f:
                blob = f.read()
                QMessageBox.information(self, "Message", f"Archivo seleccionado", QMessageBox.Ok,
                                        QMessageBox.Ok)
                self.label2.show()
                self.label3.show()
                self.saveButton.setEnabled(True)
                self.saveButton.setStyleSheet("border-radius: 5px;"
                                              "background-color: rgb(232, 93, 97);"
                                              "color: white;")
                return blob
        else:
            QMessageBox.warning(self, "Error", f"No se ha seleccionado ningun archivo", QMessageBox.Ok, QMessageBox.Ok)
            self.saveButton.setEnabled(False)
            self.saveButton.setStyleSheet("border-radius: 5px;"
                                          "background-color: gray;"
                                          "color: white;")

    # def binaryToFile(self, blob, archivo):
    #     with open(archivo, 'wb') as f:
    #         f.write(blob)

    def open(self):
        archivo = QFileDialog.getOpenFileName(self, "Seleccionar", "", "Files PDF (*.pdf)")
        if not archivo[0] is None:
            self.binary = self.fileToBinary(f'{archivo[0]}')
            self.label3.setText(archivo[0])

    def save(self):
        if self.binary is None:
            QMessageBox.warning(self, "Error", f"No hay ningun archivo", QMessageBox.Ok, QMessageBox.Ok)
        else:
            ConnectionDB.Connection().insertFiles2(self.binary)
            QMessageBox.information(self, "Succeful", f"Se ha subido con éxito", QMessageBox.Ok, QMessageBox.Ok)
            self.label3.setText("")
            self.saveButton.setEnabled(False)
            self.saveButton.setStyleSheet("border-radius: 5px;"
                                          "background-color: gray;"
                                          "color: white;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = insertando()
    window.show()
    sys.exit(app.exec_())
