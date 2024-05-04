from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# PYTHONPATH=$PWD/../
from gen_data import Data

response = requests.get("https://www.billboard.com/charts/hot-100/2000-06-16/")

# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
songs_tags = soup.find_all("h3", id="title-of-a-story", class_="a-no-trucate")
artists_tags = soup.find_all("span", class_="a-no-trucate")

song_names = [song.getText().strip() for song in songs_tags]
artists_names = [artist.getText().strip() for artist in artists_tags]

access_data = Data().get()["app"]
spotify_client_id = access_data[2]["api_key"]
spotify_client_secret = access_data[2]["client_secret"]

auth_manager = spotipy.SpotifyOAuth(
    scope="playlist-modify-private",
    client_id=spotify_client_id,
    client_secret=spotify_client_secret,
    redirect_uri="http://example.com",
    show_dialog=True,
    cache_path="token.txt",
)

sp = spotipy.Spotify(auth_manager=auth_manager)
user_id = sp.current_user()["id"]
# print(user_id)

playlist = sp.user_playlist_create(user=user_id, name=f"Billboard 100", public=False)
# print(playlisturi_songs = []

uri_songs = []
for index, song in enumerate(song_names):
    search_value = f"track:{song} artist:{artists_names[index]}"
    result = sp.search(q=search_value, type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        uri_songs.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
# print(uri_songs)
