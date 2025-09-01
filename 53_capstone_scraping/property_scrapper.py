from bs4 import BeautifulSoup
import requests

class PropertyScrapper:
    def __init__(self):
        url = "https://appbrewery.github.io/Zillow-Clone/"
        self.response = requests.get(
            url,
            headers={
                "User-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0",
                "Accept-Language": "en-US,en;q=0.5",
            },
        )

        self.soup = BeautifulSoup(self.response.content, "lxml")
    
    def get_prices(self):
        list = self.soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
        price_list = [price.getText().strip() for price in list]
        return price_list

    def get_urls(self):
        list = self.soup.find_all(class_="StyledPropertyCardDataArea-anchor")
        url_list = [url.get("href") for url in list]
        return url_list

    def get_address(self):
        list = self.soup.find_all('address')
        address_list = [address.getText().strip() for address in list]
        return address_list

