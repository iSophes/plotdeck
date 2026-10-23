# create and load showfiles
import json

from PySide6.QtWidgets import QFileDialog

from core.error_popup import error_popup
from core.signal import Signal
from tracks.track_handler import app_track_handler

loaded_file_directory: str = ""

JSON_ENCODER = json.JSONEncoder()
FILE_LOADED = Signal()


def get_showfile():
    names = QFileDialog.getOpenFileName(
        None,
        "Import Files",
        "",
        "Plotdeck Files (*.plotdeck)",
    )

    return names[0]


def save_prompt():
    dialog = QFileDialog.getSaveFileName(
        None, "Save File As", "", "Plotdeck Files (*.plotdeck)"
    )[0]

    return dialog


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
    global loaded_file_directory

    showfile = get_showfile()
    if showfile == "":
        return False

    with open(showfile) as f:
        try:
            loaded = json.load(f)
            loaded_file_directory = showfile
            FILE_LOADED.fire()
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


def save_showfile(save_as: bool):
    global loaded_file_directory

    encoded = encode_tracks()
    file_to_save = loaded_file_directory

    if loaded_file_directory == "" or save_as == True:
        file_to_save = save_prompt()

    if file_to_save == "":
        return

    if file_to_save.find(".plotdeck") == -1:
        file_to_save = file_to_save + ".plotdeck"

    with open(
        file_to_save,
        "w",
    ) as file:
        _ = file.write(encoded)

    if loaded_file_directory == "":
        loaded_file_directory = file_to_save
        FILE_LOADED.fire()


def compare_showfiles() -> bool:  # returns true if same, returns false if not
    if loaded_file_directory == "":
        return len(app_track_handler.get_tracks()) == 0

    with open(loaded_file_directory) as f:
        return f == encode_tracks()
