import data_manager
import flight_search as fs

# PYTHONPATH=$PWD/../
from gen_data import Data

access_data = Data().get()["app"]
sheety_api_token = access_data[0]["api_key"]
kiwi_api_token = access_data[1]["api_key"]
# data = data_manager.DataManager(sheety_api_token)
# cities = data.get_cities()
cities = [
    {
        "city": "montreal",
        "iataCode": "teste",
        "id": 2,
    },
]

flight_search = fs.FlightSearch(kiwi_api_token)
for city in cities:
    city_code = flight_search.get_location(city["city"])

    # new_city = {
    #     "city": {
    #         "city": city["city"],
    #         "id": city["id"],
    #         "iataCode": city_code,
    #         "lowestPrice": city["lowestPrice"],
    #     }
    # }
    # data.update_city(new_city)
    flight = flight_search.search_flight(city_code)
    print(flight)
    # for flight in flights:
    #     print(flight["price"])
    #     print(flight)
