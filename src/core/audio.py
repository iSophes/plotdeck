import vlc


class AudioHandler:
    def __init__(self):
        self._instance: vlc.Instance = vlc.Instance()
        self._player = self._instance.media_player_new()

    def play_media(self, path: str):  # god i love vlc media with it's zero types
        media: vlc.Media = self._instance.media_new(path)
        self._player.set_media(media)
        self._player.play()
