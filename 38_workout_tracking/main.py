import requests
from datetime import datetime

NUTRITION_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

with open("data.txt") as access:
    nutrition_api_key = access.readline().rstrip()
    nutrition_app_id = access.readline().rstrip()
    sheety_api_key = access.readline().rstrip()
    beaer_token = access.readline().rstrip()

headers = {
    "x-app-id": nutrition_app_id,
    "x-app-key": nutrition_api_key,
}

body = {
    "query": "run 3 miles",
    "gender": "male",
    "weight_kg": 118.0,
    "height_cm": 175.0,
    "age": 40,
}

response = requests.post(url=NUTRITION_URL, headers=headers, json=body)
exercise = response.json()["exercises"][0]


sheety_url = f"https://api.sheety.co/{sheety_api_key}/workout/log"
today = datetime.today()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")
workout_headers = {
    "Authorization": f"Bearer {beaer_token}",
}
workout_body = {
    "log": {
        "date": str(date),
        "time": str(time),
        "exercise": exercise["user_input"],
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"],
    }
}

log_resonse = requests.post(url=sheety_url, json=workout_body, headers=workout_headers)
# log_resonse = requests.get(url=sheety_url)
print(log_resonse.text)
