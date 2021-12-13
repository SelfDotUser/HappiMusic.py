"""
The Album object for the HappyMusic API wrapper.
"""
from .Artist import Artist, create_artist
from .KeyHelper import key
import requests


class Album:
    def __init__(self, **kwargs):
        self._kwargs: dict = kwargs
        self.name: str = kwargs.pop('name', None)
        self.id: int = kwargs.pop('id', None)
        self.cover: str = kwargs.pop('cover', None)
        self.upc: str = kwargs.pop('upc', None)
        self.asin: str = kwargs.pop('asin', None)
        self.mbid: str = kwargs.pop('mbid', None)
        self.genres: list = kwargs.pop('genres', None)
        self.release: str = kwargs.pop('realease', None)
        self.label: str = kwargs.pop('label', None)
        self.explicit: bool = kwargs.pop('explicit', None)

    def artist(self) -> Artist:
        return create_artist(self._kwargs.pop('artist_id', None))


def create_album(artist_id: int, album_id: int) -> Album:
    response = requests.get(f"https://api.happi.dev/v1/music/artists/{artist_id}/albums/{album_id}",
                            params={"id_artist": artist_id, "id_album": album_id},
                            headers={"x-happi-key": key})

    album_data = response.json()['result']

    data = {
        'name': album_data['album'],
        'id': album_data['id_album'],
        'artist_id': album_data['id_artist'],
        'artist': album_data['artist'],
        'cover': album_data['cover'],
        'upc': album_data['upc'],
        'asin': album_data['asin'],
        'mbid': album_data['mbid'],
        'genres': album_data['genres'],
        'realease': album_data['realease'],
        'label': album_data['label'],
        'explicit': album_data['explicit'],
        'artist_api': album_data['api_artist'],
        'albums_api': album_data['api_albums'],
        'album_api': album_data['api_album'],
        'tracks_api': album_data['api_tracks'],
    }

    return Album(**data)
