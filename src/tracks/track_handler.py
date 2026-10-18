from PySide6.QtWidgets import QFileDialog

from core import state
from core.audio import AudioHandler
from core.signal import Signal
from tracks.track import Track

TRACK_ADDED: Signal[[Track, int]] = Signal()


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
        self._audio_handler: AudioHandler = AudioHandler()
        self.playing: Track | None = None
        self.is_paused: bool = True

        _ = state.selection.changed.connect(lambda _track: self.stop())

    def get_tracks(self):
        return self._tracks

    def add_track(self, path: str, index: int | None = None):
        if any(track.get_path() == path for track in self._tracks):
            return

        if index is None:
            index = len(self._tracks)
        index = max(0, min(index, len(self._tracks)))

        track = Track(path)
        self._tracks.insert(index, track)
        TRACK_ADDED.fire(track, index)

    def play_track(self, track: Track):
        if self.playing is not track:
            track.init_track(self._audio_handler)

        track.resume_track(self._audio_handler)
        self.playing = track
        self.is_paused = False

    def pause_track(self):
        self.is_paused = True
        self._audio_handler.pause_media()

    def stop(self):
        self.playing = None
        self.is_paused = True
        self._audio_handler.stop_media()

    def panic_all_tracks(self):
        state.selection.clear()
        self.stop()

    def import_tracks(self):
        tracks = GetTrackFiles()
        if not tracks:
            return

        usable_tracks = tracks[0]

        for track in usable_tracks:
            self.add_track(track)


app_track_handler = TrackHandler()
