from PySide6.QtWidgets import QMessageBox


def error_popup(error: str):
    dlg = QMessageBox()
    dlg.setWindowTitle("PlotDeck")
    dlg.setText(error)
    dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
    dlg.setIcon(QMessageBox.Icon.Critical)
    _ = dlg.exec()
