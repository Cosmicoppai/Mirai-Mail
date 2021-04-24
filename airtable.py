from dataclasses import dataclass
import requests


@dataclass()
class AirTable:
    base_id: str
    table_name: str
    api_key: str


    def create_records(self, _data: object = {}):
        if len(_data.keys()) != 0:
            endpoint = f"https://api.airtable.com/v0/{self.base_id}/{self.table_name}"

            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            data = {
                "records": [
                    {
                        "fields": _data
                    }
                ]
            }
            # print(data)
            r = requests.post(endpoint, json=data, headers=headers)
            # print(endpoint, r.json())
            return r.status_code == 200 or r.status_code == 201

        return False
