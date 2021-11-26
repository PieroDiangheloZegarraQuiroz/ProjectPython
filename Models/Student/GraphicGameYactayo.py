import matplotlib.pyplot as plt
import numpy as np

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QLabel, QDialog


class Canvas(FigureCanvas):
    def __init__(self, parent):
        self.fig, self.ax = plt.subplots(figsize=(5, 4), dpi=80)
        super(Canvas, self).__init__(self.fig)
        self.setParent(parent)

        x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        y = np.array([1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10])
        self.ax.plot(x, y)
        plt.xlabel("Resultados")
        plt.ylabel("Probabilidades")
        plt.bar(x, y, color="blue", align="center")
        plt.xlabel("Resultados")
        plt.ylabel("Probabilidades")
        self.ax.grid()


class Graphic(QDialog):
    def __init__(self):
        super(Graphic, self).__init__()
        self.resize(600, 600)
        self.setWindowTitle("Resultado probabilistico")
        self.setStyleSheet("background: white")

        self.label = QLabel('Resultado probabilístico', self)
        self.label.setFont(QFont("Comic Sans MS", 14))
        self.label.move(180, 10)

        self.label1 = QLabel('<b>Espacio muestral:</b> S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}', self)
        self.label1.setFont(QFont("Comic Sans MS", 10))
        self.label1.move(30, 50)

        self.label2 = QLabel('<b>Variables aleatorias:</b> X = VA = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}', self)
        self.label2.setFont(QFont("Comic Sans MS", 10))
        self.label2.move(30, 80)

        self.label3 = QLabel('<b>Formula:</b> P(A) = N de casos favorables'
                             '/ N de casos posibles = P (x=1) = P(1) = 1/10', self)
        self.label3.setFont(QFont("Comic Sans MS", 10))
        self.label3.move(30, 110)

        self.label4 = QLabel('Representación en tabla:', self)
        self.label4.setFont(QFont("Comic Sans MS", 10, QFont.Bold))
        self.label4.move(30, 140)

        user_png = r"../../Images/Others/bar.png"
        try:
            with open(user_png):
                imageLogin = QLabel(self)
                pixmap = QPixmap(user_png)
                imageLogin.setPixmap(pixmap)
                imageLogin.move(20, 170)
                imageLogin.resize(600, 50)
        except FileNotFoundError:
            print("No se encontró la ruta")

        self.label5 = QLabel('Representación gráfica:', self)
        self.label5.setFont(QFont("Comic Sans MS", 10, QFont.Bold))
        self.label5.move(30, 240)
        chart = Canvas(self)
        chart.move(100, 260)
        chart.resize(400,300)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Graphic()
#     window.show()
#     sys.exit(app.exec_())

