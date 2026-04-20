# Side bar that shows plots (shown as their file, but will refer to the plot object)
from math import floor

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

    def populate(self):
        box_height = 40
        available = self.scroller.viewport().height()

        if available == self._lastAvailable:
            return
        
        while self.baseContainerLayout.count():
            self.baseContainerLayout.takeAt(0).widget().deleteLater()

        self._lastAvailable = available

        count = max(len(self.getPlots()), floor(available / (box_height + 4)))

        even = False
        for i in range(count):
            shouldHover = self.getPlots()[i] if i < len(self.getPlots()) else False
            button = QPushButton(self.getPlots()[i] if i < len(self.getPlots()) else "")
            button.setFixedHeight(box_height)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            button.setStyleSheet(
                f"QPushButton {{ color: #ffffff; background-color: {"#495158" if even else "#343c44"}; border-width: 0; }} {shouldHover and "QPushButton:hover {{ background-color: #485158; }}"}"
            )
            self.baseContainerLayout.addWidget(button)
            even = not even

    def __init__(self):
        super().__init__()

        self.scroller = QScrollArea()
        self.scroller.setWidgetResizable(True)
        self.scroller.setFixedWidth(420)
        self.scroller.resizeEvent = lambda e: (super(QScrollArea, self.scroller).resizeEvent(e), self.populate())
        self._plots = []
        self._lastAvailable = 0
        
        self.baseContainer = QFrame()

        self.baseContainerLayout = QVBoxLayout(self.baseContainer)
        self.baseContainerLayout.setSpacing(5)
        self.baseContainerLayout.setContentsMargins(5, 4, 5, 4)

        self.scroller.setWidget(self.baseContainer)
        self.populate()
