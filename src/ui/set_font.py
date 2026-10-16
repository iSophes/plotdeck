from PySide6.QtWidgets import QLabel


def set_inter(Label: QLabel):
    set_font(Label, "Inter")


def set_font(Label: QLabel, Font: str):
    style = Label.styleSheet()
    Label.setStyleSheet(style + f"font-family: {Font}")
