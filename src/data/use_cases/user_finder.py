from typing import Dict, List
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users

class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository
        
    def find(self, name: str)-> Dict: 
        self.__validate_name(name)
        users = self.__search_user(name)
        response = self.__format_response(users)
        return response
        
    @classmethod
    def __validate_name(cls, name: str) -> None:

        if not name.isalpha():
            raise Exception('Nome inválido para a busca')

        if len(name) > 18:
            raise Exception('Nome muito grande para a busca')

    def __search_user(self, name: str) -> List[Users]:

        users = self.__users_repository.select_user(name)
        if users == []: raise Exception('Usuario não encontrado')
        return users

    @classmethod
    def __format_response(self, users: List[Users]) -> Dict:
        attributes = []
        for user in users:
            attributes.append({"name": user.name, "username":user.username})

        response = {
            "type":"Users",
            "count": len(users),
            "attributes": attributes
        }

        return response