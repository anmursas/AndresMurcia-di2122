# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.window = self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        return loader.load(path, self)


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.window.show()
    widget.window.pushButton.setText("Adeu")
    sys.exit(app.exec())
