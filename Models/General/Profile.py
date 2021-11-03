from io import open
from os import getcwd, makedirs, path
from Connection import ConnectionDB
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QDialog, QPushButton,
                             QLabel, QFileDialog, QMessageBox)

from Models.Student import General_Interface


class selectProfile(QDialog):
    def __init__(self, idUser, parent=None):
        super(selectProfile, self).__init__()
        self.parent = parent
        self.idUser = idUser
        self.setWindowTitle("Selecciona una imagen...")
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(200, 275)
        self.initUI()

    def Image_Generic(self):
        self.ShortPathGeneric = path.basename(self.user_image)

    def initUI(self):
        # widgets
        self.labelImagen = QLabelClickable(self)
        self.labelImagen.setGeometry(15, 15, 168, 180)
        self.labelImagen.setToolTip("Imagen")
        self.labelImagen.setCursor(Qt.PointingHandCursor)
        self.labelImagen.setStyleSheet("QLabel {background-color: white; border: 1px solid "
                                       "#01DFD7; border-radius: 2px;}")
        self.labelImagen.setAlignment(Qt.AlignCenter)

        buttonSeleccionar = QPushButton("Seleccionar", self)
        buttonSeleccionar.setToolTip("Seleccionar imagen")
        buttonSeleccionar.setCursor(Qt.PointingHandCursor)
        buttonSeleccionar.setGeometry(15, 200, 168, 25)

        self.buttonGuardar = QPushButton("Guardar", self)
        self.buttonGuardar.setToolTip("Guardar imagen")
        self.buttonGuardar.setCursor(Qt.PointingHandCursor)
        self.buttonGuardar.setGeometry(15, 233, 168, 25)

        self.labelImagen.clicked.connect(self.seleccionarImagen)
        buttonSeleccionar.clicked.connect(self.seleccionarImagen)
        self.buttonGuardar.clicked.connect(self.Guardar)

    def seleccionarImagen(self):
        self.imagenpath, extension = QFileDialog.getOpenFileName(self, "Seleccionar imagen", getcwd(),
                                                                 "Archivos de imagen (*.png *.jpg)",
                                                                 options=QFileDialog.Options())
        if self.imagenpath:
            # Adaptar imagen
            self.pixmapImagen = QPixmap(self.imagenpath).scaled(166, 178, Qt.KeepAspectRatio,
                                                                Qt.SmoothTransformation)
            # Mostrar imagen
            self.labelImagen.setPixmap(self.pixmapImagen)

        self.ShortPfpPath = path.basename(self.imagenpath)

    def Guardar(self):
        OnlyNamePfp_Guardar = self.ShortPfpPath  # Este es la imagen
        foto = self.labelImagen.pixmap()
        if not QFile.exists("../Images/Profile"):
            makedirs("../Images/Profile")
        foto.save(f"../../Images/Profile/{OnlyNamePfp_Guardar}", quality=100)

        ConnectionDB.Connection().changeAvatar(self.idUser, OnlyNamePfp_Guardar)
        QMessageBox.information(self, "Guardar imagen", "Imagen Guardada", QMessageBox.Ok)
        self.close()


class QLabelClickable(QLabel):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super(QLabelClickable, self).__init__(parent)

    def mousePressEvent(self, event):
        self.clicked.emit()
