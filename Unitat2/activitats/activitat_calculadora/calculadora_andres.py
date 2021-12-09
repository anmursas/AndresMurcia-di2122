import sys
from functools import partial

from PySide6.QtGui import QFont
from PySide6.QtWidgets import QMainWindow, \
    QVBoxLayout, QWidget, QLineEdit, QGridLayout, QPushButton, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # Ventana principal
        self.setWindowTitle("Calculadora")

        # Layout general
        self.main_layout = QVBoxLayout()
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.main_layout)

        # Linea cálculo
        self.line = QLineEdit()
        self.line.setFont(QFont('Roman', 20))
        self.line.setReadOnly(True)
        self.main_layout.addWidget(self.line)

        self.crear_botones()
        self.conectar_botones()

    def crear_botones(self):
        self.buttons = {}
        layout_buttons = QGridLayout()
        # Creamos un diccionario con el texto y las coordenadas del Layout
        buttons_temp = {
            '√': (0, 0),
            'π': (0, 1),
            '**': (0, 2),
            "<<": (0, 3),
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

        # Recorrer el diccionario de botones
        # Creando un boton en cada posición asignada
        for btn, pos in buttons_temp.items():
            self.buttons[btn] = QPushButton(btn)
            self.buttons[btn].setFont(QFont('Roman', 15))
            self.buttons[btn].setStyleSheet("background-color: black; color: white")
            layout_buttons.addWidget(self.buttons[btn], pos[0], pos[1])  # Añadimos el boton con su posición

        # Añadimos el layout de botones al layout principal
        self.main_layout.addLayout(layout_buttons)

    def conectar_botones(self):
        # Recorre dict y utiliza la señal connect
        for text, boto in self.buttons.items():
            if text not in {"=", "C", "<<"}:
                boto.clicked.connect(partial(self.build, text))
        # Excepciones
        self.buttons["="].clicked.connect(self.calc)
        self.buttons["CE"].clicked.connect(self.clear)
        self.buttons["<<"].clicked.connect(self.clear_char)

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
        res = self.evaluate(self.line.text())
        self.line.setText(res)

    # Pasado el parámetro hace un eval de este
    def evaluate(self, expression):
        try:
            res = str(eval(expression))
        except Exception:
            res = "ERROR"
        return res


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
