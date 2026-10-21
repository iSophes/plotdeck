from core.audio import AudioHandler


class Track:
    def __init__(self, path: str):
        self._path: str = path
        self._cues: dict[str, int] = {}  # cue type, ms of track
        self._description: str = ""
        self.name: str = path.split(
            "/"
        )[
            -1
        ].split(
            "."
        )[
            0
        ]  # theres probably some crazy regex shit for this but ive thought regex expressions is code snobbery in its purest form.

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

    def get_cues(self):
        return self._cues

    def get_description(self):
        return self._description

    def set_description(self, description: str):
        self._description = description
