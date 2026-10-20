from PySide6.QtWidgets import QLineEdit, QWidget


class NameBox(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("File Name")
        print("-----")
        print(self.styleSheet())
        self.setFixedHeight(50)
