import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import Qt
from random import randint
from PyQt5.QtGui import QPainter, QPen, QColor


class MyWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.flag = False

    def run(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw(self.qp)
            self.qp.end()

    def draw(self, qp):
        pn = QPen(Qt.yellow)
        self.qp.setPen(pn)
        x = randint(50, 300)
        y = randint(50, 200)
        k = randint(0, 100)
        self.qp.drawEllipse(x, y, k, k)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
