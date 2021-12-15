import os.path
import sys
from functools import partial

from PySide6.QtGui import QFont, QAction, QKeySequence
from PySide6.QtWidgets import *

dir = os.path.dirname(__file__)
r = os.path.join(dir, 'historial')


class calculadora_estandar(QMainWindow):
    def __init__(self, cient=None):
        super(calculadora_estandar, self).__init__()
        self.cient = cient

        # Ventana principal
        self.setWindowTitle("Calculadora")

        # menu
        main_menu = self.menuBar()
        _menu = main_menu.addMenu("&Menu")
        mode = _menu.addMenu("Modo")

        _menu.addSeparator()

        estandar = QAction("Estándar", self)
        estandar.setShortcut(QKeySequence("Ctrl+e"))
        mode.addAction(estandar)

        mode.addSeparator()

        cientifica = QAction("Científica", self)
        cientifica.setShortcut(QKeySequence("Ctrl+q"))
        cientifica.triggered.connect(self.click)
        mode.addAction(cientifica)

        self.history = QAction("Autoguardar", self)
        self.history.setShortcut(QKeySequence("Ctrl+g"))
        self.history.setCheckable(True)
        _menu.addAction(self.history)

        _menu.addSeparator()

        quit = QAction("Salir", self)
        quit.setShortcut(QKeySequence("Ctrl+w"))
        quit.triggered.connect(self.quit)
        _menu.addAction(quit)

        # Layout general
        self.main_layout = QVBoxLayout()
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.main_layout)

        # Linea cálculo
        self.line = QLineEdit()
        self.line.setFont(QFont('Arial', 20))
        self.line.setReadOnly(True)
        self.main_layout.addWidget(self.line)
        self.buttons = {
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
        crear_botones(self)
        conectar_botones(self)

    # Deja pantalla en blanco
    def clear(self):
        self.line.setText("")

    # Elimina carácter
    def clear_char(self):
        self.line.setText(self.line.text()[:-1])

    # El boton que pulsemos se añade a la linea con el anterior
    def build(self, prev):
        if self.line.text() == "ERROR":
            self.clear()
        exp = self.line.text() + prev
        self.line.setText(exp)

    # Envía el texto a la funcion evaluate y el resultado se muestra por pantalla
    def calc(self):
        res = evaluate(self, self.line.text())
        operacion = self.line.text() + "=" + res
        self.line.setText(res)
        if self.history.isChecked():
            with open(os.path.join(r, "historial.txt"), "a+") as f:
                f.write(operacion)
                f.write("\n")

    def click(self):
        self.hide()
        if self.cient is None:
            self.cient = calculadora_cientifica(self)
        self.cient.show()

    def quit(self):
        self.close()


class calculadora_cientifica(QMainWindow):
    def __init__(self, std=None):
        super(calculadora_cientifica, self).__init__()
        # Ventana principal
        self.setWindowTitle("Calculadora")

        # menu
        main_menu = self.menuBar()
        _menu = main_menu.addMenu("&Menu")
        mode = _menu.addMenu("Modo")

        _menu.addSeparator()

        # Creamos el botón para cambiar a estándar
        estandar = QAction("Estándar", self)
        # Añadimos un atajo
        estandar.setShortcut(QKeySequence("Ctrl+e"))
        estandar.triggered.connect(self.click)
        mode.addAction(estandar)

        mode.addSeparator()

        cientifica = QAction("Científica", self)
        cientifica.setShortcut(QKeySequence("Ctrl+q"))
        mode.addAction(cientifica)

        self.history = QAction("Autoguardar", self)
        self.history.setShortcut(QKeySequence("Ctrl+g"))
        self.history.setCheckable(True)
        _menu.addAction(self.history)

        _menu.addSeparator()

        quit = QAction("Salir", self)
        quit.setShortcut(QKeySequence("Ctrl+w"))
        quit.triggered.connect(self.quit)
        _menu.addAction(quit)

        # Layout general
        self.main_layout = QVBoxLayout()
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.main_layout)

        self._std = std

        # Linea cálculo
        self.line = QLineEdit()
        self.line.setFont(QFont('Arial', 20))
        self.line.setReadOnly(True)
        self.main_layout.addWidget(self.line)
        self.buttons = {
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
        crear_botones(self)
        conectar_botones(self)

    def quit(self):
        self.close()

    # Deja pantalla en blanco
    def clear(self):
        self.line.setText("")

    # Elimina carácter
    def clear_char(self):
        self.line.setText(self.line.text()[:-1])

    # El boton que pulsemos se añade a la linea con el anterior
    def build(self, prev):
        if self.line.text() == "ERROR":
            self.clear()
        exp = self.line.text() + prev
        self.line.setText(exp)

    # Envía el texto a la funcion evaluate y el resultado se muestra por pantalla
    def calc(self):
        res = evaluate(self, self.line.text())
        operacion = self.line.text() + "=" + res
        self.line.setText(res)
        if self.history.isChecked():
            with open(os.path.join(r, "historial.txt"), "a+") as f:
                f.write(operacion)
                f.write("\n")

    def click(self):
        self.hide()
        if self._std is None:
            self._std = calculadora_estandar(self)
        self._std.show()


def crear_botones(self):
    buttons = {}
    layout_buttons = QGridLayout()
    # Creamos un diccionario con el texto y las coordenadas del Layout
    _buttons = dict

    # Recorrer el diccionario de botones
    # Creando un boton en cada posición asignada
    for btn, pos in self.buttons.items():
        self.buttons[btn] = QPushButton(btn)
        self.buttons[btn].setFont(QFont('Arial', 15))
        self.buttons[btn].setStyleSheet("background-color: black; color: white")
        self.buttons[btn].setShortcut(btn)
        # Añadimos el boton con su posición
        layout_buttons.addWidget(self.buttons[btn], pos[0], pos[1])
        if btn == "<=":
            self.buttons[btn].setShortcut(QKeySequence("DELETE"))

    # Añadimos el layout de botones al layout principal
    self.main_layout.addLayout(layout_buttons)


def conectar_botones(self):
    for text, boto in self.buttons.items():
        if text not in {"=", "C", "<="}:
            boto.clicked.connect(partial(self.build, text))
    # Excepciones
    self.buttons["="].clicked.connect(self.calc)
    self.line.returnPressed.connect(self.calc)
    self.buttons["CE"].clicked.connect(self.clear)
    self.buttons["<="].clicked.connect(self.clear_char)


# Pasado el parámetro hace un eval de este
def evaluate(self, expression):
    try:
        res = str(eval(expression))
    except Exception:
        res = "ERROR"
    return res


app = QApplication(sys.argv)
window = calculadora_estandar()
window.show()
app.exec()
