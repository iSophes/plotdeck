from PySide6.QtGui import QAction

from core.main_window import Window
from files.showfile import open_showfile
from tracks.track_handler import TrackHandler


class TopBar:
    def __init__(self, window: Window, track_handler: TrackHandler):
        self._track_handler: TrackHandler = track_handler
        menu_bar = window.menuBar()

        menu_bar.setStyleSheet(
            menu_bar.styleSheet()
            + """ \
            QMenu::item:selected {
                background-color: #646c75;
            }

            QMenuBar::item:selected {
                background-color: #646c75;
            }


        """
        )

        file_menu = menu_bar.addMenu("&File")

        load_track_action = QAction("Load Track", parent=window)
        _ = load_track_action.triggered.connect(self.import_track)
        file_menu.addAction(load_track_action)

        load_showfile_action = QAction("Open Showfile", parent=window)
        file_menu.addAction(load_showfile_action)
        _ = load_showfile_action.triggered.connect(self.load_showfile)

    def import_track(self):
        self._track_handler.import_tracks()

    def load_showfile(self):
        _ = open_showfile(self._track_handler)
