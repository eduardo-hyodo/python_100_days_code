import data_manager
import flight_search as fs


with open("data.txt") as access:
    sheety_api_token = access.readline().rstrip()
    kiwi_api_token = access.readline().rstrip()

data = data_manager.DataManager(sheety_api_token)
# cities = data.get_cities()["cities"]
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
    flights = flight_search.search_flight(city_code)
    print(flights[0]["price"])
    print(flights[0]["airlines"])
    print(flights[0]["route"])
    # for flight in flights:
    #     print(flight["price"])
    #     print(flight)
