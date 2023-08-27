import requests
from datetime import datetime as dt


class FlightSearch:
    def __init__(self, api_token):
        self.url = "https://api.tequila.kiwi.com/"
        self.headers = {
            "apikey": api_token,
        }

    def get_location(self, name):
        params = {
            "term": name,
            "locale": "en-US",
            "location-types": "city",
        }
        response = requests.get(
            url=f"{self.url}locations/query",
            headers=self.headers,
            params=params,
        )
        # print(response.json()["locations"][0]["code"])
        return response.json()["locations"][0]["code"]

    def search_flight(self, code):
        params = {
            "fly_from": "GRU",
            "fly_to": code,
            "date_from": dt.today().date(),
            "date_to": dt.strptime("12-25-2023", "%m-%d-%Y").date(),
            "sort": "price",
            "limit": 10,
        }
        response = requests.get(
            url=f"{self.url}search",
            headers=self.headers,
            params=params,
        )
        # print(response.text)
        return response.json()["data"]
