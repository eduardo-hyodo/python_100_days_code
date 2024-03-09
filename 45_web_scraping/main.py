from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
# article_tag = soup.find(name="a", class_="title")
# should be like above, however the site changed since the record
# of the video, now the ancho is without class inside a span
# the span has the class title
article_tag = soup.select_one(".title a")
article_text = article_tag.getText()
article_link = article_tag.get("href")
article_upvote = soup.find(name="span", class_="score").getText()
print(article_tag)
print(article_text)
print(article_upvote)

# TODO improve the select or filter after to clean, because there are more anchor then it should
article_tags = soup.select(".title a")
article_texts = []
article_links = []
for article_tag in article_tags:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    article_links.append(article_link)

article_upvotes = [
    int(score.getText().split()[0])
    for score in soup.find_all(name="span", class_="score")
]

print(article_texts)
print(article_links)
print(article_upvotes)

largest_score = max(article_upvotes)
largest_score_index = article_upvotes.index(largest_score)
print(article_texts[largest_score_index])

# Testing Bsoup

# with open("./website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title.string)

# # print(soup)

# # print(soup.prettify())

# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)

# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))
