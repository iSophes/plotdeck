from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QFrame,
    QSizePolicy,
    QLabel,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from ui.plotsExplorer import plotExplorer
import fileHandler
import sys

def set_z_order(widget, order: str):
    """order: 'raise', 'lower', or int index"""
    if order == "raise":
        widget.raise_()
    elif order == "lower":
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
        self.goButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pauseButton.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.pauseButton.setFocus()
        print("GO!")

    def Reset(self):
        self.goButton.setFocus()
        self.goButton.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.pauseButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        print("RESET!")

    def PressPause(self):
        self.isPaused = not self.isPaused
        self.pauseButton.setText(self.isPaused and "PLAY" or "PAUSE")
        
    def requestFiles(self):
        fileHandler.ImportFiles(self, self.explorer)

    def exit(self):
        sys.exit(0)

    def __init__(self, parentWindow):
        super().__init__()

        self.isPaused = False

        # Layouts to position everything nicely
        self.mainLayout = QVBoxLayout(self)
        self.setLayout(self.mainLayout)

        self.footerBox = QHBoxLayout()
        self.footerBox.setContentsMargins(0, 0, 0, 0)
        self.footerBox.setSpacing(0)

        self.leftWidget = QVBoxLayout()
        self.actionsSection = QHBoxLayout()
        self.tracksSection = QVBoxLayout()
        self.mainLayout.addLayout(self.leftWidget)
        self.mainLayout.addLayout(self.footerBox)

        # Topbar

        self.topbar = parentWindow.menuBar()
        self.topbar.setStyleSheet(self.topbar.styleSheet() + """ \
            QMenu::item:selected {
                background-color: #646c75;
            }
                                  
            QMenuBar::item:selected {
                background-color: #646c75;
            }
        """)

        fileMenu = self.topbar.addMenu("&File")

        newProject = QAction("New Project", parentWindow)
        openProject = QAction("Open Project", parentWindow)

        importTrack = QAction("Import Track", parentWindow)
        importTrack.triggered.connect(self.requestFiles)
        
        settings = QAction("Settings", parentWindow)

        exit = QAction("Exit", parentWindow)
        exit.triggered.connect(self.exit)

        fileMenu.addAction(newProject)
        fileMenu.addAction(openProject)
        fileMenu.addSeparator()
        fileMenu.addAction(importTrack)
        fileMenu.addSeparator()
        fileMenu.addAction(settings)
        fileMenu.addSeparator()
        fileMenu.addAction(exit)

        # Our main buttons

        self.goButton = QPushButton(parent=self, text="GO")
        existing_style = self.goButton.styleSheet()
        self.goButton.setStyleSheet(
            existing_style + "font-size: 100pt; font-family: Inter;"
        )
        self.goButton.setFixedSize(420, 175)
        self.goButton.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.goButton.clicked.connect(self.PressGo)

        # Action buttons under go

        self.pauseButton = QPushButton(parent=self, text="Pause")
        self.pauseButton.setStyleSheet(existing_style + "font-size: 13pt;")
        self.pauseButton.setFixedSize(100, 100)
        self.pauseButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pauseButton.pressed.connect(self.PressPause)

        self.restartButton = QPushButton(parent=self, text="Restart")
        self.restartButton.setStyleSheet(
            existing_style + "font-size: 13pt; padding-left: 4pt; padding-right: 4pt;"
        )
        self.restartButton.setFixedSize(100, 100)
        self.restartButton.setContentsMargins(0, 0, 0, 0)
        self.restartButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.skipButton = QPushButton(parent=self, text="Skip")
        self.skipButton.setStyleSheet(existing_style + "font-size: 13pt;")
        self.skipButton.setFixedSize(100, 100)
        self.skipButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.resetButton = QPushButton(parent=self, text="Reset")
        self.resetButton.setStyleSheet(existing_style + "font-size: 13pt;")
        self.resetButton.setFixedSize(100, 100)
        self.resetButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.resetButton.clicked.connect(self.Reset)


        # Side bar with plots

        self.explorer = plotExplorer()

        # Footer

        self.footerBar = QFrame()
        self.footerBar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.footerBar.setFixedHeight(30)

        self.footerBox.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.footerBox.addWidget(self.footerBar)

        self.innerFooterBox = QHBoxLayout()
        self.innerFooterBox.setContentsMargins(10, 0, 10, 0)
        self.footerBar.setLayout(self.innerFooterBox)
        self.innerFooterBox.setAlignment(
            Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignLeft
        )

        self.version = QLabel("V0.0.1")
        self.innerFooterBox.addWidget(self.version)
        self.innerFooterBox.addStretch()
        self.version.setMinimumHeight(20)
        self.version.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.version.setStyleSheet(self.version.styleSheet() + "font-family: Inter")

        self.middleText = QLabel("Nothing Open")
        self.innerFooterBox.addWidget(self.middleText)
        self.innerFooterBox.addStretch()
        self.middleText.setAlignment(
            Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter
        )
        self.middleText.setMinimumHeight(20)
        self.middleText.setStyleSheet(
            self.middleText.styleSheet() + "font-family: Inter"
        )

        self.madeWithLove = QLabel("Made with ❤️ by Sophie")
        self.innerFooterBox.addWidget(self.madeWithLove)
        self.madeWithLove.setMinimumHeight(20)
        self.madeWithLove.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.madeWithLove.setStyleSheet(
            self.madeWithLove.styleSheet() + "font-family: Inter"
        )

        self.actionsSection.addWidget(self.restartButton)
        self.actionsSection.addWidget(self.pauseButton)
        self.actionsSection.addWidget(self.skipButton)
        self.actionsSection.addWidget(self.resetButton)

        self.leftWidget.addWidget(self.goButton)
        self.leftWidget.addLayout(self.actionsSection)
        self.leftWidget.addWidget(self.explorer.scroller)

        self.leftWidget.setAlignment(
            Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft
        )
        self.actionsSection.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.tracksSection.setAlignment(Qt.AlignmentFlag.AlignLeft)
