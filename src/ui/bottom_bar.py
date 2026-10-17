from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QSizePolicy, QWidget

from ui.set_font import set_inter


class bottom_bar:
    def __init__(self):
        self.widget: QWidget = QWidget()
        self.widget.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        self.widget.setFixedHeight(30)

        self.box: QHBoxLayout = QHBoxLayout(self.widget)
        self.box.setSpacing(0)
        self.box.setContentsMargins(10, 0, 10, 0)

        self._version_text: QLabel = self._make_label(
            "v0.1.0 ALPHA", Qt.AlignmentFlag.AlignLeft
        )
        self.loaded_text: QLabel = self._make_label(
            "PlotDeck | Nothing Loaded", Qt.AlignmentFlag.AlignCenter
        )
        self._love: QLabel = self._make_label(
            "PlotDeck | Nothing Loaded", Qt.AlignmentFlag.AlignRight
        )

        self.widget.setLayout(self.box)

    def _make_label(self, text: str, h_align: Qt.AlignmentFlag) -> QLabel:
        label = QLabel(text)
        label.setAlignment(h_align | Qt.AlignmentFlag.AlignVCenter)
        set_inter(label)

        self.box.addWidget(label, 1)
        return label
