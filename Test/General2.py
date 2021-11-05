from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Python ")

        self.setGeometry(100, 100, 400, 600)

        self.UiComponents()

        self.show()

    def UiComponents(self):

        # button = QPushButton("Set time(s)", self)
        #
        # button.setGeometry(125, 100, 150, 50)
        #
        # button.clicked.connect(self.get_seconds)

        self.label = QLabel("//TIMER//", self)

        self.label.setGeometry(100, 200, 200, 50)

        self.label.setStyleSheet("border : 3px solid black")

        self.label.setFont(QFont('Times', 15))

        self.label.setAlignment(Qt.AlignCenter)

        start_button = QPushButton("Start", self)

        start_button.setGeometry(125, 350, 150, 40)



        self.count = 200
        self.start = False
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(100)
        start_button.clicked.connect(self.start_action)

    def showTime(self):
        if self.start:
            self.count -= 1
            if self.count == 0:
                self.start = False
                self.label.setText("Completed !!!! ")
        if self.start:
            text = str(self.count / 10) + " s"
            self.label.setText(text)

    def start_action(self):
        self.start = True
        if self.count == 0:
            self.start = False


App = QApplication(sys.argv)

window = Window()

sys.exit(App.exec())
