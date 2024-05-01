from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")

movies_tags = soup.find_all("h3")
# print(movies_tags)
movies_tags.reverse()
with open("movies.txt", "w") as movies:
    for movie in movies_tags:
        print(movie.getText())
        movies.write(movie.getText() + "\n")
