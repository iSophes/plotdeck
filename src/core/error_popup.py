from PySide6.QtWidgets import QMessageBox


def error_popup(error: str):
    dlg = QMessageBox()
    dlg.setWindowTitle("PlotDeck")
    dlg.setText(error)
    dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
    dlg.setIcon(QMessageBox.Icon.Critical)
    _ = dlg.exec()


def unsaved_popup():
    dlg = QMessageBox()
    dlg.setWindowTitle("PlotDeck")
    dlg.setText("You have unsaved changes, do you want to save or discard them?")
    dlg.setStandardButtons(
        QMessageBox.StandardButton.Cancel
        | QMessageBox.StandardButton.Ignore
        | QMessageBox.StandardButton.Save
    )
    result = dlg.exec()
    return result
