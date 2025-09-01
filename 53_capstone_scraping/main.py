from bs4 import BeautifulSoup
import requests

url = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(
    url,
    headers={
        "User-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0",
        "Accept-Language": "en-US,en;q=0.5",
    },
)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

list = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
price_list = [ price.getText().strip() for price in list]
for item in price_list:
    print(item[1:6])

list = soup.find_all(class_="StyledPropertyCardDataArea-anchor")
url_list = [ url.get("href") for url in list]
for url in url_list:
    print(url)

list = soup.find_all('address')
address_list = [ address.getText().strip() for address in list]
for address in address_list:
    print(address)
