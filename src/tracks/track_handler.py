from tracks.track import Track


class TrackHandler:
    def __init__(self):
        self._tracks: list[Track] = []
        self.selected_track_id = 0  # track id

    def get_tracks(self):
        return self._tracks

    def add_track(self, path: str, index=None):
        if not index:
            index = len(self._tracks)

        index = min(index, len(self._tracks))
        self._tracks.insert(index, Track(path))
