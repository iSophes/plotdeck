from enum import Enum

from PySide6.QtWidgets import QPushButton

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
        _ = self.button.clicked.connect(self.click)

    def click(self):
        if self.type == PlaybackButtonType.PANIC:
            app_track_handler.panic_all_tracks()
