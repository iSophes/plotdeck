from PySide6.QtWidgets import QHBoxLayout, QStatusBar, QVBoxLayout, QWidget

from core.main_window import Window
from ui.bottom_bar import bottom_bar
from ui.center.center_layout import CenterColumn
from ui.left_column import left_column
from ui.top_bar.top_bar import TopBar


class main_ui(QWidget):
    def __init__(self, window: Window):
        super().__init__()
        self._top_bar: TopBar = TopBar(window)
        self._left_column: left_column.LeftColumn = left_column.LeftColumn()
        self._center_layout: CenterColumn = CenterColumn()
        self._window: Window = window

        main_layout: QHBoxLayout = QHBoxLayout(self)
        main_layout.setContentsMargins(5, 5, 5, 5)
        main_layout.setSpacing(0)

        self.create_footer()
        main_layout.addWidget(self._left_column)
        main_layout.addWidget(self._center_layout, 1)
        window.setCentralWidget(self)

    def create_footer(self):
        footer: bottom_bar = bottom_bar()
        status_bar: QStatusBar = QStatusBar()
        status_bar.setSizeGripEnabled(False)
        status_bar.addWidget(footer.widget, 1)
        self._window.setStatusBar(status_bar)
