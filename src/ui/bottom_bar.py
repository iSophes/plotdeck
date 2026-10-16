from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QSizePolicy

from ui.set_font import set_inter


class bottom_bar:
    def __init__(self):
        self._bar = QFrame()
        self._bar.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self._bar.setFixedHeight(30)

        self.box = QHBoxLayout()
        self.box.setContentsMargins(0, 0, 0, 0)
        self.box.setSpacing(0)
        self.box.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.box.addWidget(self._bar)

        self._innerBox = QHBoxLayout()
        self._innerBox.setContentsMargins(10, 0, 10, 0)
        self._bar.setLayout(self._innerBox)
        self._innerBox.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.version_text = QLabel("v0.1.0 ALPHA")
        set_inter(self.version_text)
        self.version_text.setMinimumHeight(20)
        self.version_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.loaded_text = QLabel("PlotDeck | Nothing Loaded")
        set_inter(self.loaded_text)
        self.loaded_text.setMinimumHeight(20)
        self.loaded_text.setAlignment(
            Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter
        )

        self._love = QLabel("Made with ❤️ by Sophie")
        set_inter(self._love)
        self._love.setMinimumHeight(20)
        self._love.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._innerBox.addWidget(self.version_text)
        self._innerBox.addStretch()
        self._innerBox.addWidget(self.loaded_text)
        self._innerBox.addStretch()
        self._innerBox.addWidget(self._love)
