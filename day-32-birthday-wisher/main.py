from datetime import datetime
import pandas as pd
import random
import smtplib

today = datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("./birthdays.csv")

birthdays_dict = {(r['month'], r['day']): r for (idx, r) in data.iterrows()}

if today_tuple in birthdays_dict:
    p = birthdays_dict.get(today_tuple)
    file_path = f"./letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as f:
        email_body = f.read()
        email_body = email_body.replace("[NAME]", p['name'])

    my_email = "unp7600@gmail.com"
    my_password = "your-app-password"

    with smtplib.SMTP("smtp.gmail.com", timeout=60, port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=p['email'],
            msg=f"Subject: Happy Birthday!.\n\n{email_body}"
        )
        print("sent!")
