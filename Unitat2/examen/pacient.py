import re
import sys

from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QVBoxLayout,
    QWidget, QSpinBox, QDoubleSpinBox, QPushButton, )


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")
        self.widget = QWidget()
        layout = QVBoxLayout(self.widget)

        # Nom
        nom_text = QLabel(self.widget)
        nom_text.setText("Nom:")
        self.nom = QLineEdit(self.widget)
        layout.addWidget(nom_text)
        layout.addWidget(self.nom)
        self.nom.textChanged.connect(self.valida_nom)

        # DNI
        dni_text = QLabel(self.widget)
        dni_text.setText("DNI:")
        self.dni = QLineEdit(self.widget)
        layout.addWidget(dni_text)
        self.dni.textChanged.connect(self.valida_dni)
        layout.addWidget(self.dni)

        # Sexe
        sexe_text = QLabel(self.widget)
        sexe_text.setText("Sexe:")
        self.sexe = QComboBox()
        self.sexe.addItems(["Mascul·lí", "Femení", "Indeterminat"])
        self.sexe.setCurrentText("Indeterminat")

        layout.addWidget(sexe_text)
        layout.addWidget(self.sexe)

        # Edat
        edat_text = QLabel(self.widget)
        edat_text.setText("Edat:")
        self.edat = QComboBox()
        self.edat.addItems(["0-10", "10-20", "20-30", "30-40", "40-50", "60-70", "70-80", "80-90", "90-100", ])
        layout.addWidget(edat_text)
        layout.addWidget(self.edat)

        # Altura
        altura_text = QLabel(self.widget)
        altura_text.setText("Altura:")
        self.altura = QSpinBox()
        self.altura.setRange(40, 220)
        self.altura.setSuffix("cm")
        layout.addWidget(altura_text)
        layout.addWidget(self.altura)

        # Pes
        pes_text = QLabel(self.widget)
        pes_text.setText("Pes:")
        self.pes = QDoubleSpinBox()
        self.pes.setRange(2, 125)
        self.pes.setSuffix("kg")
        layout.addWidget(pes_text)
        layout.addWidget(self.pes)

        # Boto
        self.registrar = QPushButton()
        self.registrar.setText("Registrar")
        layout.addWidget(self.registrar)
        self.registrar.setEnabled(False)
        self.registrar.clicked.connect(self.pressed_button)
        self.setCentralWidget(self.widget)

    def pressed_button(self):
        file = open("registre.txt", "a")
        file.write(self.nom.text() + "\n")
        file.write(self.dni.text() + "\n")
        file.write(self.sexe.currentText() + "\n")
        file.write(self.edat.currentText() + "\n")
        file.write(self.altura.text() + "\n")
        file.write(self.pes.text() + "\n")
        file.write("\n")
        self.nom.setText("")
        self.dni.setText("")
        self.sexe.setCurrentText("Indeterminat")
        self.edat.setCurrentText("0-10")
        self.altura.setValue(40)
        self.pes.setValue(2)
        file.close()

    def valida_nom(self):
        length = self.nom.text().split(" ")
        i = 0
        i2 = 0
        if len(length) >= 2:
            for nombre in length[0]:
                i += 1
            for apellido in length[1]:
                i2 += 1
            if i >= 2 and i2 >= 2:
                self.registrar.setEnabled(True)
        else:
            self.registrar.setEnabled(False)

    def valida_dni(self):
        if re.match('\d{8}[a-zA-Z]$', self.dni.text()):
            self.registrar.setEnabled(True)
        else:
            self.registrar.setEnabled(False)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
