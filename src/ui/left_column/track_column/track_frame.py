from PySide6.QtWidgets import (
    QFrame,
    QScrollArea,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

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

        self.scroller.setWidget(self.base_container)

    def add_option(self, track: str, index: int | None = None):
        using_index = len(self.options) if index is None else index
        option = TrackOption(track, using_index % 2 == 0)
        self.options.insert(using_index, option)

        # remove the existing stretch (always the last item) if there is one
        layout = self.base_container_layout
        if layout.count() > len(self.options) - 1:
            _ = layout.takeAt(layout.count() - 1)

        layout.insertWidget(using_index, option)
        layout.addStretch(1)
