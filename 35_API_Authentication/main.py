import requests
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall?"
with open("data.txt") as access:
    lat = access.readline().rstrip()
    lon = access.readline().rstrip()
    api_key = access.readline().rstrip()
    account_sid = access.readline().rstrip()
    auth_token = access.readline().rstrip()
    from_cellphone = access.readline().rstrip()
    to_cellphone = access.readline().rstrip()

weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "exclude": "daily,minutely,current",
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

hourly_weather = response.json()["hourly"][0:11]

will_rain = False

for item in hourly_weather:
    weather_code = item["weather"][0]["id"]
    if int(weather_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=from_cellphone, body="take a umbrella", to=to_cellphone
    )
    print(message.sid)
