from core.audio import AudioHandler
from tracks.track import Track


class TrackHandler:
    def __init__(self):
        self._tracks: list[Track] = []
        self.selected_track_id: int = 0  # track id
        self._audio_handler: AudioHandler = AudioHandler()

    def get_tracks(self):
        return self._tracks

    def add_track(self, path: str, index: int | None = None):
        if not index:
            index = len(self._tracks)

        index = min(int(index), len(self._tracks))
        self._tracks.insert(index, Track(path))

    def play_track(self, track_id: int):
        if track_id > len(self._tracks) - 1:
            return

        self._tracks[track_id].play_track(self._audio_handler)
