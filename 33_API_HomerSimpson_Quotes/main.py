import requests
from  datetime import datetime

MY_LAT =  30.507351
MY_LONG = -34.127758
ACCECPTABLE_DISTANCE = 5.0

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_lat = data["iss_position"]["latitude"]
iss_long = data["iss_position"]["longitude"]
print(iss_lat + " " + iss_long)
parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data =  response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

iss_lat =  float(iss_lat)
iss_long = float(iss_long)
if iss_lat < (MY_LAT + ACCECPTABLE_DISTANCE) and iss_lat > (MY_LAT - ACCECPTABLE_DISTANCE):
    if iss_long < (MY_LONG + ACCECPTABLE_DISTANCE) and iss_long > (MY_LONG - ACCECPTABLE_DISTANCE):
        if time_now >= sunset:
            print("lookup")
