from PySide6.QtCore import Qt
from PySide6.QtGui import QWindow
from PySide6.QtWidgets import QHBoxLayout, QStatusBar, QVBoxLayout, QWidget

from core.main_window import Window
from tracks.track_handler import TrackHandler
from ui.bottom_bar import bottom_bar
from ui.left_column import left_column
from ui.top_bar.top_bar import TopBar


class main_ui(QWidget):
    def __init__(self, window: Window, track_handler: TrackHandler):
        super().__init__()
        self._top_bar: TopBar = TopBar(window, track_handler)
        self._left_column: left_column.LeftColumn = left_column.LeftColumn()
        self._window: Window = window

        main_layout: QVBoxLayout = QVBoxLayout(self)
        main_layout.setContentsMargins(5, 5, 5, 5)
        main_layout.setSpacing(0)

        self.create_footer()
        main_layout.addWidget(self._left_column)
        window.setCentralWidget(self)

    def create_footer(self):
        footer: bottom_bar = bottom_bar()
        status_bar: QStatusBar = QStatusBar()
        status_bar.setSizeGripEnabled(False)
        status_bar.addWidget(footer.widget, 1)
        self._window.setStatusBar(status_bar)
