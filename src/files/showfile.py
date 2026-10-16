# create and load showfiles
import json

from PySide6.QtWidgets import QFileDialog

from core.error_popup import error_popup


def get_showfile():
    return QFileDialog.getOpenFileNames(
        None,
        "Import Files",
        "",
        "Plotdeck Files (*.plotdeck)",
    )


def handle_decoded_file(data):
    print(data)
    return True


def open_showfile():
    showfile, _ = get_showfile()
    if not showfile:
        return False

    for file in showfile:
        with open(file) as f:
            try:
                loaded = json.load(f)
                return handle_decoded_file(loaded)

            except json.JSONDecodeError:
                error_popup("Failed to decode file!")
                return False

            except (OSError, UnicodeDecodeError) as e:
                error_popup(f"Failed to read file: {e}")
