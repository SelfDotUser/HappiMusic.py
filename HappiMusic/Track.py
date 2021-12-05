"""
The Track object for the Happi Music API wrapper.
"""
from .Lyrics import get_lyrics
from KeyHelper import key
import requests


class Track:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.id: int = kwargs.pop('id', None)
        self.name: str = kwargs.pop('name', None)
        self.artist_name: str = kwargs.pop('artist', None)
        self.album_name: str = kwargs.pop('album', None)
        self.bpm = kwargs.pop('bpm', None)
        self.lang = kwargs.pop('lang', None)
        self.hasLyrics: bool = kwargs.pop('hasLyrics', None)

    def lyrics(self):
        return get_lyrics(self.kwargs['lyrics_api'])


def create_track(artist_id: int, album_id: int, track_id: int):
    response = requests.get(f"https://api.happi.dev/v1/music/artists/{artist_id}/albums/{album_id}/tracks/{track_id}",
                            params={"id_artist": artist_id, "id_album": album_id, "id_track": track_id},
                            headers={"x-happi-key": key})
    track_data = response.json()['result']

    data = {
        'id': track_data['id_track'],
        'name': track_data['track'],
        'artist': track_data['artist'],
        'album': track_data['album'],
        'bpm': track_data['bpm'],
        'lang': track_data['lang'],
        'hasLyrics': track_data['haslyrics'],
        'track_api': track_data['api_track'],
        'lyrics_api': track_data['api_lyrics']
    }

    return Track(**data)
