import os
from dotenv import load_dotenv
import requests

if not os.path.exists(".env"):
    print("The '.env' file was not found. Let's fix that!")

    potential_key = input('Paste your API key here: ')

    print("Testing key...")
    response = requests.get("https://api.happi.dev/v1/music/artists/116148/albums/3220879/tracks/19656780",
                            params={"id_artist": "116148", "id_album": "3220879", "id_track": "19656780"},
                            headers={"x-happi-key": potential_key})

    if response.json()['success']:
        f = open(".env", "w")
        f.write(f"API_KEY={potential_key}")
        f.close()

        print("Great, it works! Back to our regularly scheduled program!")
    else:
        raise Exception("The key looks to be invalid. :(")
load_dotenv()

key = os.getenv("API_KEY")
