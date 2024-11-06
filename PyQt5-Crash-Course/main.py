import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("qtcrashcourse2.ui",self)

        # Button
        self.button.clicked.connect(self.buttonclicked)

        # Check Box
        self.checkBox.stateChanged.connect(self.checked)

        # Combo Box
        self.comboBox.setVisible(False)
        listocc=["engineer", "doctor", "manager"]
        for job in listocc:
            self.comboBox.addItem(job)
        self.comboBox.currentIndexChanged.connect(self.combochanged)

        # Spin Box
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(10)
        self.spinBox.valueChanged.connect(self.spinchanged)
