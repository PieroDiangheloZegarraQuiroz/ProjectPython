from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QScrollArea, QVBoxLayout, QFormLayout, \
    QGroupBox, QDialog

from Connection import ConnectionDB


class ShowStudentFive(QDialog):
    def __init__(self, code):
        super(ShowStudentFive, self).__init__()
        self.code = str(code)
        self.initialize()

    def initialize(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet("background-color: white;")
        self.setGeometry(550, 250, 510, 650)
        self.move(650, 150)
        self.setWindowTitle("Alumnos 5to Primaria")
        self.display_widgets()

    def display_widgets(self):

        formLayout = QFormLayout()
        groupBox = QGroupBox()

        results, quantity = ConnectionDB.Connection().listStudent5(self.code)

        self.labelNames = QLabel(f"Nombres\t\tApellidos", self)
        self.labelNames.setFont(QFont("Comic Sans MS", 10, QFont.Bold))

        self.labelEmails = QLabel("Emails")
        self.labelEmails.setFont(QFont("Comic Sans MS", 10, QFont.Bold))

        self.labelLine = QLabel("______________________________________________________________________")
        formLayout.addRow(self.labelNames, self.labelEmails)
        formLayout.addRow(self.labelLine)
        formLayout.setVerticalSpacing(0)

        self.names = []
        for n in range(quantity):
            self.names.append(results[n][0])

        self.surnames = []
        for k in range(quantity):
            self.surnames.append(results[k][1])
        #
        self.emails = []
        for d in range(quantity):
            self.emails.append(results[d][3])
        #
        self.varNames = []
        for i in range(quantity):
            self.varNames.append(f'labName{i + 1}')

        self.varEmails = []
        for i in range(quantity):
            self.varEmails.append(f'labEmail{i + 1}')

        for i in range(quantity):
            self.varNames = QLabel(f'{self.names[i]}\t\t{self.surnames[i]}', self)
            self.varNames.setFont(QFont("Comic Sans MS", 10))
            self.varNames.move(30, 50 * (i + 1))

            self.varEmails = QLabel(f'{self.emails[i]}', self)
            self.varEmails.setFont(QFont("Comic Sans MS", 10))
            self.varEmails.move(30, 50 * (i + 1))

            formLayout.setContentsMargins(30, 10, 5, 5)
            formLayout.setHorizontalSpacing(80)
            formLayout.setVerticalSpacing(20)

            formLayout.addRow(self.varNames, self.varEmails)
            formLayout.setAlignment(Qt.AlignCenter)

        groupBox.setLayout(formLayout)

        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)

        layout = QVBoxLayout(self)
        layout.addWidget(scroll)
