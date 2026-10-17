from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget

from ui.left_column.play_button import PlayButton
from ui.left_column.square_button import PlaybackButtonType, SquareButton


class LeftColumn:
    def __init__(self):
        self.layout: QVBoxLayout = QVBoxLayout()  # Our left column is a VBox

        self.media_layout: QHBoxLayout = QHBoxLayout()
        self.playbacks: list[SquareButton] = [
            SquareButton(PlaybackButtonType.RESTART),
            SquareButton(PlaybackButtonType.PREVIOUS),
            SquareButton(PlaybackButtonType.NEXT),
            SquareButton(PlaybackButtonType.PANIC),
        ]

        for button in self.playbacks:
            self.media_layout.addWidget(button.button)

        self.play_button: PlayButton = PlayButton()

        self.layout.addWidget(self.play_button.button)  # Put go button in
        self.layout.addLayout(self.media_layout)  # Put media controls after our HBox
        self.layout.setAlignment(
            Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft
        )  # align it where we want

        self.play_button.disable()
