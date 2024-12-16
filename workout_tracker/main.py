import requests
from datetime import datetime
import os

USERNAME = "jerrylifts"
TOKEN = os.environ.get("PIXELA_TOKEN")
ID = "graph1"
starting_url = "https://pixe.la/v1/users"
DATE_FORMATTED = datetime(year=2024, month=6, day=25).strftime("%Y%m%d")

"""parameters needed to create a new user"""
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#https://docs.pixe.la/entry/post-user
#https://pixe.la

"""create username and secret key using post"""
# response = requests.post(url=pixela_url, json=user_params)
# print(response.text)


"""graph starting url"""
#https://docs.pixe.la/entry/post-graph
graph_url = f"{starting_url}/{USERNAME}/graphs"

"""parameters for graph"""
graph_config = {
    "id": ID,
    "name": "Workout Graph",
    "unit": "commit",
    "type": "int",
    "color": "sora"
}

"""authenticates ourselves using headers """
headers = {
    "X-USER-TOKEN": TOKEN
}

"""creates the graph"""
# response = requests.post(url=graph_url, json=graph_config, headers=headers)
# print(response.text)

today = datetime(year=2024, month=6, day=25)

"""create a pixel on graph url"""
pixel_url = f"{graph_url}/{ID}"

#format datetime using strftime - https://www.w3schools.com/python/python_datetime.asp

pixel_config = {
    "date": DATE_FORMATTED,
    "quantity": input("How many hours did you workout today")
}

# response = requests.post(url=pixel_url, json=pixel_config, headers=headers)
# print(response.text)


#https://docs.pixe.la/entry/put-pixel
"""update pixel on graph"""
update_url = f"{pixel_url}/{DATE_FORMATTED}"

update_config = {
    "quantity": "9"
}

# response = requests.put(url=update_url, json=update_config, headers=headers)
# print(response.text)


#https://docs.pixe.la/entry/delete-pixel
"""delete pixel on graph"""
delete_url = f"{pixel_url}/{DATE_FORMATTED}"

# response = requests.delete(url=delete_url, headers=headers)
# print(response.text)