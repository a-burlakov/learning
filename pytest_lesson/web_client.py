import requests
import json
from dataclasses import dataclass


@dataclass
class SomeResourceClient:
    url: str

    def __user_get_status(self, user_id: str):
        resp = requests.get(f"{self.url}/web/user/get-status/{user_id}")
        json_data = json.loads(resp.text)
        return json_data

    def get_information(self, user_id: str):
        json_data = self.__user_get_status(user_id)
        return json_data


if __name__ == "__main__":
    src = SomeResourceClient(url="https://www.avito.ru")
    result = src.get_information("177041581")
    print(result)
