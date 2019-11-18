import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QImage
from random import randint


class FirstForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self._im = QImage(self.width(), self.height(), QImage.Format_ARGB32)
        self._im.fill(QColor("white"))

        self.go = False
        self.pushButton.clicked.connect(self.draw_circle)

        self.setFixedSize(800, 800)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        painter = QPainter(self)
        painter.drawImage(0, 0, self._im)
        qp.end()

    def draw_circle(self):
        qp = QPainter(self._im)
        a = randint(10, 600)
        x, y = randint(0, 800 - a), randint(0, 800 - a)

        qp.setBrush(QColor(0, 0, 0))
        qp.drawEllipse(x - 1, y - 1, a + 2, a + 2)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(x, y, a, a)

        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
ex = FirstForm()
ex.show()
sys.exit(app.exec())
