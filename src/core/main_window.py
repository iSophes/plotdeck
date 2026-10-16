# This code was ripped from ShowDeck (A Level CS Project)
# The exam board requires MANY comments, so here we are.

from PySide6 import QtWidgets
from qt_material import apply_stylesheet

DEFAULT_WIDTH = 1200
DEFAULT_HEIGHT = 800


class Window(QtWidgets.QWidget):
    def __init__(self, app: QtWidgets.QApplication):
        super().__init__()  # Initialise the super class
        self.main_layout: QtWidgets.QHBoxLayout = QtWidgets.QHBoxLayout(
            self
        )  # Main layout is a Horizontal Box

        self.resize(
            DEFAULT_WIDTH, DEFAULT_HEIGHT
        )  # Resize the window to default width and height
        self.setWindowTitle("PlotDeck")  # Set window title to project name
        apply_stylesheet(app, theme="dark_teal.xml")  # Give it a material theme
        self.setLayout(self.main_layout)  # Make our program follow the main layout
        self.show()  # Show our window
        self.showMaximized()  # Maximise it
