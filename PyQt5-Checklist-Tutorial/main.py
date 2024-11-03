from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PyQt5.uic import loadUi
import sys
from qtconsole.qt import QtCore

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("main.ui", self)
        todos = ["Walk dog", "Buy groceries", "Send email", "Call bank", "Clean house"]
        for todo in todos:
            item = QListWidgetItem(todo)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.todo_listWidget.addItem(item)
        self.toggleall_button.clicked.connect(self.toggle_all)