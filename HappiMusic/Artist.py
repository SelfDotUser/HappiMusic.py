"""
This is the Artist object for the Happi Music API wrapper.
"""
from .KeyHelper import key
import requests


class Artist:
    def __init__(self, **kwargs):
        self.name: str = kwargs.pop('name', None)
        self.id: int = kwargs.pop('id', None)
        self.mbid: str = kwargs.pop('mbid', None)
        self.gender: str = kwargs.pop('gender', None)
        self.country: str = kwargs.pop('country', None)
        self.youtube: str = kwargs.pop('youtube', None)
        self.instagram: str = kwargs.pop('instagram', None)
        self.twitter: str = kwargs.pop('twitter', None)
        self.facebook: str = kwargs.pop('facebook', None)
        self.website: str = kwargs.pop('website', None)
        self.spotify: str = kwargs.pop('spotify', None)


def create_artist(artist_id: int):
    response = requests.get(f"https://api.happi.dev/v1/music/artists/{artist_id}",
                            params={"id_artist": artist_id},
                            headers={"x-happi-key": key})
    artist_data = response.json()['result']
    data = {
        "name": artist_data['artist'],
        "id": artist_data['id_artist'],
        'mbid': artist_data['mbid'],
        'gender': artist_data['gender'],
        'country': artist_data['country'],
        'youtube': artist_data['youtube'],
        'instagram': artist_data['instagram'],
        'twitter': artist_data['twitter'],
        'facebook': artist_data['facebook'],
        'website': artist_data['website'],
        'spotify': artist_data['spotify'],
        'albums_api': artist_data['api_albums']
    }

    return Artist(**data)
