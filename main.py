import random
import sys

from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.flag = False
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw_yellow_circles(qp)
            qp.end()

    def run(self):
        self.flag = True
        self.repaint()

    def draw_yellow_circles(self, qp):
        x = random.randint(110, 450)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(100, 100, x, x)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
