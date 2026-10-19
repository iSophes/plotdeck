from enum import Enum
from operator import indexOf

from PySide6.QtWidgets import QPushButton

from core import state
from tracks import track_handler
from tracks.track import Track
from tracks.track_handler import app_track_handler


class PlaybackButtonType(
    Enum
):  # Create an enum which only allows us to use these types of buttons.
    RESTART = 1
    PREVIOUS = 2
    NEXT = 3
    PANIC = 4


class SquareButton:  # it makes a square button... what did you expect?
    def __init__(
        self, type: PlaybackButtonType
    ):  # Forces type to be one specified in our enum.
        self.button: QPushButton = QPushButton(type.name)  # create a button
        self.button.setFixedSize(100, 100)  # change size of button
        self.type: PlaybackButtonType = type
        self._default_style: str = self.button.styleSheet()
        self.disable()
        _ = state.selection.changed.connect(self.update_select_state)
        _ = self.button.clicked.connect(self.click)

    def click(self):
        if self.type == PlaybackButtonType.RESTART:
            track_handler.app_track_handler.restart()

        if self.type == PlaybackButtonType.PREVIOUS:
            current_selection = state.selection.track
            app_track_handler.panic_all_tracks()
            tracks = app_track_handler.get_tracks()
            track_index = indexOf(tracks, current_selection)
            next_track_index = track_index - 1
            if track_index == 0:
                next_track_index = len(tracks) - 1
            state.selection.select(tracks[next_track_index])
            app_track_handler.play_track(tracks[next_track_index])

        if self.type == PlaybackButtonType.NEXT:
            current_selection = state.selection.track
            app_track_handler.panic_all_tracks()
            tracks = app_track_handler.get_tracks()
            track_index = indexOf(tracks, current_selection)
            next_track_index = track_index + 1
            if track_index == len(tracks) - 1:
                next_track_index = 0
            state.selection.select(tracks[next_track_index])
            app_track_handler.play_track(tracks[next_track_index])

        if self.type == PlaybackButtonType.PANIC:
            app_track_handler.panic_all_tracks()

    def update_select_state(self, selected: Track | None):
        if selected is not None:
            self.enable()
        else:
            self.disable()

    def enable(self):
        self.button.setEnabled(True)
        self.button.setStyleSheet(self._default_style)

    def disable(self):
        self.button.setEnabled(False)
        self.button.setStyleSheet(
            f"{self._default_style}\nQPushButton: {{border: 2px solid #555555; background-color: #30343B; color: #555555 }}"
        )
