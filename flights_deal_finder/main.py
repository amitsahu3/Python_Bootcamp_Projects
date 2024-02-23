# import requests
from pprint import pprint
# from data_manager import DataManager
# from flight_search import FlightSearch
# from datetime import datetime, timedelta
#
# #This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
#
# # creating data manager
# data_mng =DataManager()
# sheet_data = data_mng.get_destination_data()
#
# #creating flight search in order to populate sheet with iatacode
# flight_search = FlightSearch()
# # for i in range(len(sheet_data)):
# #     if sheet_data[i]["iataCode"] == "":
# #         iataCode = flight_search.get_destination_code(sheet_data[i]["city"])
# #         data_mng.update_destination_codes(sheet_data[i], iataCode)
#
# ORIGIN_CITY_IATA = 'LON'
#
# # getting time and dates for next six months
# tomorrow = datetime.now().date() + timedelta(days=1)
# two_months_from_today = datetime.now().date() + timedelta(days=(2*30))
#
# for destination in sheet_data:
#     flight = flight_search.check_flights(
#         origin_city_code= ORIGIN_CITY_IATA,
#         destination_city_code= destination['iataCode'],
#         from_time= tomorrow,
#         to_time= two_months_from_today
#     )
#---------------------------------------------------------------------------------
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    # if flight.price < destination["lowestPrice"]:
    #     notification_manager.send_sms(
    #         message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
    #     )
    pprint(flight)