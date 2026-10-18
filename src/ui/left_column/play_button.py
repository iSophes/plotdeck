from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QPainter, QPixmap, Qt
from PySide6.QtWidgets import QPushButton

from core import state
from tracks.track_handler import app_track_handler


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
        self.button.setCheckable(True)
        self.button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.button.setIconSize(QSize(128, 128))

        self.playbackIcon: QIcon = QIcon()

        self.playbackIcon.addPixmap(
            QPixmap("src/icons/play.svg"), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.playbackIcon.addPixmap(
            make_greyed(QPixmap("src/icons/play_disabled.svg")),
            QIcon.Mode.Disabled,
            QIcon.State.Off,
        )
        self.playbackIcon.addPixmap(
            QPixmap("src/icons/pause.svg"), QIcon.Mode.Normal, QIcon.State.On
        )

        self.button.setIcon(self.playbackIcon)
        self.button.setFixedSize(420, 175)  # make it a decent size
        self.button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        _ = self.button.clicked.connect(self.press_button)
        self._original_stylesheet: str = self.button.styleSheet()

        if state.current_selected_cue != -1:
            self.enable()
        else:
            self.disable()

        _ = state.update_selected_cue.connect(self.is_track_playing)

    def is_track_playing(self, id: int):
        if id != -1:
            self.enable()
        else:
            self.disable()

    def enable(self):
        self.button.setEnabled(True)
        self.button.setStyleSheet(self._original_stylesheet)

    def disable(self):
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

        current_selection = state.current_selected_cue
        if current_selection != -1:
            if app_track_handler.is_paused:
                app_track_handler.play_track(current_selection)
            else:
                app_track_handler.pause_track()
