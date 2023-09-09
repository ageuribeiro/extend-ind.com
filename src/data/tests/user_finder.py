from typing import Dict

class UserFinderSpy:
    def __init__(self) -> None:
        self.find_attributes = {}


    def find(self, name: str, username: str) -> Dict:
        self.find_attributes['name'] = name
        self.find_attributes['username'] = username

        return {
            "type":"Users",
            "count": 1,
            "attributes": [
                {"name": name, "username": username}
            ]
        }
