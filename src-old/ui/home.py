import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon, QPainter, QPixmap
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

import fileHandler
from ui.plotsExplorer import plotExplorer


def make_greyed(pixmap):
    grey = QPixmap(pixmap.size())
    grey.fill(Qt.transparent)
    painter = QPainter(grey)
    painter.setOpacity(0.3)
    painter.drawPixmap(0, 0, pixmap)
    painter.end()
    return grey


class home(QWidget):
    def PressPlay(self):
        self.isPaused = not self.isPaused
        self.playbackButton.setFocus()
        self.playbackButton.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        print("toggle")

    def Reset(self):
        self.loadedTrack = False
        self.playbackButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        print("RESET!")

    def requestFiles(self):
        fileHandler.ImportFiles(self, self.explorer)

    def exit(self):
        sys.exit(0)

    def __init__(self, parentWindow):
        super().__init__()

        self.isPaused = True
        self.loadedTrack = False

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

        self.playbackIcon = QIcon()
        self.playbackIcon.addPixmap(
            QPixmap("src/icons/play.svg"), QIcon.Normal, QIcon.State.Off
        )
        self.playbackIcon.addPixmap(
            make_greyed(QPixmap("src/icons/play.svg")), QIcon.Disabled, QIcon.State.Off
        )
        self.playbackIcon.addPixmap(
            QPixmap("src/icons/pause.svg"), QIcon.Normal, QIcon.State.On
        )

        # Topbar

        self.topbar = parentWindow.menuBar()
        self.topbar.setStyleSheet(
            self.topbar.styleSheet()
            + """ \
            QMenu::item:selected {
                background-color: #646c75;
            }

            QMenuBar::item:selected {
                background-color: #646c75;
            }
        """
        )

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

        self.playbackButton = QPushButton(parent=self)
        self.playbackButton.setFixedSize(420, 175)
        self.playbackButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.playbackButton.setEnabled(True)
        self.playbackButton.clicked.connect(self.PressPlay)
        self.playbackButton.setCheckable(True)
        self.playbackButton.setIcon(self.playbackIcon)
        self.playbackButton.setIconSize(QSize(110, 110))

        existing_style = self.playbackButton.styleSheet()

        # Action buttons under go

        self.previousButton = QPushButton(parent=self, text="Previous")
        self.previousButton.setStyleSheet(existing_style + "font-size: 13pt;")
        self.previousButton.setFixedSize(100, 100)
        self.previousButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.previousButton.pressed.connect(self.PressPlay)

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

        self.actionsSection.addWidget(self.previousButton)
        self.actionsSection.addWidget(self.restartButton)
        self.actionsSection.addWidget(self.skipButton)
        self.actionsSection.addWidget(self.resetButton)

        self.leftWidget.addWidget(self.playbackButton)
        self.leftWidget.addLayout(self.actionsSection)
        self.leftWidget.addWidget(self.explorer.scroller)

        self.leftWidget.setAlignment(
            Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft
        )
        self.actionsSection.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.tracksSection.setAlignment(Qt.AlignmentFlag.AlignLeft)
