import sys
import csv
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor

class FirstForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect()


if __name__ == '__main__':
    app = QApplication(sys.argv)
ex = FirstForm()
ex.show()
sys.exit(app.exec())
