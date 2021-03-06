from PySide6.QtWidgets import QLabel, QDialogButtonBox, QVBoxLayout, QDialog


class exit_window(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Elige una opción")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Estás seguro que quieres salir?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
