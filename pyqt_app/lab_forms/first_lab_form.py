from PyQt6.QtWidgets import QDialog, QLineEdit, QLabel, QPushButton, QHBoxLayout


class FirstLabForm(QDialog):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        self.setLayout(layout)

        label = QLabel('Введите функцию')
        layout.addWidget(label)

        self.function_input = QLineEdit()
        layout.addWidget(self.function_input)

        self.execute_button = QPushButton('OK')
        layout.addWidget(self.execute_button)