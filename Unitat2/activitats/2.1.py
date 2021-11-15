import sys
from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("La meua aplicacio")
        self.setFixedSize(800, 400)
        self.button = QPushButton("Aceptar", self)
        self.toolButtonStyle()
        self.setStyleSheet("background-color : yellow")
        self.setCentralWidget(self.button)
        self.button.clicked.connect(self.clickme)

    def clickme(self):
        print("pressed")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
