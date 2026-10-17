from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class TrackOption(QWidget):
    def __init__(self, track: str, even: bool):
        super().__init__()

        split_path = track.split("/")
        track_name = split_path[len(split_path) - 1]

        outer_layout: QVBoxLayout = QVBoxLayout(self)
        outer_layout.setContentsMargins(0, 0, 0, 0)

        self._button: QPushButton = QPushButton("", parent=self)
        self._button.setFixedHeight(60)
        self._button.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )

        self._button.setStyleSheet(
            f"QPushButton {{ font-size: 10pt; color: #ffffff; background-color: {'#495158' if even else '#343c44'}; border-width: 0; }} QPushButton:hover {{ background-color: #8697a4; }}"
        )

        self._button_layout: QHBoxLayout = QHBoxLayout()
        self._button.setLayout(self._button_layout)

        label: QLabel = QLabel(track_name)
        label.setStyleSheet("QLabel {font-size: 10pt; color: #ffffff}")
        label.setWordWrap(True)
        self._button_layout.addWidget(label)

        outer_layout.addWidget(self._button)
