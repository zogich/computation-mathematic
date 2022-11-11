from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QHBoxLayout, QWidget
from pyqt_app.lab_forms.first_lab_form import FirstLabForm


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.__init_ui()

    def __init_ui(self):
        self.box_layout = QHBoxLayout()

        central_widget = QWidget()

        first_lab_button = QPushButton('Выполнить лабораторную 1')
        first_lab_button.clicked.connect(self.__open_form_for_first_lab)

        lbl2 = QPushButton('Выполнить лабораторную 2')

        self.box_layout.addWidget(first_lab_button)
        self.box_layout.addWidget(lbl2)

        central_widget.setLayout(self.box_layout)

        self.setCentralWidget(central_widget)

        self.setWindowTitle("My App")

        self.setWindowTitle('Absolute')
        self.show()

    def __open_form_for_first_lab(self):
        first_lab_form = FirstLabForm()
        first_lab_form.exec()