from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget

from core.main_window import Window
from tracks.track_handler import TrackHandler
from ui.bottom_bar import bottom_bar
from ui.left_column import left_column
from ui.top_bar.top_bar import TopBar


class main_ui(QWidget):
    def __init__(self, window: Window, track_handler: TrackHandler):
        super().__init__()
        self._top_bar: TopBar = TopBar(window, track_handler)
        self._left_side: left_column.LeftColumn = left_column.LeftColumn()
        self._footer: bottom_bar = bottom_bar()

        main_layout: QVBoxLayout = QVBoxLayout(self)
        main_layout.setContentsMargins(5, 5, 5, 5)
        main_layout.setSpacing(0)

        self.widget_layout: QHBoxLayout = QHBoxLayout()
        self.widget_layout.addLayout(self._left_side.layout, stretch=2)

        main_layout.addLayout(self.widget_layout, stretch=1)
        main_layout.addLayout(self._footer.box)

        window.setCentralWidget(self)
