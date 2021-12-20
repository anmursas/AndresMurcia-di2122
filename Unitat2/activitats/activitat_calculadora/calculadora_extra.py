import os.path
import sys

from PySide6.QtGui import QAction, QKeySequence, QFont, Qt, QIcon, QPixmap
from PySide6.QtWidgets import QMainWindow, QWidget, QStackedLayout, QVBoxLayout, QStatusBar, QLabel, QLineEdit, \
    QGridLayout, QPushButton, QFileDialog, QApplication

from exit_window import exit_window


class calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora Estándar")

        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        # Variables
        self.line = ""
        self.file = ""

        # Stacked Layout
        self.stacked_layout = QStackedLayout(self.main_widget)

        # Estándar
        self.estandar = QWidget()
        self.estandar_layout = QVBoxLayout(self.estandar)
        self.estandar.setLayout(self.estandar_layout)
        self.stacked_layout.addWidget(self.estandar)

        # Científica
        self.cient = QWidget()
        self.cient_layout = QVBoxLayout(self.cient)
        self.cient.setLayout(self.cient_layout)
        self.stacked_layout.addWidget(self.cient)

        # Menú
        main_menu = self.menuBar()

        # Menu con los modos
        _menu = main_menu.addMenu("&Menú")
        mode = _menu.addMenu("Modo")

        # Botón de cambiar a estándar
        estandar_btn = QAction("&Estándar", self)
        estandar_btn.setShortcut(QKeySequence("Ctrl+e"))
        estandar_btn.triggered.connect(self.to_estandar)
        mode.addAction(estandar_btn)

        # Botón de cambiar a científica
        cient_btn = QAction("&Científica", self)
        cient_btn.setShortcut(QKeySequence("Ctrl+q"))
        cient_btn.triggered.connect(self.to_cient)
        mode.addAction(cient_btn)

        _menu.addSeparator()

        # Boton de autoguardado
        self.saving_true = os.path.join(os.path.dirname(__file__), "res/saving.png")
        self.saving_false = os.path.join(os.path.dirname(__file__), "res/not_saving.png")
        self.saving = QAction(QIcon(self.saving_false), "Saving", self)
        self.saving.setShortcut(QKeySequence("Ctrl+g"))
        self.saving.setCheckable(True)
        self.saving.triggered.connect(self.save)
        _menu.addAction(self.saving)

        _menu.addSeparator()

        # Salir de la aplicación
        salir = QAction("Salir", self)
        salir.setShortcut(QKeySequence("Ctrl+w"))
        salir.triggered.connect(self.close)
        _menu.addAction(salir)

        # status_bar
        # modo calculadora
        self.setStatusBar(QStatusBar(self))
        self.mode = QLabel("Calc. Estándar")
        self.statusBar().addPermanentWidget(self.mode)

        # Está guardando?

        self.is_saving = QLabel()
        self.is_saving.setPixmap(QPixmap(self.saving_false))
        self.statusBar().addPermanentWidget(self.is_saving)

        # Calculadora estándar
        # Pantalla donde se muestran nuestras operaciones
        self.estandar_line = QLineEdit()
        self.estandar_line.setFont(QFont('Arial', 20))
        self.estandar_line.setReadOnly(True)
        self.estandar_line.setAlignment(Qt.AlignRight)
        self.estandar_layout.addWidget(self.estandar_line)

        # El layout para los botones
        layout_botones_estandar = QGridLayout()
        self.estandar_buttons = {
            '√': (0, 0),
            'π': (0, 1),
            '**': (0, 2),
            '<=': (0, 3),
            '(': (1, 0),
            ')': (1, 1),
            '%': (1, 2),
            '/': (1, 3),
            '7': (2, 0),
            '8': (2, 1),
            '9': (2, 2),
            '*': (2, 3),
            '4': (3, 0),
            '5': (3, 1),
            '6': (3, 2),
            '+': (3, 3),
            '1': (4, 0),
            '2': (4, 1),
            '3': (4, 2),
            '-': (4, 3),
            '.': (5, 0),
            '0': (5, 1),
            'CE': (5, 2),
            '=': (5, 3),
        }

        # Posicionamos los botones
        for btn in self.estandar_buttons.keys():
            button = QPushButton(btn)
            button.setFont(QFont('Arial', 15))
            button.setStyleSheet("background-color: black; color: white")
            button.setShortcut(btn)
            button.setStatusTip(btn)
            layout_botones_estandar.addWidget(button, self.estandar_buttons[btn][0], self.estandar_buttons[btn][1])
            if btn == "<=":
                button.setShortcut("Backspace")
            button.clicked.connect(self.build)

        self.estandar_layout.addLayout(layout_botones_estandar)

        # Calculadora científica
        # Pantalla donde se muestran nuestras operaciones
        self.cient_line = QLineEdit()
        self.cient_line.setFont(QFont('Arial', 20))
        self.cient_line.setReadOnly(True)
        self.cient_line.setAlignment(Qt.AlignRight)
        self.cient_layout.addWidget(self.cient_line)

        # El layout para los botones
        layout_botones_cient = QGridLayout()
        self.cient_buttons = {
            '√': (0, 0),
            'π': (0, 1),
            '**': (0, 2),
            '<=': (0, 3),
            'sin': (0, 4),
            '(': (1, 0),
            ')': (1, 1),
            '%': (1, 2),
            '/': (1, 3),
            'cos': (1, 4),
            '7': (2, 0),
            '8': (2, 1),
            '9': (2, 2),
            '*': (2, 3),
            'tan': (2, 4),
            '4': (3, 0),
            '5': (3, 1),
            '6': (3, 2),
            '+': (3, 3),
            'log': (3, 4),
            '1': (4, 0),
            '2': (4, 1),
            '3': (4, 2),
            '-': (4, 3),
            '!': (4, 4),
            '.': (5, 0),
            '0': (5, 1),
            'CE': (5, 2),
            '=': (5, 3),
            '|x|': (5, 4),
        }

        # Posicionamos los botones
        for btn in self.cient_buttons.keys():
            button = QPushButton(btn)
            button.setFont(QFont('Arial', 15))
            button.setStyleSheet("background-color: black; color: white")
            button.setShortcut(btn)
            button.setStatusTip(btn)
            layout_botones_cient.addWidget(button, self.cient_buttons[btn][0], self.cient_buttons[btn][1])
            if btn == "<=":
                button.setShortcut("Intro")
            button.clicked.connect(self.build)
        self.cient_layout.addLayout(layout_botones_cient)

    # Función que cambia el layout al de la calculadora estándar
    def to_estandar(self):
        self.stacked_layout.setCurrentIndex(0)
        self.mode.setText("Calc. Estándar")

    # Función que cambia el layout al de la calculadora científica
    def to_cient(self):
        self.stacked_layout.setCurrentIndex(1)
        self.mode.setText("Calc. Científica")

    # Función que cierra la aplicación
    def closeEvent(self, event):
        out = exit_window(self)
        if not out.exec():
            event.ignore()

    # Funcion para guardar
    def save(self):
        if self.saving.isChecked():
            self.saving.setIcon(QIcon(self.saving_true))
            self.is_saving.setPixmap(QPixmap(self.saving_true))
            var = QFileDialog(self)
            self.file, temp = var.getOpenFileName()
        else:
            self.saving.setIcon(QIcon(self.saving_false))
            self.is_saving.setPixmap(QPixmap(self.saving_false))

    # Funcion que crea la operacion
    def build(self):
        if self.sender().text() == '=':
            if self.saving.isChecked():
                try:
                    result = str(eval(self.line))
                    total = self.line + '=' + result
                    self.line = result
                    self.change_text(self.line)
                    with open(self.file, 'a') as f:
                        f.write(total + "\n")
                except Exception:
                    result = "ERROR"
                    self.line = ""
                    self.change_text(result)
            else:
                try:
                    result = str(eval(self.line))
                    self.line = result
                    self.change_text(self.line)
                except Exception:
                    result = "ERROR"
                    self.line = ""
                    self.change_text(result)

        elif self.sender().text() == '<=':
            self.change_text(self.line[:-1])
            self.line = self.line[:-1]
        elif self.sender().text() == 'CE':
            self.line = ""
            self.change_text(self.line)
        else:
            self.line += self.sender().text()
            self.change_text(self.line)

    # Cambia el texto de la pantalla
    def change_text(self, text):
        self.estandar_line.setText(text)
        self.cient_line.setText(text)


app = QApplication(sys.argv)
window = calculadora()
window.show()
app.exec()
