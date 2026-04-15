from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt
class home(QWidget):
    def PressGo(self):
        print("GO!")

    def __init__(self):
        super().__init__()
        self.mainLayout = QHBoxLayout(self);
        self.setLayout(self.mainLayout)

        self.leftWidget = QVBoxLayout();
        self.actionsSection = QHBoxLayout();
        self.tracksSection = QVBoxLayout();

        self.mainLayout.addLayout(self.leftWidget)
        
        self.goButton = QPushButton(parent=self, text="GO")
        existing_style = self.goButton.styleSheet()
        self.goButton.setStyleSheet(existing_style + "font-size: 100pt;")
        self.goButton.setFixedSize(420, 175)

        self.pauseButton = QPushButton(parent=self, text="Pause")
        existing_style = self.pauseButton.styleSheet()
        self.pauseButton.setStyleSheet(existing_style + "font-size: 30pt;")
        self.pauseButton.setFixedSize(100, 100)

        self.leftWidget.addWidget(self.goButton)
        self.leftWidget.addLayout(self.actionsSection)
        self.leftWidget.addLayout(self.tracksSection)

        self.leftWidget.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        self.actionsSection.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.tracksSection.setAlignment(Qt.AlignmentFlag.AlignLeft)


