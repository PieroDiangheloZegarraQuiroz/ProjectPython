import sys
from urllib import request

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import *
from Connection import ConnectionDB
from PyQt5.QtGui import *


class QLabelClick(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        # self.clicked.emit()
        url = self.text()
        remote_url = url
        local_file = QFileDialog.getSaveFileName(self, "Seleccionar ruta", "", "Archivo PDF (*.pdf)")
        request.urlretrieve(remote_url, local_file[0])
        if local_file:
            QMessageBox.information(self, "Succeful", f"Se ha descargado el archivo", QMessageBox.Ok, QMessageBox.Ok)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QScrollArea Test')
        self.setGeometry(400, 400, 600, 400)

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
            self.vars = QLabel(f'{self.names[i]}\t\t{self.descriptions[i]}', self)
            self.vars.move(30, 50 * (i + 1))

            # self.descs = QLabel(f'{self.descriptions[i]}', self)
            # self.descs.move(120, 50 * (i + 1))

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


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
