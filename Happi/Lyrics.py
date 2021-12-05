from .KeyHelper import key
import requests


def get_lyrics(link):
    response = requests.get(link,
                            headers={"x-happi-key": key})

    return response.json()['result']['lyrics']
