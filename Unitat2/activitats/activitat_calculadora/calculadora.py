import sys
from functools import partial

from PySide6.QtCore import *
from PySide6.QtWidgets import *

ERROR = "ERROR"


class calculadora(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora")
        self.setFixedSize(300, 400)

        self.g_layout = QVBoxLayout()
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.g_layout)

        self.display()
        self.buttons()

    def display(self):
        self.line = QLineEdit()

        self.line.setFixedSize(250, 100)
        self.line.setAlignment(Qt.AlignRight)

        self.line.setReadOnly(True)

        self.g_layout.addWidget(self.line)

    def buttons(self):
        self.buttons = {}
        layout_buttons = QGridLayout()

        buttons = {
            '√': (0, 0),
            'π': (0, 1),
            '^': (0, 2),
            '!': (0, 3),
            'AC': (1, 0),
            '()': (1, 1),
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
            '0': (5, 0),
            '.': (5, 1),
            'C': (5, 2),
            '=': (5, 3),
        }
        print(type(self.buttons))

        for btn, pos in buttons.items():
            self.buttons[btn] = QPushButton(btn)
            self.buttons[btn].setFixedSize(50, 50)
            layout_buttons.addWidget(self.buttons[btn], pos[0], pos[1])

        self.g_layout.addLayout(layout_buttons)

    def set_line_text(self, text):
        self.line.setText(text)
        self.line.setFocus()

    def line_text(self):
        return self.line.text()

    def clear_line(self):
        self.set_line_text("")


def evaluate(expression):
    try:
        res = str(eval(expression, {}, {}))
    except Exception:
        res = ERROR

    return res


class calc:
    def __init__(self, model, view):
        self.evaluate = model
        self.view = view

        self.connect()

    def calculate_result(self):
        res = self.evaluate(expression=self.view.line_text())
        self.view.set_line_text(res)

    def build_expression(self, prev):
        if self.view.line_text() == ERROR:
            self.view.clear_line()

        exp = self.view.line_text() + prev
        self.view.set_line_text(exp)

    def connect(self):
        for text, btn in self.view.buttons.items():
            if text not in {"=", "C"}:
                btn.clicked.connect(partial(self.build_expression, text))

        self.view.buttons["="].clicked.connect(self.calculate_result)
        self.view.line.returnPressed.connect(self.calculate_result)
        self.view.buttons["C"].clicked.connect(self.view.clear_line)


app = QApplication(sys.argv)
window = calculadora()
window.show()

model = evaluate

calc(model=model, view=window)

app.exec()
