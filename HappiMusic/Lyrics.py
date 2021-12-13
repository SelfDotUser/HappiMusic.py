"""
The Lyrics object for the Happi Music API wrapper.
"""
from .KeyHelper import key
import requests


def get_lyrics(link) -> str:
    response = requests.get(link,
                            headers={"x-happi-key": key})

    return response.json()['result']['lyrics']
