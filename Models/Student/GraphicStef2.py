import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import QApplication, QLabel, QDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import *


class QLabelClick(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()


class Canvas(FigureCanvas):
    def __init__(self, parent):
        self.fig, self.ax = plt.subplots(figsize=(5, 4), dpi=80)
        super(Canvas, self).__init__(self.fig)
        self.setParent(parent)

        x = np.array(["Piedra", "Papel", "Tijera"])
        y = np.array([1 / 3, 1 / 3, 1 / 3])
        self.ax.plot(x, y)
        plt.bar(x, y, color="red", align="center")
        plt.xlabel("Resultados")
        plt.ylabel("Frecuencia")
        self.ax.grid()


class Graphic2(QDialog):
    def __init__(self):
        super(Graphic2, self).__init__()
        self.resize(600, 600)
        self.setWindowTitle("Resultado probabilistico")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet("background: white")

        Icon_Return = r"../../Images/Others/IconoReturn_1.png"
        try:
            with open(Icon_Return):
                Image = QLabelClick(self)
                pixmap = QPixmap(Icon_Return)
                Image.setPixmap(pixmap)
                Image.move(10, -20)
                Image.resize(180, 120)
        except FileNotFoundError:
            print("Nose encontro el archivo")

        Image.clicked.connect(self.close_function)

        # labels
        self.label = QLabel('Análisis Estadístico', self)
        self.label.setFont(QFont("Segoe Print", 14))
        self.label.move(220, 10)

        self.label1 = QLabel('<b>Espacio muestral:</b> S = {Piedra, Papel, Tijera}', self)
        self.label1.setFont(QFont("Segoe Print", 10))
        self.label1.move(30, 70)

        self.label2 = QLabel('<b>Variables aleatorias:</b> X = {1, 2, 3}', self)
        self.label2.setFont(QFont("Segoe Print", 10))
        self.label2.move(30, 100)

        self.label3 = QLabel('Representación en tabla:', self)
        self.label3.setFont(QFont("Segoe Print", 10, QFont.Bold))
        self.label3.move(30, 140)

        user_png = r"../../Images/Others/grafica2.PNG"
        try:
            with open(user_png):
                login_image = QLabel(self)
                pixmap = QPixmap(user_png)
                login_image.setPixmap(pixmap)
                login_image.move(10, 180)
                login_image.resize(600, 50)
        except FileNotFoundError:
            print("No se encontró la ruta")

        self.label4 = QLabel('Representación gráfica:', self)
        self.label4.setFont(QFont("Segoe Print", 10, QFont.Bold))
        self.label4.move(30, 240)
        chart = Canvas(self)
        chart.move(100, 260)
        chart.resize(400, 300)

    def close_function(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Graphic2()
    window.show()
    sys.exit(app.exec_())
