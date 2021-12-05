# HappiMusic.py
Welcome to the Happi Music API wrapper for Python!

---
# Authentication
The HappyMusic wrapper comes with a KeyHelper that will help you set up your API key when you first try to use the 
wrapper.<br>
Please get an API key from the [Happi website](https://happi.dev) and follow the instructions given to you in the 
terminal.
---
# Examples
### Searching for a song
```python
import HappiMusic

# Returns a list of SearchedTrack objects
songs = HappiMusic.search_track("Marina Oh No!")

for song in songs:
    # See below for the attributes of a SearchedTrack
    print(f"{song.name}'s ID is {song.id}.")
```

### Getting IDs
```python
import HappiMusic

# Returns a list of SearchedTrack objects
song = HappiMusic.search_track("Marina I Am Not a Robot", limit=1)
song = song[0]

# See below for the attributes and methods of a SearchedTrack
print(f"Song ID: {song.id}")
print(f"Album ID: {song.album().id}")
print(f"Artist ID: {song.artist().id}")
```

### Creating a Track and getting its Lyrics
```python
import HappiMusic

# IDs for Marina's "Oh No!"
song = HappiMusic.create_track(116148, 3220879, 19656780)

# See below for the methods of a Track object
lyrics = song.lyrics()
```
---
# Requirements
This project uses:
```
requests==2.25.1
python-dotenv==0.19.0
```
---
# API Documentation
Below you will find the objects available in HappiMusic, as well as their attributes and methods.

---
# Track
### Attributes
|Attribute|Type|Description|
|---|---|---|
|`name`|String|Name of the song|
|`id`|Integer|ID of the track|
|`artist_name`|String|The name of the artist.|
|`bpm`|Integer?|The beats per minute.|
|`lang`|String|Language of the song|
|`hasLyrics`|Boolean|True/False of whether or not the song has lyrics.|

### Methods
|Method|Return Type|Description|
|---|---|---|
|`lyrics()`|String|Returns a thing with the lyrics.|

---
# Artist
### Attributes
|Attribute|Type|Description|
|---|---|---|
|`name`|String|Name of the artist.|
|`id`|Integer|ID of the artist.|
|`mbid`|String|mbid of the artist.|
|`gender`|String|Gender of the artist.|
|`country`|String|Country of the artist.|
|`youtube`|String|YouTube link.|
|`instagram`|String|Instagram link.|
|`twitter`|String|Twitter link.|
|`facebook`|String|Facebook link.|
|`website`|String|Website link|
|`spotify`|String|Spotify link.|

---
# Album
### Attributes
|Attribute|Type|Description|
|---|---|---|
|`name`|String|Name of album.|
|`id`|Integer|ID of album.|
|`cover`|String|URL to the cover.|
|`upc`|String|upc of the album.|
|`asin`|String|asin of the album.|
|`mbid`|String|mbid of the album.|
|`genres`|List[String]|Genres of the album in a List.|
|`release`|String|Release date of the album.|
|`label`|String|Label of the album.|
|`explicit`|Boolean|Whether or not it's explicit.|

### Methods
|Method|Return Type|Description|
|---|---|---|
|`artist()`|Artist|Returns an Artist object of the song.|
---
# Searching
Searching using HappiMusic is, well, pretty easy.
<br>
Some things to know:
- `q: str` - The query
- `limit: int` - The amount of artists you want to get back.
- `lyrics: bool` - Whether to filter songs without lyrics.

### Methods
|Method|Return Type|Description|
|---|---|---|
|`search_artist(q, limit=5, lyrics=False)`|List[SearchedArtist]|Entering a string query (q), this returns a list of SearchedArtist for you to use.|
|`search_track(q, limit=5, lyrics=False)`|List[SearchedTrack]|Entering a string query (q), this returns a list of SearchedTrack for you to use.|
---
# SearchedTrack
### Attributes
|Attribute|Type|Description|
|---|---|---|
|`name`|String|Name of the track.|
|`id`|Integer|ID of the track.|
|`hasLyrics`|Boolean|Whether the song has lyrics or not.|
|`bpm`|Float|The BPM of the song.|
|`lang`|String|The language of the song.|
|`cover`|String|URL of the cover.|

### Methods
|Method|Return Type|Description|
|---|---|---|
|`artist()`|Artist|Returns an Artist object of the song's artist.|
|`album()`|Album|Returns an Album object of the song's album.|
|`track()`|Track|Returns a Track object of the song.|
|`lyrics()`|String|Returns a String of the song's lyrics.|
---
# SearchedArtist
### Attributes
|Attribute|Type|Description|
|---|---|---|
|`name`|String|Name of the artist.|
|`id`|Integer|ID of the artist.|
|`cover`|String|URL of the artist cover.|

### Methods
|Method|Return Type|Description|
|---|---|---|
|`api()`|Artist|Returns an Artist object of the SearchedArtist. This is to get more information.|
---
# Creating Track, Artist, Album
There's specific methods that you can use in order to create Track/Artist/Album objects without needing to search first.
<br>
Here are parameters you should know:
- `artist_id: int` - The Artist ID
- `album_id: int` - The Album ID
- `track_id: int` - The Track ID

To find these IDs, I recommend using the Search function until you find what you are looking for and get the IDs out of 
each object.

|Method|Return Type|Description|
|---|---|---|
|`create_track(artist_id, album_id, track_id)`|Track|Returns the Track object that corresponds with the IDs.|
|`create_album(artist_id, album_id)`|Album|Returns the Album object that corresponds with the IDs.|
|`create_artist(artist_id)`|Artist|Returns the Artist object that corresponds with the IDs.|