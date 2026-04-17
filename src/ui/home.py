from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QFrame, QSizePolicy, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

def set_z_order(widget, order: str):
    """order: 'raise', 'lower', or int index"""
    if order == 'raise':
        widget.raise_()
    elif order == 'lower':
        widget.lower()
    elif isinstance(order, int):
        parent = widget.parent()
        if parent:
            siblings = parent.children()
            siblings.remove(widget)
            siblings.insert(order, widget)
            for w in siblings:
                w.raise_()

class home(QWidget):
    def PressGo(self):
        print("GO!")

    def __init__(self):
        super().__init__()
        
        # Layouts to position everything nicely
        self.mainLayout = QVBoxLayout(self);
        self.setLayout(self.mainLayout)
        
        self.footerBox = QHBoxLayout();
        self.footerBox.setContentsMargins(0, 0, 0, 0)
        self.footerBox.setSpacing(0)

        self.leftWidget = QVBoxLayout();
        self.actionsSection = QHBoxLayout();
        self.tracksSection = QVBoxLayout();
        self.mainLayout.addLayout(self.leftWidget)
        self.mainLayout.addLayout(self.footerBox)
        
        # Our main buttons

        self.goButton = QPushButton(parent=self, text="GO")
        existing_style = self.goButton.styleSheet()
        self.goButton.setStyleSheet(existing_style + "font-size: 100pt;")
        self.goButton.setFixedSize(420, 175)
        
        # Action buttons under go

        self.pauseButton = QPushButton(parent=self, text="Pause")
        self.pauseButton.setStyleSheet(existing_style + "font-size: 13pt;")
        self.pauseButton.setFixedSize(100, 100)

        self.restartButton = QPushButton(parent=self, text="Restart")
        self.restartButton.setStyleSheet(existing_style + "font-size: 11pt;")
        self.restartButton.setFixedSize(100, 100)

        self.skipButton = QPushButton(parent=self, text="Skip")
        self.skipButton.setStyleSheet(existing_style + "font-size: 13pt;")
        self.skipButton.setFixedSize(100, 100)

        self.resetButton = QPushButton(parent=self, text="Reset")
        self.resetButton.setStyleSheet(existing_style + "font-size: 13pt;")
        self.resetButton.setFixedSize(100, 100)

        # Footer

        self.footerBar = QFrame()
        self.footerBar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.footerBar.setFixedHeight(30)

        self.footerBox.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.footerBox.addWidget(self.footerBar)

        self.innerFooterBox = QHBoxLayout()
        self.innerFooterBox.setContentsMargins(10, 0, 10, 0)
        self.footerBar.setLayout(self.innerFooterBox)
        self.innerFooterBox.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignLeft)

        self.version = QLabel("V0.0.1")
        self.innerFooterBox.addWidget(self.version)
        self.innerFooterBox.addStretch()
        self.version.setMinimumHeight(20)
        self.version.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.version.setFont(QFont("Inter", 10))

        self.middleText = QLabel("Nothing Open")
        self.innerFooterBox.addWidget(self.middleText)
        self.innerFooterBox.addStretch()
        self.middleText.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
        self.middleText.setMinimumHeight(20)
        self.middleText.setFont(QFont("Inter", 10))

        self.madeWithLove = QLabel("Made with ❤️ by Sophie")
        self.innerFooterBox.addWidget(self.madeWithLove)
        self.madeWithLove.setMinimumHeight(20)
        self.madeWithLove.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.madeWithLove.setFont(QFont("Inter", 12))

        self.actionsSection.addWidget(self.restartButton)
        self.actionsSection.addWidget(self.pauseButton)
        self.actionsSection.addWidget(self.skipButton)
        self.actionsSection.addWidget(self.resetButton)

        self.leftWidget.addWidget(self.goButton)
        self.leftWidget.addLayout(self.actionsSection)
        self.leftWidget.addLayout(self.tracksSection)
        
        self.leftWidget.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        self.actionsSection.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.tracksSection.setAlignment(Qt.AlignmentFlag.AlignLeft)


