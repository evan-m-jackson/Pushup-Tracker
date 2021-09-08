import requests
from datetime import datetime

USERNAME = "ejackson93"
TOKEN = "effafhfakfjaffha"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "pushupgraph",
    "name": "Pushup Graph",
    "unit": "Pushups",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_endpoint = f"{graph_endpoint}/{graph_config['id']}"

today = datetime.now()


post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many pushups did you do today?")
}

# response = requests.post(url=post_endpoint, json=post_config, headers=headers)
# print(response.text)

update_endpoint = f"{post_endpoint}/<Insert date to be updated>"

update_config = {
    "quantity": input("How many pushups did you actually do?")
}

# response = requests.put(url=update_endpoint, json=update_config,headers=headers)
# print(response.text)

delete_endpoint = f"{post_endpoint}/<Insert date to be deleted>"

# response = requests.delete(url=delete_endpoint,headers=headers)
# print(response.text)