import requests


class DataManager:
    def __init__(self, api_token):
        self.api_url = (
            "https://api.sheety.co/9bde88c28235d13c6991888f999ba320/airplaneSearch/"
        )
        self.headers = {"Authorization": f"Bearer {api_token}"}

    def get_cities(self):
        response = requests.get(url=f"{self.api_url}cities/", headers=self.headers)
        # print(response.text)
        return response.json()["cities"]

    def update_city(self, item):
        # print(item)
        response = requests.put(
            url=f"{self.api_url}cities/{item['city']['id']}",
            headers=self.headers,
            json=item,
        )
        # print(response.text)
        return response.status_code

    def create_user(self, item):
        response = requests.post(
            url=f"{self.api_url}users/",
            headers=self.headers,
            json=item,
        )
        return response.raise_for_status()
