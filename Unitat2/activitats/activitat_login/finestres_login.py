import sys

from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QWidget, QVBoxLayout, QLineEdit, QPushButton, QStatusBar
)


class WindowAdmin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admin")
        main_menu = self.menuBar()
        menu = main_menu.addMenu("&Menu")
        logout = QAction("$Tancar sessió", self)
        logout.triggered.connect(self.logout)
        menu.addAction(logout)
        menu.addSeparator()

        exit = QAction("Exit", self)
        exit.triggered.connect(self.close)
        menu.addAction(exit)

        self.widget = QWidget()
        layout = QVBoxLayout(self.widget)

        self.label = QLabel("Has entrat com administrador")
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.setStatusBar(QStatusBar(self))
        self.mode = QLabel("Admin")
        self.statusBar().addPermanentWidget(self.mode)

        self.setCentralWidget(self.widget)

    def logout(self):
        self.main = MainWindow()

        if self.main.isVisible():
            self.main.hide()
        else:
            self.hide()
            self.main.show()


class WindowUser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User")
        main_menu = self.menuBar()
        menu = main_menu.addMenu("&Menu")
        logout = QAction("$Tancar sessió", self)
        logout.triggered.connect(self.logout)
        menu.addAction(logout)
        menu.addSeparator()

        exit = QAction("Exit", self)
        exit.triggered.connect(self.close)
        menu.addAction(exit)

        self.widget = QWidget()
        layout = QVBoxLayout(self.widget)

        self.label = QLabel("Has entrat com usuari")
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.setStatusBar(QStatusBar(self))
        self.mode = QLabel("User")
        self.statusBar().addPermanentWidget(self.mode)

        self.setCentralWidget(self.widget)

    def logout(self):
        self.main = MainWindow()

        if self.main.isVisible():
            self.main.hide()
        else:
            self.hide()
            self.main.show()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        usuari = QLabel()
        usuari.setText("Usuari:")
        self.usuari_edit = QLineEdit()

        self.layout.addWidget(usuari)
        self.layout.addWidget(self.usuari_edit)

        password = QLabel()
        password.setText("Contrasenya:")
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(password)
        self.layout.addWidget(self.password_edit)

        self.login = QPushButton()
        self.login.setText("Registrar")
        self.layout.addWidget(self.login)
        self.login.clicked.connect(self.pressed_button)

        self.error = QLabel("")
        self.layout.addWidget(self.error)

        self.setLayout(self.layout)

    def pressed_button(self):
        user = self.usuari_edit.text()
        contra = self.password_edit.text()

        if user == "admin" and contra == "1234":
            self.windowAdmin = WindowAdmin()
            self.close()
            self.windowAdmin.show()
        else:
            if user == "user" and contra == "1234":
                self.windowUsers = WindowUser()
                self.close()
                self.windowUsers.show()
            else:
                self.error.setText("Credencials incorrectes")
                self.error.setStyleSheet("QLabel { color : red; }")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
