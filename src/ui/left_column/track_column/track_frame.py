from PySide6.QtCore import QMetaObject
from PySide6.QtWidgets import (
    QFrame,
    QScrollArea,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from core import state
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

        self.options: list[TrackOption] = []
        self.click_connections: list[QMetaObject.Connection] = []

        self.scroller.setWidget(self.base_container)

    def add_option(self, track: str, index: int):
        using_index = index == 0 and len(self.options) or index
        option = TrackOption(track, using_index % 2 == 0)

        clicked = option.button.clicked.connect(lambda: self.select_track(using_index))
        self.options.insert(using_index, option)
        self.click_connections.insert(using_index, clicked)

        # remove the existing stretch (always the last item) if there is one
        layout = self.base_container_layout
        if layout.count() > len(self.options) - 1:
            _ = layout.takeAt(layout.count() - 1)

        layout.insertWidget(using_index, option)
        layout.addStretch(1)

    def select_track(self, track_index: int):
        print(track_index)
        state.updateSelectedCue(track_index)
        for i, option in enumerate(self.options):
            is_index = i == track_index
            option.select_option(is_index)
