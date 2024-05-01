from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
