from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import *
from Connection import ConnectionDB
import sys


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.initialize()

    def initialize(self):
        self.resize(400, 550)
        self.contador = 0
        # main button
        self.addButton = QPushButton('Agregar otra pregunta')
        self.addButton.clicked.connect(self.addWidget)

        self.saveButton = QPushButton('Subir preguntas')
        self.saveButton.clicked.connect(self.saveQuestion)

        # scroll area widget contents - layout
        self.scrollLayout = QFormLayout()

        # scroll area widget contents
        self.scrollWidget = QWidget()
        self.scrollWidget.setLayout(self.scrollLayout)

        # scroll area
        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.scrollWidget)

        # main layout
        self.mainLayout = QVBoxLayout()

        # add all main to the main vLayout
        self.mainLayout.addWidget(self.addButton)
        self.mainLayout.addWidget(self.saveButton)
        self.mainLayout.addWidget(self.scrollArea)

        # central widget
        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.mainLayout)

        # set central widget
        self.setCentralWidget(self.centralWidget)

    def addWidget(self):
        if self.contador < 10:
            self.scrollLayout.addRow(Test())
            self.contador = self.contador + 1
            print(self.contador)
        else:
            QMessageBox.warning(self, "Error",
                                "Limite excedido",
                                QMessageBox.Ok, QMessageBox.Ok)

    def saveQuestion(self):
        # save = ConnectionDB.Connection().insertQuestions()
        pass


class Test(QWidget):
    def __init__(self):
        super(Test, self).__init__()

        self.textBox = QLineEdit()
        self.textBox.resize(100, 200)

        layout = QHBoxLayout()
        layout.addWidget(self.textBox)
        self.setLayout(layout)


app = QApplication(sys.argv)
myWidget = Main()
myWidget.show()
app.exec_()
