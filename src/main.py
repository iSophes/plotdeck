from PySide6.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget
from PySide6.QtCore import QSize
from qt_material import apply_stylesheet

import shutil
import sys
import os
import platform
import webbrowser

from ui import home

# Check if we have VLC media before ANYTHING

class vlcPopupBox(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cue Plotter")
        self.resize(600, 100)

        self.setMaximumWidth(570)
        self.setMaximumHeight(100)

        self.setMinimumWidth(570)
        self.setMinimumHeight(100)

        self._setup_ui()

    def _setup_ui(self):
        self.box = temporaryBoxUI()
        self.setCentralWidget(self.box)

class temporaryBoxUI(QWidget):
    def redirect(self):
        return webbrowser.open("https://www.videolan.org/")
    
    def restart(self):
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 

    def __init__(self):
        super().__init__()

        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)

        self.subButtonLayout = QHBoxLayout()
        
        textLabel = QLabel("To run this, you need to have VLC Media Player Installed. Click below to be sent to a download link.")
        self.mainLayout.addWidget(textLabel)

        downloadButton = QPushButton(parent=self, text="Download")
        downloadButton.setFixedSize(144, 42)
        downloadButton.clicked.connect(self.redirect)
        self.subButtonLayout.addWidget(downloadButton)
        
        restartButton = QPushButton(parent=self, text="Restart")
        restartButton.setFixedSize(144, 42)
        restartButton.clicked.connect(self.restart)
        self.subButtonLayout.addWidget(restartButton)
        
        self.mainLayout.addLayout(self.subButtonLayout)

def vlc_exists():
    system = platform.system()
    paths = []
    if system == "Windows":
        paths = [
            r"C:\Program Files\VideoLAN\VLC\vlc.exe",
            r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
        ]
    elif system == "Darwin":  # macOS 
        paths = ["/Applications/VLC.app/Contents/MacOS/VLC"]
    else:  # Linux/Unix
        paths = ["/usr/bin/vlc", "/usr/local/bin/vlc"]

    return any(os.path.exists(p) for p in paths)

if not vlc_exists():
    App = QApplication(sys.argv)
    apply_stylesheet(App, "dark_teal.xml")
    box = vlcPopupBox()
    box.show()

    sys.exit(App.exec())

# Now we can run our application.

import vlc # Only import here as program will error and crash if we do not detect vlc not being there.

class app(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cue Plotter")
        screensize: QSize = (
            self.screen().size() * self.screen().devicePixelRatio()
        )

        self.resize(screensize * 0.85)
        self.showMaximized()

        self.homeScreen = home.home()
        self.setCentralWidget(self.homeScreen)

if __name__ == "__main__":
    QApp = QApplication()
    apply_stylesheet(QApp, "dark_teal.xml")
    QApp.setStyleSheet(QApp.styleSheet())
    plotterApp = app()
    plotterApp.show()

    

    sys.exit(QApp.exec())
    