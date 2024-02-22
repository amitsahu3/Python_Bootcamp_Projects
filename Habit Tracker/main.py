import requests
from datetime import datetime

# pixela variables
USERNAME = "amit9999"
TOKEN = "adnjndkcnkjsdnkjndn"
GRAPHID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#1 create a user account
# response1 = requests.post(url=pixela_endpoint, json=user_params)
# print(response1.text)

#2 create a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPHID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"

}

headers = {
    "X-USER-TOKEN" : TOKEN              # to authenticate the url
}
# response2 = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response2.text)

#3 post a pixel to the graph
today = datetime.now().date()
formatted_today = today.strftime("%Y%m%d")

pixela_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
post_pixel_params= {
    "date":formatted_today,
    "quantity": input("How many km did you cycle today?\n")
}
response3 = requests.post(url=pixela_creation_endpoint, json=post_pixel_params, headers=headers)

# #4 pixel updation
# update_pixel_endpoint = f"{pixela_creation_endpoint}/{formatted_today}"
# update_data = {
#     "quantity": "50"
# }
# # response4 = requests.put(url=update_pixel_endpoint, json=update_data, headers=headers)
# # print(response4.text)
#
# #5 delete a pixel
# response5 = requests.delete(url=update_pixel_endpoint, headers=headers)
# print(response5.text)