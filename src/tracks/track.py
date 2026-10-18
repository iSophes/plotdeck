from core.audio import AudioHandler


class Track:
    def __init__(self, path: str):
        self._path: str = path
        self._cues: dict[str, int] = {}  # cue type, ms of track

    def get_path(self):
        return self._path

    def init_track(self, audio_handler: AudioHandler):
        audio_handler.init_media(self._path)

    def resume_track(self, audio_handler: AudioHandler):
        audio_handler.resume_media()

    def pause_track(self, audio_handler: AudioHandler):
        audio_handler.pause_media()

    def add_cue(self, type: str, time: int):
        self._cues[type] = time
