import requests
from  datetime import datetime
import smtplib

MY_LAT =  -42.507351
MY_LONG = -169.127758
ACCECPTABLE_DISTANCE = 5.0

def is_iss_over_me():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = data["iss_position"]["latitude"]
    iss_long = data["iss_position"]["longitude"]
    print(iss_lat + " " + iss_long)
    iss_lat =  float(iss_lat)
    iss_long = float(iss_long)
    if iss_lat < (MY_LAT + ACCECPTABLE_DISTANCE) and iss_lat > (MY_LAT - ACCECPTABLE_DISTANCE):
        if iss_long < (MY_LONG + ACCECPTABLE_DISTANCE) and iss_long > (MY_LONG - ACCECPTABLE_DISTANCE):
            return True
    return False

def is_dark():

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
    if time_now >= sunset:
        return True
    return False

def send_mail():
    with open("data.txt") as access:
        my_email = access.readline()
        password = access.readline()
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
                from_addr=my_email, 
                to_addrs="", 
                msg=f"subject:Hello\n\n Body Look up ")

if is_iss_over_me():
    if is_dark():
        print("lookup")
        send_mail()
