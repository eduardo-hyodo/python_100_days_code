import smtplib
import datetime as dt
import pandas as pd


with open("data.txt") as access:
    my_email = access.readline()
    password = access.readline()

today = dt.datetime.now()
today_tuple = (today.month, today.day) 
df_birthday = pd.read_csv("birthdays.csv")
birthdays_dict = {
        (data_row["month"], data_row["day"]): data_row for (index, data_row) in df_birthday.iterrows()
    }

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
                from_addr=my_email, 
                to_addrs=birthday_person["email"], 
                msg=f"subject:Hello\n\n Body da msg aqui com o dia {birthday_person['name']}")

