from PySide6.QtGui import Qt
from PySide6.QtWidgets import QVBoxLayout, QWidget

from ui.center.description_box import DescriptionBox
from ui.center.name_box import NameBox


class CenterColumn(QWidget):
    def __init__(self):
        super().__init__()
        self.dock_layout: QVBoxLayout = QVBoxLayout(self)

        self._name_box: NameBox = NameBox()
        self._description_box: DescriptionBox = DescriptionBox()

        self.dock_layout.addWidget(self._name_box)
        self.dock_layout.addWidget(self._description_box)
        self.dock_layout.setAlignment(
            Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter
        )
