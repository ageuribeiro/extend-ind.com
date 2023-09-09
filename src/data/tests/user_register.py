from typing import Dict

class UserRegisterSpy:
    def __init__(self) -> None:
        self.register_attributes = {}


    def register(self, name: str, username: str) -> Dict:
        self.register_attributes['name'] = name
        self.register_attributes['username'] = username
    
        return {
            "type":"Users",
            "count": 1,
            "attributes": [
                {"name": name, "username": username}
            ]
        }
