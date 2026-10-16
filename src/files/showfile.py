# create and load showfiles
import json

from PySide6.QtWidgets import QFileDialog
from typing_extensions import TypedDict

from core.error_popup import error_popup
from tracks.track_handler import TrackHandler


def get_showfile():
    return QFileDialog.getOpenFileNames(
        None,
        "Import Files",
        "",
        "Plotdeck Files (*.plotdeck)",
    )


def handle_decoded_file(data, track_handler: TrackHandler):
    if not "com.isophes.plotdeck.valid_showfile" in data:
        error_popup("Not a valid showfile!")
        return False

    if not "files" in data:
        error_popup("Not a valid showfile!")
        return False

    for file in data["files"]:
        # file goes in structure
        index: int | None = None
        if "index" in file:
            index = int(file["index"])

        track_handler.add_track(file["path"], index)
        continue

    return True


def open_showfile(track_handler: TrackHandler):
    showfile, _ = get_showfile()
    if not showfile:
        return False

    for file in showfile:
        with open(file) as f:
            try:
                loaded = json.load(f)
                return handle_decoded_file(loaded, track_handler)

            except json.JSONDecodeError:
                error_popup("Failed to decode file!")
                return False

            except (OSError, UnicodeDecodeError) as e:
                error_popup(f"Failed to read file: {e}")
