import sys
import argparse
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--title", help="Title of application")
parser.add_argument("-b", "--button-text", help="Button text")
parser.add_argument("-f", "--fixed-size", action="store_true", help="Window fixed size")
parser.add_argument("-s", "--size", nargs=2, metavar=("SIZE_X", "SIZE_Y"), type=int, help="Window's size")
args = parser.parse_args()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        title, text, fixed, size_x, size_y = "APP", "Close", False, 300, 200
        if args.title:
            title = args.title
        if args.button_text:
            text = args.button_text
        if args.fixed_size:
            fixed = args.fixed_size
        if args.size:
            size_x, size_y = args.size

        self.setWindowTitle(title)
        self.setGeometry(600, 400, size_x, size_y)
        if fixed:
            self.setFixedSize(size_x, size_y)

        self.button = QPushButton(text)
        self.setCentralWidget(self.button)
        self.button.clicked.connect(QApplication.instance().quit)

        self.setCentralWidget(self.button)

        self.button.setMaximumSize(100, 25)
        self.setMaximumSize(400, 400)
        self.setMinimumSize(200, 200)

        self.button.show()
        self.show()


app = QApplication(sys.argv)

window = MainWindow()

app.exec()
