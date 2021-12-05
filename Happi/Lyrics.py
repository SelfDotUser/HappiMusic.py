import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_lyrics(link):
    response = requests.get(link,
                            headers={"x-happi-key": os.getenv("API_KEY")})

    return response.json()['result']['lyrics']
