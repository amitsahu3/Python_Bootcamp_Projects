from bs4 import BeautifulSoup
import requests

# spotify password for amit.9993013869@gmail.com, Amiti$9999


# Scraping the billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
billboard_url = "https://www.billboard.com/charts/hot-100"
response = requests.get(url=f"{billboard_url}/{date}/")
billboard_webpage = response.text
soup = BeautifulSoup(billboard_webpage, 'html.parser')
songs = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in songs]


# spotify authetication

# spotify credenials
client_id = "cc823fb148aa49d68644c0beaa8ee96c"
client_secret = "d3b69c71d0cc4c7ebeb20caf9f9395a8"

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username="amit",
    )
)
user_info = sp.current_user()
user_id = user_info["id"]

# searching spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


# creating a private playlist and getting back the playlist id after its creation
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
pl_id = playlist['id']
# adding songs to that playlist
sp.playlist_add_items(playlist_id=pl_id, items=song_uris)
