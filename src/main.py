import sys

from PySide6 import QtWidgets

from core import main_window
from core.vlc_checker import check_vlc
from tracks.track_handler import TrackHandler
from ui.main_ui import main_ui


def main():
    if not check_vlc():  # We need VLC before anything!
        return

    app = QtWidgets.QApplication([])  # Begin!
    app_window = main_window.Window(app)

    _main_ui = main_ui(app_window)
    app_track_handler = TrackHandler()
    app_track_handler.add_track("A")
    app_track_handler.add_track("B")
    app_track_handler.add_track("C", 1)
    app_track_handler.add_track("D")
    app_track_handler.add_track("E", 1)
    app_track_handler.add_track("F", 1)

    sys.exit(app.exec())  # Close the app when we want it to close.


if __name__ == "__main__":
    main()
