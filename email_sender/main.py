# importing libraries
from datetime import datetime
import pandas
import random
import smtplib
# creating constants
MY_EMAIL = "amit.9993013869@gmail.com"
MY_PASSWORD = "zygaejrgxbemaesn"  #"lwohqywjnyrhpzdt"

#1. add details to the birthdays.

#2. check if today is a birthday in birthday.csv
today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("C:/Users/nitro/Desktop/PythonBootCamp/day-32(send automatic emails)/birthdays.csv")

# USE DICT_COMPREHENSION TO CREATE A DICTIONARY FROM BIRTHDAY.CSv
birthday_dict = {
    (data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()
}

# checking if today day and today month matches in dictionary,if so getting a letter from the three
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letters_{random.randint(1,3)}.txt"           # selecting a random letter template from the given three
    with open(file_path) as letter_file:                                        # opening the final file_path to read from it
        contents = letter_file.read()                                           # reading the file
        contents = contents.replace("[NAME]", birthday_person["name"])             # saving it to the original variable

# sending that person the birthday msg
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday! \n\n{contents}"
        )




