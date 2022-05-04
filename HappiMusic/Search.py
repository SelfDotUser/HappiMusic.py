"""
The Search module for the Happi Music API wrapper.

This helps users conveniently search the Happi Music API.
"""
from .Album import Album, create_album
from .Artist import Artist, create_artist
from .Track import Track, create_track
from .Lyrics import get_lyrics
from .KeyHelper import key
import requests


class SearchedTrack:
    def __init__(self, **kwargs):
        self._kwargs = dict(kwargs)
        self.name: str = kwargs.pop("name", None)
        self.id: int = kwargs.pop("id", None)
        self.hasLyrics: bool = kwargs.pop("hasLyrics", None)
        self.bpm: float = kwargs.pop("bpm", None)
        self.lang: str = kwargs.pop("lang", None)
        self.cover: str = kwargs.pop("cover", None)

    def artist(self) -> Artist:
        return create_artist(self._kwargs["artist_id"])

    def album(self) -> Album:
        return create_album(self._kwargs["artist_id"], self._kwargs['album_id'])

    def track(self) -> Track:
        return create_track(self._kwargs["artist_id"], self._kwargs['album_id'], self.id)

    def lyrics(self) -> str:
        return get_lyrics(self._kwargs['lyrics_api'])

    def __bool__(self):
        return True if self.id is not None else False

    def __repr__(self):
        c = "SearchedTrack("

        for k, v in self._kwargs.items():
            c += f"{k}='{v}', " if type(v) is str else f"{k}={v}, "
        if len(self._kwargs) != 0:
            c = c[:-2] + ")"
        else:
            c += ")"
        return c

    def __str__(self):
        return "" if len(self._kwargs) == 0 else self.name

    def __eq__(self, other):
        assert type(other) in (Track, SearchedTrack, int), "SearchedTrack.__eq__: Equality only works on int, Track, " \
                                                           f"or SearchedTrack, not '{type(other)}'."

        if type(other) in (Track, SearchedTrack):
            return True if other.id == self.id else False
        else:
            return True if self.id == other else False


class SearchedArtist:
    def __init__(self, **kwargs):
        self._kwargs = kwargs
        self.name = kwargs.pop("name", None)
        self.id: int = kwargs.pop('id', None)
        self.cover: str = kwargs.pop('cover', None)

    def api(self) -> Artist:
        return create_artist(self.id)

    def __bool__(self):
        return True if self.id is not None else False

    def __repr__(self):
        c = "SearchedArtist("

        for k, v in self._kwargs.items():
            c += f"{k}='{v}', " if type(v) is str else f"{k}={v}, "
        if len(self._kwargs) != 0:
            c = c[:-2] + ")"
        else:
            c += ")"
        return c

    def __str__(self):
        return "" if len(self._kwargs) == 0 else self.name

    def __eq__(self, other):
        assert type(other) in (Track, SearchedArtist, int), f"SearchedArtist.__eq__: Equality only works on int, " \
                                                            f"Artist, or SearchedArtist, not '{type(other)}'."

        if type(other) in (Track, SearchedArtist):
            return True if other.id == self.id else False
        else:
            return True if self.id == other else False


def search_artist(q: str, limit=5, lyrics=False) -> list[SearchedArtist]:
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


def search_track(q: str, limit=5, lyrics=False) -> list[SearchedTrack]:
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
