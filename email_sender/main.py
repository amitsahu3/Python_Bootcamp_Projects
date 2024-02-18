#
# import smtplib
# MY_EMAIL = "amit.9993013869@gmail.com"
# MY_PASSWORD = "tychelnsyonpdbgg"            # app password for this particular use case of the gmail provided
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=MY_EMAIL, password=MY_PASSWORD)
#     connection.sendmail(
#         from_addr=MY_EMAIL,
#         to_addrs='as.play9@gmail.com',
#         msg=f"Subject:Happy Birthday!"  # email without a subject is highly likely to be spam
#     )

import datetime as dt

# getting current day
current_datetime = dt.datetime.now()
print(current_datetime)
