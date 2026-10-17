from core.main_window import Window
from ui.bottom_bar import bottom_bar
from ui.left_column import left_column


class main_ui:
    def __init__(self, window: Window):
        left_side = left_column.LeftColumn()
        footer = bottom_bar()

        window.main_layout.addLayout(footer.box)
        window.main_layout.addLayout(left_side.layout)
