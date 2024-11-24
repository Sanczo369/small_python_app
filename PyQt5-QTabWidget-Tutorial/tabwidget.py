import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTabWidget, QWidget

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("tabtutorial.ui",self)
        self.tabWidget.currentChanged.connect(self.tabChanged)
        self.change.clicked.connect(self.changeTabText)
        self.insert.clicked.connect(self.insertTab)
        self.remove.clicked.connect(self.removeTab)

    def tabChanged(self):
        print("Tab was changed to ", self.tabWidget.currentIndex())


    def changeTabText(self):
        self.tabWidget.setTabText(0, "First tab")
        self.tabWidget.setTabText(1, "Second tab")
