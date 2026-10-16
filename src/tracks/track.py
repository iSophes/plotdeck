from core.audio import AudioHandler


class Track:
    def __init__(self, path: str):
        self._path: str = path

    def get_path(self):
        return self._path

    def play_track(self, audio_handler: AudioHandler):
        audio_handler.play_media(self._path)
