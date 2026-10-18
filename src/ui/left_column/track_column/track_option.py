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
        self._button_layout.addWidget(label)

        outer_layout.addWidget(self.button)

    def select_option(self, enable: bool):
        self.button.setStyleSheet(
            f"{self._base_style}\nQPushButton {{ border: 3px {enable and 'solid' or 'none'} #1de9b6;}}"
        )
