from PyQt5.QtCore import QDir
from urllib import request
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QTextEdit, QLineEdit, QMessageBox, \
    QTableWidget, QTableWidgetItem, QAbstractItemView, QAction, QActionGroup, QMenu
from PyQt5.QtCore import Qt
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
        files, quantity = ConnectionDB.Connection().listFile()

        self.tabla = QTableWidget(self)
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla.setColumnCount(3)
        self.tabla.horizontalHeader().setDefaultSectionSize(150)
        self.tabla.setRowCount(quantity)
        self.tabla.setHorizontalHeaderLabels(("Url", "Name", "Description"))
        self.tabla.resize(317, 240)
        self.tabla.move(20, 56)
        row = 0
        for r in files:
            self.tabla.setRowCount(row + 1)
            self.tabla.setItem(row, 0, QTableWidgetItem(r[1]))
            self.tabla.setItem(row, 1, QTableWidgetItem(r[2]))
            self.tabla.setItem(row, 2, QTableWidgetItem(r[3]))
            row = row + 1
        self.tabla.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tabla.customContextMenuRequested.connect(self.menuContextual)

    def menuContextual(self, posicion):
        indices = self.tabla.selectedIndexes()

        if indices:
            menu = QMenu()

            itemsGrupo = QActionGroup(self)
            itemsGrupo.setExclusive(True)

            menu.addAction(QAction("Copiar todo", itemsGrupo))

            columnas = [self.tabla.horizontalHeaderItem(columna).text()
                        for columna in range(self.tabla.columnCount())
                        if not self.tabla.isColumnHidden(columna)]

            copiarIndividual = menu.addMenu("Copiar individual")
            for indice, item in enumerate(columnas, start=0):
                accion = QAction(item, itemsGrupo)
                accion.setData(indice)

                copiarIndividual.addAction(accion)

            itemsGrupo.triggered.connect(self.copiarTableWidgetItem)

            menu.exec_(self.tabla.viewport().mapToGlobal(posicion))

    def copiarTableWidgetItem(self, accion):
        filaSeleccionada = [dato.text() for dato in self.tabla.selectedItems()]

        if accion.text() == "Copiar todo":
            filaSeleccionada = tuple(filaSeleccionada)
        else:
            filaSeleccionada = filaSeleccionada[accion.data()]

        print(filaSeleccionada)

        return

    def download(self, accion):
        filaSeleccionada = [dato.text() for dato in self.tabla.selectedItems()]
        accion = None

        print(filaSeleccionada)
        files, quantity = ConnectionDB.Connection().listFile()
        #self.urlClass.downloadUrl(self.urls[self.n])
        # remote_url = files[1][1]
        # local_file = QFileDialog.getSaveFileName(self, "Seleccionar ruta", "", "Archivo PDF (*.pdf)")
        # request.urlretrieve(remote_url, local_file[0])
        # if local_file:
        #     QMessageBox.information(self, "Succeful", f"Se ha descargado el archivo", QMessageBox.Ok, QMessageBox.Ok)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Download()
    window.show()
    sys.exit(app.exec_())
