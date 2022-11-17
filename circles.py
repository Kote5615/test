from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5.QtCore import Qt
from PyQt5 import uic
from random import randint


class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.pushButton.clicked.connect(self.circle)

        self.label = QLabel()
        canvas = QPixmap(600, 600)
        self.label.setPixmap(canvas)

        layout = QGridLayout(self.centralwidget)
        layout.addWidget(self.pushButton, 0, 0, alignment=Qt.AlignCenter)
        layout.addWidget(self.label, 1, 0)

    def circle(self):
        r = randint(10, 500)
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(*[248, 243, 43]))
        painter.setPen(pen)
        painter.drawEllipse(randint(10, 500), randint(10, 500), r, r)
        painter.end()
        self.update()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = Test()
    w.show()
    sys.exit(app.exec_())
# https://github.com/Kote5615/test.git