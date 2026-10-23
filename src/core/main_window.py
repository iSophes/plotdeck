# This code was ripped from ShowDeck (A Level CS Project)
# The exam board requires MANY comments, so here we are.

from PySide6 import QtWidgets
from qt_material import apply_stylesheet

DEFAULT_WIDTH = 1200
DEFAULT_HEIGHT = 800


class Window(QtWidgets.QMainWindow):
    def __init__(self, app: QtWidgets.QApplication):
        super().__init__()  # Initialise the super class

        self.resize(
            DEFAULT_WIDTH, DEFAULT_HEIGHT
        )  # Resize the window to default width and height
        self.setWindowTitle("PlotDeck")  # Set window title to project name
        apply_stylesheet(app, theme="dark_teal.xml")  # Give it a material theme

        app.setStyleSheet(
            app.styleSheet()
            + """
            QTextEdit, QPlainTextEdit {
                border: none;
                border-bottom: 2px solid #5a5a5a;
                border-radius: 0px;
                padding-left: 12px;
                color: #ffffff;
                background: #232629;
            }

            QTextEdit:focus, QPlainTextEdit:focus {
                border-bottom: 2px solid #1de9b6;
                color: #ffffff
            }

            QPlainTextEdit:disabled {
                background: #232629
            }
        """
        )

        self.show()  # Show our window
        self.showMaximized()  # Maximise it
