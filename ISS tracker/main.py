# importing modules
import requests
import datetime as dt
import smtplib
import time

# creating constants
MY_LONG = 73.765907
MY_LAT = 18.657133
MY_EMAIL = 'as.play9@gmail.com'
MY_PASSWORD = 'tychelnsyonpdbgg'

# iss api
def iss_overhead():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()         # to raise error in case of any

    data = response.json()  # to hold the data
    iss_longitude = float(data['iss_position']['longitude'])
    iss_latitude = float(data['iss_position']['latitude'])

    # your position with +5 and -5 error
    if MY_LAT - 5 <= iss_longitude <= MY_LAT + 5 and MY_LAT - 5 <= iss_latitude <= MY_LAT + 5:
        return True

# sunlight api
def is_night():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        'formatted':0
    }
    response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_data = data['results']['sunrise']
    sunset_data = data['results']['sunset']
    sunrise = float(sunrise_data.split('T')[1].split(':')[2])
    sunset = float(sunset_data.split('T')[1].split(':')[2])

    # getting current datetime
    time_now = dt.datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(3600)
    if iss_overhead() and is_night():
        with smtplib.SMTP('smpt.gmail.com') as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f'Subject:ISS TRACKER \n look up'
            )

