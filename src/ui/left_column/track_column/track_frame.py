from PySide6.QtWidgets import (
    QFrame,
    QScrollArea,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from core import state
from tracks.track import Track
from ui.left_column.track_column.track_option import TrackOption


class TrackFrame(QWidget):
    def __init__(self):
        super().__init__()

        self.scroller: QScrollArea = QScrollArea()
        self.scroller.setWidgetResizable(True)
        self.scroller.setFixedWidth(420)

        self.base_container: QFrame = QFrame(self.scroller)
        self.base_container.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )

        self.base_container_layout: QVBoxLayout = QVBoxLayout(self.base_container)
        self.base_container_layout.setSpacing(5)
        self.base_container_layout.addStretch(1)

        self.options: list[tuple[Track, TrackOption]] = []

        self.scroller.setWidget(self.base_container)

        _ = state.selection.changed.connect(self.show_selection)

    def add_option(self, track: Track, index: int):
        option = TrackOption(track.get_path(), index % 2 == 0)
        _ = option.button.clicked.connect(lambda: state.selection.select(track))
        self.options.insert(index, (track, option))

        self.base_container_layout.insertWidget(index, option)

    def show_selection(self, selected: Track | None):
        for track, option in self.options:
            option.select_option(track is selected)
