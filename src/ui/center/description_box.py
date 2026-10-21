from PySide6.QtGui import Qt
from PySide6.QtWidgets import QPlainTextEdit

from core.state import selection
from tracks.track import Track


class DescriptionBox(QPlainTextEdit):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(115)
        self.setPlaceholderText("Description")
        self.setDisabled(True)

        selection_changed = selection.changed.connect(self.change_selection)

    def change_selection(self, track: Track | None):
        if track is None:
            self.disable()
        else:
            self.setPlainText(track.get_description())
            self.enable()

    def enable(self):
        _ = self.textChanged.connect(self.changeText)
        self.setDisabled(False)

    def disable(self):
        _ = self.textChanged.disconnect()
        self.setPlainText("")
        self.setDisabled(True)

    def changeText(self):
        track = selection.track
        if track:
            track.set_description(self.toPlainText())
