import random
import sys

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    r = Signal(bool, int)

    def __init__(self):
        super().__init__()
        btn = QPushButton("Press me")
        btn.setCheckable(True)
        btn.clicked.connect(self.button_clicked)

        self.r.connect(self.funct)
        self.setCentralWidget(btn)

    def button_clicked(self, checked):
        self.r.emit(checked, random.randint(0, 10))

    def funct(self, button_state, random_number):
        print(button_state, random_number)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
