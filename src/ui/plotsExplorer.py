# Side bar that shows plots (shown as their file, but will refer to the plot object)
from PySide6.QtWidgets import (
    QWidget,
    QScrollArea,
    QVBoxLayout,
    QPushButton,
    QFrame,
    QSizePolicy,
)


class plotExplorer(QWidget):
    def getPlots(self):
        return self._plots

    def __init__(self):
        super().__init__()

        self.scroller = QScrollArea()
        self.scroller.setWidgetResizable(True)
        self.scroller.setFixedWidth(420)
        self._plots = []

        self.baseContainer = QFrame()

        self.baseContainerLayout = QVBoxLayout(self.baseContainer)

        self.scroller.setWidget(self.baseContainer)

        even = False
        for i in range(22):
            button = QPushButton("")
            button.setFixedHeight(40)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            currentStyle = button.styleSheet()
            button.setStyleSheet(
                currentStyle
                + f"QPushButton {{ color: #ffffff; background-color: {'#4E4E4E' if even else '#484848'}; border-width: 0; text-transform: none; }} QPushButton:hover {{ background-color: #666666; }}"
            )
            self.baseContainerLayout.addWidget(button)
            even = not even
