import sys
from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication

app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self, title="Title", button_text="Text"):
        super().__init__()
        self.setWindowTitle(title)

        button = QPushButton(button_text)
        button.show()

        self.setCentralWidget(button)


if len(sys.argv) == 3:
    window = MainWindow(sys.argv[1], sys.argv[2])
else:
    window = MainWindow()

window.show()
app.exec()
