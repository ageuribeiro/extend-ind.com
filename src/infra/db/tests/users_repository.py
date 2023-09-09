from typing import List
from src.domain.models.users import Users

class UsersRepositorySpy():

    def __init__(self) -> None:
        self.insert_user_attributes = {}
        self.select_user_attributes = {}


    def insert_user(self, name:str, username:str)->None:
        self.insert_user_attributes["name"] = name
        self.insert_user_attributes["username"] = username
       
        return
    
    def select_user(self, name: str) -> List[Users]:
        self.select_user_attributes["name"] = name
        return[
            Users('Ageu','ageuribeiro'),
            Users('Ageu','ageuribeiro'),
            Users('Ageu','ageuribeiro'),
            Users('Ageu','ageuribeiro'),
        ]