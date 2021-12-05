def from_web_to_data(data):
    for thing in data:
        print(f"'': data['{thing}'],")


def from_data_to_object(data):
    for thing in data:
        print(f"self.{thing}: str = kwargs.pop('{thing}', None)")

data = {'id': ['id_track'],
        'name': ['track'],
        'artist': ['artist'],
        'album': ['album'],
        'bpm': ['bpm'],
        'lang': ['lang'],
        'hasLyrics': ['haslyrics'],
        'track_api': ['api_track'],
        'lyrics_api': ['api_lyrics']}

from_data_to_object(data)
