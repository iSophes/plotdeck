import os
import sys
import webbrowser
from platform import platform, system, system_alias

from PySide6 import QtCore, QtWidgets
from qt_material import apply_stylesheet

POPUP_WIDTH = 590
POPUP_HEIGHT = 130


class vlc_popup(QtWidgets.QWidget):
    def __init__(self, app):
        super().__init__()

        self.setFixedSize(POPUP_WIDTH, POPUP_HEIGHT)
        self.setWindowTitle("PlotDeck")

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.mainLayout)

        self.subButtonLayout = QtWidgets.QHBoxLayout()

        textLabel = QtWidgets.QLabel(
            "To run this, you need to have VLC Media Player Installed. Click below to be sent to a download link."
        )
        self.mainLayout.addWidget(textLabel)

        downloadButton = QtWidgets.QPushButton("Download")
        downloadButton.setFixedSize(144, 42)
        downloadButton.clicked.connect(self.redirect)
        self.subButtonLayout.addWidget(downloadButton)

        restartButton = QtWidgets.QPushButton("Restart")
        restartButton.setFixedSize(144, 42)
        restartButton.clicked.connect(self.restart)
        self.subButtonLayout.addWidget(restartButton)

        self.mainLayout.addLayout(self.subButtonLayout)

    def redirect(self):
        return webbrowser.open("https://www.videolan.org/")

    def restart(self):
        args = sys.argv[1:] if getattr(sys, "frozen", False) else sys.argv
        QtCore.QProcess.startDetached(sys.executable, args)
        QtWidgets.QApplication.quit()  # clean shutdown, no thread warnings


def vlc_exists():
    current_system: str = system()
    paths = []
    if current_system == "Windows":
        paths = [
            r"C:\Program Files\VideoLAN\VLC\vlc.exe",
            r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe",
        ]
    elif current_system == "Darwin":  # macOS
        paths = ["/Applications/VLC.app/Contents/MacOS/VLC"]
    else:  # Linux/Unix
        paths = ["/usr/bin/vlc", "/usr/local/bin/vlc"]

    return any(os.path.exists(p) for p in paths)


def check_vlc():
    if vlc_exists():
        return True

    app = QtWidgets.QApplication.instance() or QtWidgets.QApplication(sys.argv)
    apply_stylesheet(app, "dark_teal.xml")
    popup = vlc_popup(app)
    popup.show()
    sys.exit(app.exec())
