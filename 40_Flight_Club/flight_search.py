import requests
from datetime import datetime as dt
from datetime import timedelta
from flight_data import FlightData


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
        return response.json()["locations"][0]["code"]

    def search_flight(self, code):
        today = dt.today().date()
        until = dt.today() + timedelta(days=180)
        params = {
            "fly_from": "GRU",
            "fly_to": code,
            "date_from": today,
            "date_to": until.date(),
            "sort": "price",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "limit": 10,
            "curr": "USD",
        }
        response = requests.get(
            url=f"{self.url}v2/search",
            headers=self.headers,
            params=params,
        )
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {code}.")
            return None
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["cityFrom"],
            origin_airport=data["flyFrom"],
            destination_city=data["cityTo"],
            destination_airport=data["flyTo"],
            out_date=data["route"][0]["local_departure"],
            return_date=data["route"][1]["local_departure"],
        )
        # print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data
