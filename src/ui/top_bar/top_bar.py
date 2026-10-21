from PySide6.QtGui import QAction

from core.main_window import Window
from files import showfile
from files.showfile import open_showfile
from tracks.track_handler import app_track_handler


class TopBar:
    def __init__(self, window: Window):
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

        save_file = QAction("Save Showfile", parent=window)
        file_menu.addAction(save_file)
        _ = save_file.triggered.connect(self.save_showfile)

        save_as = QAction("Save Showfile As", parent=window)
        file_menu.addAction(save_as)
        _ = save_as.triggered.connect(self.save_showfile_as)

    def import_track(self):
        app_track_handler.import_tracks()

    def load_showfile(self):
        _ = open_showfile()

    def save_showfile(self):
        showfile.save_showfile(False)

    def save_showfile_as(self):
        showfile.save_showfile(True)
