import requests
from datetime import datetime

USERNAME = "hyododeveloper"

pixela_endpoint = "https://pixe.la/v1/users"

with open("data.txt") as access:
    pixela_api_key = access.readline().rstrip()

headers = {"X-USER-TOKEN": pixela_api_key}
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_params = {
#     "id": "pythonlessons",
#     "name": "Lessons per day Learning Python",
#     "unit": "lessons",
#     "type": "int",
#     "color": "ajisai",
# }
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

today = datetime.now()
pix_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/pythonlessons"
pix_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "2",
}

response = requests.post(url=pix_endpoint, headers=headers, json=pix_params)
print(response.text)
