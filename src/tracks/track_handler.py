from PySide6.QtWidgets import QFileDialog

from core import state
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
        self._audio_handler: AudioHandler = AudioHandler()
        self.playing_track: int | None = False
        self.is_paused: bool = True

        _ = state.update_selected_cue.connect(self.panic_all_tracks)

    def get_tracks(self):
        return self._tracks

    def add_track(self, path: str, index: int):
        if path in self._paths:
            return

        index = min(int(index), len(self._tracks))
        self._tracks.insert(index, Track(path))
        self._paths.insert(index, path)
        CREATE_TRACK_SIGNAL.fire(path)

    def play_track(self, track_id: int):
        if track_id > len(self._tracks):
            return

        track: Track = self._tracks[track_id]

        if not track.initialised:
            track.init_track(self._audio_handler)

        track.resume_track(self._audio_handler)
        self.playing_track = track_id
        self.is_paused = False

    def panic_all_tracks(self, _=1):
        self.playing_track = None
        self.is_paused = True

        state.update_selected_cue.fire(-1)
        for track in self._tracks:
            track.initialised = False

        self._audio_handler.stop_media()

    def pause_track(self):
        self.is_paused = True
        self._audio_handler.pause_media()

    def import_tracks(self):
        tracks = GetTrackFiles()
        if not tracks:
            return

        usable_tracks = tracks[0]

        for track in usable_tracks:
            self.add_track(track, 0)


app_track_handler = TrackHandler()
