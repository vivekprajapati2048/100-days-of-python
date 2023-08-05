import smtplib
import datetime
import random

today = datetime.datetime.now()
day_of_week = today.weekday()

if day_of_week == 0:
    with open("./quotes.txt") as f:
        all_quotes = f.readlines()
        qotd = random.choice(all_quotes)
        print(qotd)

        my_email = "unp7600@gmail.com"
        my_password = "your-app-password"

        with smtplib.SMTP("smtp.gmail.com", timeout=60, port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="vp2048@gmail.com",
                msg=f"Subject: Monday Motivation.\n\n{qotd}"
            )
            print("sent!")

