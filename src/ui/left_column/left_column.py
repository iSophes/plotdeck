from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget

from tracks import track_handler
from ui.left_column.play_button import PlayButton
from ui.left_column.square_button import PlaybackButtonType, SquareButton
from ui.left_column.track_column import track_frame


class LeftColumn(QWidget):
    def __init__(self):
        super().__init__()
        self.dock_layout: QVBoxLayout = QVBoxLayout(self)

        self.play_button: PlayButton = PlayButton()
        self.dock_layout.addWidget(self.play_button.button)  # Put go button in

        self.media_layout: QHBoxLayout = QHBoxLayout()
        self.playbacks: list[SquareButton] = [
            SquareButton(PlaybackButtonType.RESTART),
            SquareButton(PlaybackButtonType.PREVIOUS),
            SquareButton(PlaybackButtonType.NEXT),
            SquareButton(PlaybackButtonType.PANIC),
        ]

        for button in self.playbacks:
            self.media_layout.addWidget(button.button)

        self.track_frame: track_frame.TrackFrame = track_frame.TrackFrame()
        _ = track_handler.CREATE_TRACK_SIGNAL.connect(self.create_track)

        self.dock_layout.addLayout(self.media_layout)
        self.dock_layout.addWidget(self.track_frame.scroller)
        self.dock_layout.setAlignment(
            Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft
        )  # align it where we want

        self.play_button.disable()

    def create_track(self, path: str):
        self.track_frame.add_option(path, 0)
