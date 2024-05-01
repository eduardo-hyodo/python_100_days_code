from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.billboard.com/charts/hot-100/2000-06-16/")

# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
songs_tags = soup.find_all("h3", id="title-of-a-story", class_="a-no-trucate")

song_names = [song.getText().strip() for song in songs_tags]
