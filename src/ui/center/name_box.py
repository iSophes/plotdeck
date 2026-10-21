from PySide6.QtWidgets import QLabel

from core import state
from tracks.track import Track


class NameBox(QLabel):
    def __init__(self):
        super().__init__()
        self.setText("File Name")
        self.setStyleSheet(
            self.styleSheet()
            + f"""QLabel {{ border: none;
        border-bottom: 2px solid #5a5a5a;
        border-radius: 0px;
        padding-left: 12px;
        background: #232629;
        color: rgba(255,255,255,0.5); }}
        """
        )

        self.setFixedHeight(50)

        _ = state.selection.changed.connect(self.selection_changed)

    def selection_changed(self, track: Track | None):
        if track is None:
            self.unselect_file()
        else:
            self.select_file(track.name)

    def unselect_file(self):
        self.setText("File Name")
        self.setStyleSheet(
            self.styleSheet() + "QLabel {color: rgba(255,255,255,0.5); } "
        )

    def select_file(self, file: str):
        self.setText(file)
        self.setStyleSheet(self.styleSheet() + "QLabel {color: rgb(255,255,255); } ")
