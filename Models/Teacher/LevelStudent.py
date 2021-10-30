from PyQt5.QtWidgets import QLabel, QPushButton, QApplication, QMainWindow
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox, QLabel, QScrollArea, QVBoxLayout, QFormLayout, \
    QGroupBox, QDialog


class LvlStudent(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setGeometry(550, 250, 500, 650)
        self.setWindowTitle("")
        self.setStyleSheet("background-color: white;")
        self.move(650, 150)

        self.btnAbrir = QPushButton("5to", self)
        self.btnAbrir.move(170, 90)
        self.btnAbrir.resize(150, 30)
        self.btnAbrir.setFont(QFont("Comic Sans MS", 12))
        self.btnAbrir.clicked.connect(self.open)
        self.btnAbrir.setStyleSheet("border-radius: 5px;"
                                    "background-color: rgb(14, 150, 232);"
                                    "color: white;")

        self.btnAbrir1 = QPushButton("4to", self)
        self.btnAbrir1.move(170, 140)
        self.btnAbrir1.resize(150, 30)
        self.btnAbrir1.setFont(QFont("Comic Sans MS", 12))
        #self.btnAbrir1.clicked.connect(self.open)
        self.btnAbrir1.setStyleSheet("border-radius: 5px;"
                                    "background-color: rgb(14, 150, 232);"
                                    "color: white;")

        self.btnAbrir2 = QPushButton("3ro", self)
        self.btnAbrir2.move(170, 190)
        self.btnAbrir2.resize(150, 30)
        self.btnAbrir2.setFont(QFont("Comic Sans MS", 12))
        self.btnAbrir2.clicked.connect(self.open)
        self.btnAbrir2.setStyleSheet("border-radius: 5px;"
                                    "background-color: rgb(14, 150, 232);"
                                    "color: white;")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LvlStudent()
    window.show()
    sys.exit(app.exec_())