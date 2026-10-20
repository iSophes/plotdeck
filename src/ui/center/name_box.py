from PySide6.QtWidgets import QLabel


class NameBox(QLabel):
    def __init__(self):
        super().__init__()
        self.setText("File Name")
        self.setStyleSheet(
            self.styleSheet()
            + f"""QLabel {{ border: none;
        border-bottom: 2px solid #5a5a5a;
        border-radius: 0px;
        padding-left: 12px;
        background: #232629;
        color: rgba(255,255,255,0.5); }}
        """
        )

        self.setFixedHeight(50)

    def unselect_file(self):
        self.setText("File Name")
        self.setStyleSheet(
            self.styleSheet() + f"""QLabel {{color: rgba(255,255,255,0.5); }} """
        )
