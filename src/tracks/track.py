from core.audio import AudioHandler


class Track:
    def __init__(self, path: str):
        self._path: str = path
        self.initialised: bool = False

    def get_path(self):
        return self._path

    def init_track(self, audio_handler: AudioHandler):
        audio_handler.init_media(self._path)
        self.initialised = True

    def resume_track(self, audio_handler: AudioHandler):
        audio_handler.resume_media()

    def pause_track(self, audio_handler: AudioHandler):
        audio_handler.pause_media()
