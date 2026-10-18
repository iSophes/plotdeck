from PySide6.QtWidgets import QFileDialog

from core.audio import AudioHandler
from core.signal import Signal
from tracks.track import Track

CREATE_TRACK_SIGNAL = Signal()


def GetTrackFiles():
    return QFileDialog.getOpenFileNames(
        None,
        "Import Files",
        "",
        "Media (*.mp3 *.mp4 *.aac *.wav *.flac *.m4a *.ogg *.avi *.mkv *.flv *.mov)",
    )


class TrackHandler:
    def __init__(self):
        self._tracks: list[Track] = []
        self._paths: list[str] = []
        self._selected_track_id: int = 0  # track id
        self._audio_handler: AudioHandler = AudioHandler()

    def get_tracks(self):
        return self._tracks

    def add_track(self, path: str, index: int | None = None):
        if path in self._paths:
            return

        if not index:
            index = len(self._tracks)

        index = min(int(index), len(self._tracks))
        self._tracks.insert(index, Track(path))
        self._paths.insert(index, path)
        CREATE_TRACK_SIGNAL.fire(path)

        if index == 1:
            self.play_track(1)

    def play_track(self, track_id: int):
        if track_id > len(self._tracks):
            return

        self._tracks[track_id].play_track(self._audio_handler)

    def import_tracks(self):
        tracks = GetTrackFiles()
        if not tracks:
            return

        usable_tracks = tracks[0]

        for track in usable_tracks:
            self.add_track(track)

    def get_current_selection(self):
        return self._selected_track_id
