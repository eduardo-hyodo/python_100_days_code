from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
# article_tag = soup.find(name="a", class_="title")
# should be like above, however the site changed since the record
# of the video, now the ancho is without class inside a span
article_tags = soup.find_all("span", "titleline")
article_texts = []
article_links = []
for article_tag in article_tags:
    article = article_tag.findChildren("a", recursive=False)[0]
    article_text = article.getText()
    article_texts.append(article_text)
    article_link = article.get("href")
    article_links.append(article_link)

article_upvotes = []
for subtext in soup.find_all(class_="subtext"):
    score = subtext.findChildren(class_="score")
    if not score:
        article_upvotes.append(0)
    else:
        article_upvotes.append(int(score[0].getText().split()[0]))

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
