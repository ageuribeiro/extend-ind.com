from typing import List
from src.domain.models.users import Users

class UsersRepositorySpy():

    def __init__(self) -> None:
        self.insert_user_attributes = {}
        self.select_user_attributes = {}


    def insert_user(self, name:str, username:str, email:str, senha:str, profile:str, ativo:bool)->None:
        self.insert_user_attributes["name"] = name
        self.insert_user_attributes["username"] = username
        self.insert_user_attributes["email"] = email
        self.insert_user_attributes["senha"] = senha
        self.insert_user_attributes["profile"] = profile
        self.insert_user_attributes["ativo"] = ativo
        return
    
    def select_user(self, name: str) -> List[Users]:
        self.select_user_attributes["name"] = name
        return[
            Users('Ageu','ageuribeiro', 'ageu87@gmail.com','123','admin',True),
            Users('Ageu','ageuribeiro', 'ageu87@gmail.com','123','admin',True),
            Users('Ageu','ageuribeiro', 'ageu87@gmail.com','123','admin',True),
            Users('Ageu','ageuribeiro', 'ageu87@gmail.com','123','admin',True),
        ]