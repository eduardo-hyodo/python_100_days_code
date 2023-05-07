import smtplib
import datetime as dt


with open("data.txt") as access:
    my_email = access.readline()
    password = access.readline()
email_to = input("Enviar para:")
day_of_the_week = dt.datetime.now().weekday()
if day_of_the_week == 6:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
                from_addr=my_email, 
                to_addrs=email_to, 
                msg=f"subject:Hello\n\n Body da msg aqui com o dia {day_of_the_week}")

