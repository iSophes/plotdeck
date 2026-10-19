from decimal import ROUND_HALF_UP, Decimal

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)
from tinytag import TinyTag


def split_time(time_str: str):
    # Round to 3 decimal places (exact decimal maths avoids float rounding quirks)
    total = Decimal(time_str.strip()).quantize(Decimal("0.001"), rounding=ROUND_HALF_UP)

    total_ms = int(total * 1000)
    minutes, remainder = divmod(total_ms, 60_000)
    seconds, milliseconds = divmod(remainder, 1000)

    mins_string = str(minutes)
    secs_string = str(seconds)
    ms_string = str(milliseconds)

    if seconds < 10:
        secs_string = f"0{secs_string}"

    return f"{mins_string}:{secs_string}.{ms_string}"


class TrackOption(QWidget):
    def __init__(self, track: str, even: bool):
        super().__init__()

        split_path = track.split("/")
        track_name = split_path[len(split_path) - 1]

        outer_layout: QVBoxLayout = QVBoxLayout(self)
        outer_layout.setContentsMargins(0, 0, 0, 0)

        self.button: QPushButton = QPushButton("", parent=self)
        self.button.setFixedHeight(60)
        self.button.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )

        self.button.setStyleSheet(
            f"QPushButton {{ font-size: 10pt; color: #ffffff; background-color: {'#495158' if even else '#343c44'}; border-width: 0; }} QPushButton:hover {{ background-color: #8697a4; }}"
        )

        self._base_style: str = self.button.styleSheet()

        self._button_layout: QHBoxLayout = QHBoxLayout()
        self.button.setLayout(self._button_layout)

        label: QLabel = QLabel(track_name)
        label.setStyleSheet("QLabel {font-size: 10pt; color: #ffffff}")
        label.setWordWrap(True)

        tag = TinyTag.get(track)

        length = split_time(str(tag.duration))
        lengthOfTrack = QLabel(f"{length}")
        lengthOfTrack.setStyleSheet("QLabel {font-size: 10pt; color: #ffffff}")
        lengthOfTrack.setWordWrap(True)
        lengthOfTrack.setAlignment(Qt.AlignmentFlag.AlignRight)

        self._button_layout.addWidget(label)
        self._button_layout.addSpacing(1)
        self._button_layout.addWidget(lengthOfTrack)

        outer_layout.addWidget(self.button)

    def select_option(self, enable: bool):
        self.button.setStyleSheet(
            f"{self._base_style}\nQPushButton {{ border: 3px {enable and 'solid' or 'none'} #1de9b6;}}"
        )
