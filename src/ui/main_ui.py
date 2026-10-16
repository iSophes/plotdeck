from core.main_window import Window
from ui.bottom_bar import bottom_bar


class main_ui:
    def __init__(self, window: Window):
        footer = bottom_bar()

        window.main_layout.addLayout(footer.box)
