from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import config


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setFixedSize(QSize(520, 300))
        self.setWindowTitle("Exemple signals-slots 1")

        self.max = QPushButton('maxim', self)
        self.min = QPushButton('minim', self)
        self.norm = QPushButton('normal', self)

        # Connectem la senyal clicked a la ranura button_pressed
        self.max.clicked.connect(self.maximm)
        self.min.clicked.connect(self.minimm)
        self.norm.clicked.connect(self.normall)

        self.max.resize(config.BUTTON_WIDTH, config.BUTTON_HEIGHT)
        self.max.move(80, 135)

        self.min.resize(config.BUTTON_WIDTH, config.BUTTON_HEIGHT)
        self.min.move(320, 135)

        self.norm.resize(config.BUTTON_WIDTH, config.BUTTON_HEIGHT)
        self.norm.move(200, 135)

    def maximm(self):
        self.max.setEnabled(False)
        self.norm.setEnabled(True)
        self.min.setEnabled(True)
        self.setFixedSize(QSize(config.MAX_SCREEN_WIDTH, config.MAX_SCREEN_HEIGHT))
        self.max.move((config.MAX_SCREEN_WIDTH / 2) - (config.BUTTON_WIDTH * 1.5),
                      (config.MAX_SCREEN_HEIGHT / 2) - (config.BUTTON_HEIGHT / 2))
        self.norm.move((config.MAX_SCREEN_WIDTH / 2) - (config.BUTTON_WIDTH / 2),
                       (config.MAX_SCREEN_HEIGHT / 2) - (config.BUTTON_HEIGHT / 2))
        self.min.move((config.MAX_SCREEN_WIDTH / 2) + (config.BUTTON_WIDTH / 2),
                      (config.MAX_SCREEN_HEIGHT / 2) - (config.BUTTON_HEIGHT / 2))

    def minimm(self):
        self.setFixedSize(QSize(config.MIN_SCREEN_WIDTH, config.MIN_SCREEN_HEIGHT))

        self.max.setEnabled(True)
        self.norm.setEnabled(True)
        self.min.setEnabled(False)
        self.max.move((config.MIN_SCREEN_WIDTH / 2) - (config.BUTTON_WIDTH * 1.5),
                      (config.MIN_SCREEN_HEIGHT / 2) - (config.BUTTON_HEIGHT / 2))
        self.norm.move((config.MIN_SCREEN_WIDTH / 2) - (config.BUTTON_WIDTH / 2),
                       (config.MIN_SCREEN_HEIGHT / 2) - (config.BUTTON_HEIGHT / 2))
        self.min.move((config.MIN_SCREEN_WIDTH / 2) + (config.BUTTON_WIDTH / 2),
                      (config.MIN_SCREEN_HEIGHT / 2) - (config.BUTTON_HEIGHT / 2))

    def normall(self):
        self.setFixedSize(QSize(config.NORM_SCREEN_WIDTH, config.NORM_SCREEN_HEIGHT))

        self.max.setEnabled(True)
        self.norm.setEnabled(False)
        self.min.setEnabled(True)
        self.max.move((config.NORM_SCREEN_WIDTH / 2) - (config.BUTTON_WIDTH * 1.5),
                      (config.NORM_SCREEN_HEIGHT / 2) - (config.BUTTON_HEIGHT / 2))
        self.norm.move((config.NORM_SCREEN_WIDTH / 2) - (config.BUTTON_WIDTH / 2),
                       (config.NORM_SCREEN_HEIGHT / 2) - (config.BUTTON_HEIGHT / 2))
        self.min.move((config.NORM_SCREEN_WIDTH / 2) + (config.BUTTON_WIDTH / 2),
                      (config.NORM_SCREEN_HEIGHT / 2) - (config.BUTTON_HEIGHT / 2))


if __name__ == "__main__":
    app = QApplication([])

    mainWin = MainWindow()
    mainWin.show()
    app.exec()
