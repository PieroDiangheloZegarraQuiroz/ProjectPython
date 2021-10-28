from PyQt5.QtCore import *
from urllib import request
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QTextEdit, QLineEdit, QMessageBox, QLabel, \
    QScrollArea, QVBoxLayout, QFormLayout, QGroupBox
import Test.urlDow
from Connection import ConnectionDB
from Test import *
import sys


class QLabelClick(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        print(self.text())
        # self.clicked.emit()
        url = self.text()
        remote_url = url
        local_file = QFileDialog.getSaveFileName(self, "Seleccionar uta", "", "Archivo PDF (*.pdf)")
        request.urlretrieve(remote_url, local_file[0])
        if local_file:
            QMessageBox.information(self, "Succeful", f"Se ha descargado el archivo", QMessageBox.Ok, QMessageBox.Ok)


class Download(QWidget):
    def __init__(self):
        super(Download, self).__init__()
        self.initialize()
        self.urlClass = Test.urlDow.Url()

    def initialize(self):
        # self.resize(600, 500)
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("Download")
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
            self.vars = QLabel(f'{self.names[i]}', self)
            self.vars.move(30, 50 * (i + 1))

            self.descs = QLabel(f'{self.descriptions[i]}', self)
            self.descs.move(120, 50 * (i + 1))

            self.varsu = QLabelClick(f'{self.urls[i]}', self)
            self.varsu.move(210, 50 * (i + 1))
            formLayout.setContentsMargins(100, 10, 5, 5)
            formLayout.setHorizontalSpacing(50)
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
