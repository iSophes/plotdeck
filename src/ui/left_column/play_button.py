from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QPainter, QPixmap, Qt
from PySide6.QtWidgets import QPushButton


def make_greyed(pixmap):
    grey = QPixmap(pixmap.size())
    grey.fill(Qt.GlobalColor.transparent)
    painter = QPainter(grey)
    painter.setOpacity(0.3)
    painter.drawPixmap(0, 0, pixmap)
    _ = painter.end()
    return grey


class PlayButton:
    def __init__(self):

        self.button: QPushButton = QPushButton()
        self.playbackIcon: QIcon = QIcon()
        self.button.setIconSize(QSize(128, 128))
        self.playbackIcon.addPixmap(
            QPixmap("src/icons/play.svg"), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.playbackIcon.addPixmap(
            make_greyed(QPixmap("src/icons/play.svg")),
            QIcon.Mode.Disabled,
            QIcon.State.Off,
        )
        self.playbackIcon.addPixmap(
            QPixmap("src/icons/pause.svg"), QIcon.Mode.Normal, QIcon.State.On
        )

        self.button.setIcon(self.playbackIcon)
        self.button.setFixedSize(420, 175)  # make it a decent size
        self.button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self._original_stylesheet: str = self.button.styleSheet()

    def enable(self):
        self.button.setEnabled(True)
        self.button.setStyleSheet(self._original_stylesheet)

    def disable(self):
        self.button.setEnabled(False)
        self.button.setStyleSheet(
            self._original_stylesheet
            + "border: 2px solid #555555; background-color: #30343B; color: #555555"
        )

    def press_button(self):
        pass
