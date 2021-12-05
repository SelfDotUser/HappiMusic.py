"""
The Search module for the Happi Music API wrapper.

This helps users conveniently search the Happi Music API.
"""
from .Album import create_album
from .Artist import create_artist
from .Track import create_track
from .Lyrics import get_lyrics
from .KeyHelper import key
import requests


class SearchedTrack:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.name: str = kwargs.pop("name", None)
        self.id: int = kwargs.pop("id", None)
        self.hasLyrics: bool = kwargs.pop("hasLyrics", None)
        self.bpm: float = kwargs.pop("bpm", None)
        self.lang: str = kwargs.pop("lang", None)
        self.cover: str = kwargs.pop("cover", None)

    def artist(self):
        return create_artist(self.kwargs["artist_id"])

    def album(self):
        return create_album(self.kwargs["artist_id"], self.kwargs['album_id'])

    def track(self):
        return create_track(self.kwargs["artist_id"], self.kwargs['album_id'], self.id)

    def lyrics(self):
        return get_lyrics(self.kwargs['lyrics_api'])


class SearchedArtist:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.name = kwargs.pop("name", None)
        self.id: int = kwargs.pop('id', None)
        self.cover: str = kwargs.pop('cover', None)

    def api(self):
        return create_artist(self.id)


def search_artist(q: str, limit=5, lyrics=False):
    response = requests.get(f"https://api.happi.dev/v1/music",
                            params={"q": q, "limit": limit, "lyrics": lyrics, type: "artist"},
                            headers={"x-happi-key": key})
    artist_data = response.json()['result']

    list_of_artists = []

    for i in artist_data:
        data = {
            "name": i['artist'],
            "id": i['id_artist'],
            'cover': i['cover'],
            'artist_api': i['api_artist']
        }

        list_of_artists.append(SearchedArtist(**data))

    return list_of_artists


def search_track(q: str, limit=5, lyrics=False):
    response = requests.get(f"https://api.happi.dev/v1/music",
                            params={"q": q, "limit": limit, "lyrics": lyrics, type: "track"},
                            headers={"x-happi-key": key})
    track_data = response.json()['result']

    list_of_results = []

    for i in track_data:
        data = {
            "name": i['track'],
            "id": i['id_track'],
            "hasLyrics": i['haslyrics'],
            "artist": i['artist'],
            "artist_id": i['id_artist'],
            'album': i['album'],
            'album_id': i['id_album'],
            "bpm": i['bpm'],
            "lang": i['lang'],
            "cover": i['cover'],
            "artist_api": i['api_artist'],
            'album_api': i['api_album'],
            'albums_api': i['api_albums'],
            'tracks_api': i['api_tracks'],
            'track_api': i['api_track'],
            'lyrics_api': i['api_lyrics']
        }

        list_of_results.append(SearchedTrack(**data))

    return list_of_results
