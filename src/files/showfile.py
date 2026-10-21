# create and load showfiles
import json

from PySide6.QtWidgets import QFileDialog

from core.error_popup import error_popup
from tracks.track_handler import app_track_handler

LOADED_FILE_DIRECTORY = ""

JSON_ENCODER = json.JSONEncoder()


def get_showfile():
    return QFileDialog.getOpenFileNames(
        None,
        "Import Files",
        "",
        "Plotdeck Files (*.plotdeck)",
    )


def handle_decoded_file(data):
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

        app_track_handler.add_track(file["path"], index)
        continue

    return True


def open_showfile():
    showfile, _ = get_showfile()
    if not showfile:
        return False

    for file in showfile:
        with open(file) as f:
            try:
                loaded = json.load(f)
                LOADED_FILE_DIRECTORY = showfile
                return handle_decoded_file(loaded)

            except json.JSONDecodeError:
                error_popup("Failed to decode file!")
                return False

            except (OSError, UnicodeDecodeError) as e:
                error_popup(f"Failed to read file: {e}")


def encode_tracks():
    dict: dict[str, bool | list[dict[str, str | list[str]]]] = {
        "com.isophes.plotdeck.valid_showfile": True,
        "files": [],
    }

    for track in app_track_handler.get_tracks():
        encoded_track = {
            "path": track.get_path(),
            "cues": track.get_cues(),
            "description": track.get_description(),
        }

        dict["files"].append(encoded_track)

    return JSON_ENCODER.encode(dict)


def save_showfile():
    encoded = encode_tracks()

    print(encoded)

    if LOADED_FILE_DIRECTORY == "":
        # prompt to save a new file
        return

    # save new file
