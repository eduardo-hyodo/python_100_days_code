import data_manager

# PYTHONPATH=$PWD/../
from gen_data import Data


print("Welcome to the Flight Club")
print("we find the best flight deals and email you")

name = input("What is your name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")
re_email = input("Type your email again, plz\n")

if email == re_email:
    access_data = Data().get()["app"]
    sheety_api_token = access_data[0]["api_key"]
    data = data_manager.DataManager(sheety_api_token)
    item = {
        "user": {
            "name": name,
            "lastName": last_name,
            "email": email,
        }
    }
    data.create_user(item)

print("You are in the  club!")
