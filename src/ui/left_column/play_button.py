from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QPainter, QPixmap
from PySide6.QtWidgets import QPushButton

from core import state
from tracks.track import Track
from tracks.track_handler import TRACK_ADDED, TRACK_PLAYING, app_track_handler


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
        self.button.setEnabled(False)
        self.button.setIconSize(QSize(128, 128))
        self.button.setFixedSize(420, 175)  # make it a decent size
        self.button.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.playIcon: QIcon = QIcon()
        self.pauseIcon: QIcon = QIcon()

        self.playIcon.addPixmap(
            QPixmap("src/icons/play.svg"), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.playIcon.addPixmap(
            make_greyed(QPixmap("src/icons/play_disabled.svg")),
            QIcon.Mode.Disabled,
            QIcon.State.Off,
        )
        self.pauseIcon.addPixmap(
            QPixmap("src/icons/pause.svg"), QIcon.Mode.Normal, QIcon.State.On
        )

        self.button.setIcon(self.playIcon)
        _ = self.button.clicked.connect(self.press_button)
        self._original_stylesheet: str = self.button.styleSheet()

        self.update_enabled(state.selection.track)
        _ = state.selection.changed.connect(self.update_enabled)

        _ = TRACK_PLAYING.connect(self.update_playing)

    def update_playing(self):
        self.button.setIcon(self.pauseIcon)

    def update_enabled(self, track: Track | None):
        if track is not None:
            self.enable()
        else:
            self.disable()

    def enable(self):
        self.button.setIcon(self.playIcon)
        self.button.setEnabled(True)
        self.button.setStyleSheet(self._original_stylesheet)

    def disable(self):
        self.button.setIcon(self.playIcon)
        self.button.setEnabled(False)

        self.button.clearFocus()
        self.button.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.button.setStyleSheet(
            self._original_stylesheet
            + "border: 2px solid #555555; background-color: #30343B; color: #555555"
        )

    def press_button(self):
        self.button.setFocus()
        self.button.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        track = state.selection.track
        if track is None:
            return

        if app_track_handler.is_paused:
            app_track_handler.play_track(track)
        else:
            self.button.setIcon(self.playIcon)
            app_track_handler.pause_track()
