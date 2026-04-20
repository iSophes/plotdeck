# Side bar that shows plots (shown as their file, but will refer to the plot object)
from math import floor
import librosa

from PySide6.QtWidgets import (
    QWidget,
    QScrollArea,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QFrame,
    QSizePolicy,
    QLabel,
)

from PySide6.QtCore import (
    Qt
)

def get_audio_duration(file_path):
    audio_data, sample_rate = librosa.load(file_path)
    duration = librosa.get_duration(y=audio_data, sr=sample_rate)
    return duration

class plotExplorer(QWidget):
    def getPlots(self):
        return self._plots

    def setPlots(self, newPlots):
        self._plots = newPlots
        self.populate(True)

    def populate(self, override):
        box_height = 60
        available = self.scroller.viewport().height()

        if available == self._lastAvailable and not override:
            return
        
        while self.baseContainerLayout.count():
            self.baseContainerLayout.takeAt(0).widget().deleteLater()

        self._lastAvailable = available

        count = max(len(self.getPlots()), floor(available / (box_height + 4)))

        even = False
        for i in range(count):
            shouldHover = self.getPlots()[i] if i < len(self.getPlots()) else False
            if shouldHover:
                shouldHover = True # I know, it just keeps state nice as a boolean

            text = shouldHover and ((self.getPlots()[i].getName() != "" and self.getPlots()[i].getName()) or self.getPlots()[i].getTrack()) or ""
            button = QPushButton(text="")
            button.setFixedHeight(box_height)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            button.setStyleSheet(
                f"QPushButton {{ font-size: 10pt; color: #ffffff; background-color: {"#495158" if even else "#343c44"}; border-width: 0; }} {shouldHover and "QPushButton:hover { background-color: #8697a4; }"}"
            )

            even = not even

            if not shouldHover:
                self.baseContainerLayout.addWidget(button)
                continue

            buttonLayout = QHBoxLayout()
            button.setLayout(buttonLayout)

            label = QLabel(text)
            label.setStyleSheet("QLabel {font-size: 10pt; color: #ffffff}")
            label.setWordWrap(True)

            lengthOfTrack = QLabel(f"{get_audio_duration(self.getPlots()[i].getTrack()):.2f}")
            lengthOfTrack.setStyleSheet("QLabel {font-size: 10pt; color: #ffffff}")
            lengthOfTrack.setWordWrap(True)
            lengthOfTrack.setAlignment(Qt.AlignmentFlag.AlignRight, Qt.AlignmentFlag.AlignVCenter)

            buttonLayout.addWidget(label)
            buttonLayout.addSpacing(1)
            buttonLayout.addWidget(lengthOfTrack)



            self.baseContainerLayout.addWidget(button)
            

    def __init__(self):
        super().__init__()

        self.scroller = QScrollArea()
        self.scroller.setWidgetResizable(True)
        self.scroller.setFixedWidth(420)
        self.scroller.resizeEvent = lambda e: (super(QScrollArea, self.scroller).resizeEvent(e), self.populate(False))
        self._plots = []
        self._lastAvailable = 0
        
        self.baseContainer = QFrame()

        self.baseContainerLayout = QVBoxLayout(self.baseContainer)
        self.baseContainerLayout.setSpacing(5)
        self.baseContainerLayout.setContentsMargins(5, 4, 5, 4)

        self.scroller.setWidget(self.baseContainer)
        self.populate(False)
