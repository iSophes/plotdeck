import vlc


class AudioHandler:
    def __init__(self):
        self._instance: vlc.Instance = vlc.Instance()
        self._player = self._instance.media_player_new()
        self._media: vlc.Media

    def init_media(self, path: str):  # god i love vlc media with it's zero types
        self._media: vlc.Media = self._instance.media_new(path)
        self._player.set_media(self._media)

    def resume_media(self):
        self._player.play()

    def pause_media(self):
        self._player.pause()

    def stop_media(self):
        self._player.stop()
        self._player.set_media(None)
