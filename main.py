import random
import smtplib

import pandas
import datetime as dt


dt_now = dt.datetime.now()
b_day = (dt_now.month, dt_now.day)

df_data = pandas.read_csv("birthdays.csv")
birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row for (index, data_row) in df_data.iterrows()
}

if b_day in birthdays_dict:
    random_letter = f"letter_{random.randint(1, 3)}.txt"
    with open(f"./letter_templates/{random_letter}") as letter_file:
        content = letter_file.read()
        person = birthdays_dict[b_day]
        new_letter = content.replace("[NAME]", person["name"])

my_email = "ttestar459@gmail.com"
password = "wwrnjxhmfjwdycie"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()  # make connection secure
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=person["email"],
        msg=f"Subject:Happy Birthday!\n\n{new_letter}")
