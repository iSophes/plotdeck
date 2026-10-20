from PySide6.QtWidgets import QTextEdit


class DescriptionBox(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(115)
        self.setPlaceholderText("Description")
        self.textChanged.connect
