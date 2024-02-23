# import requests
# from pprint import pprint
# sheety_username = "42132b232468540c1c607c1c6049a62c"
# project_name = "copyOfFlightDeals"
# sheet_name = "prices"
# sheety_endpoint = f"https://api.sheety.co/{sheety_username}/{project_name}/{sheet_name}"
#
#
# class DataManager:
#     # This class is responsible for talking to the Google Sheet.
#     # getting the data from sheety
#     def __init__(self):
#         self.destination_data = {}
#
#
#     def get_destination_data(self):
#
#         response = requests.get(url=sheety_endpoint)
#         response.raise_for_status()
#         data = response.json()
#         self.destination_data = data['prices']
#
#         return self.destination_data
#
#     def update_destination_codes(self, data, iataCode):
#         new_data = {
#             "price": {
#                 "iataCode": iataCode
#             }
#         }
#         response = requests.put(
#             url=f"{sheety_endpoint}/{data['id']}",
#             json=new_data
#         )
# -------------------------------------------------------------------------------
from pprint import pprint
import requests

sheety_username = "42132b232468540c1c607c1c6049a62c"
project_name = "copyOfFlightDeals"
sheet_name = "prices"


SHEETY_PRICES_ENDPOINT = f"https://api.sheety.co/{sheety_username}/{project_name}/{sheet_name}"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

