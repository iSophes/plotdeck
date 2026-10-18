from core.signal import Signal
from tracks.track import Track


class Selection:
    def __init__(self):
        self._track: Track | None = None
        self.changed: Signal[[Track | None]] = Signal()

    @property
    def track(self) -> Track | None:
        return self._track

    def select(self, track: Track | None):
        if track is self._track:
            return
        self._track = track
        self.changed.fire(track)

    def clear(self):
        self.select(None)


selection = Selection()
