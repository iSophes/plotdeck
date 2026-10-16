import sys

from PySide6 import QtWidgets

from core import main_window
from core.vlc_checker import check_vlc


def main():
    if not check_vlc():  # We need VLC before anything!
        return

    app = QtWidgets.QApplication([])  # Begin!
    app_window = main_window.Window(app)
    sys.exit(app.exec())  # Close the app when we want it to close.


if __name__ == "__main__":
    main()
