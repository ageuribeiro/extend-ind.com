from typing import Dict
from src.domain.use_cases.user_register import UserRegister as UserRegisterInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface
import re

class UserRegister(UserRegisterInterface):
    def __init__(self, user_repository: UsersRepositoryInterface)->None:
        self.__user_repository = user_repository

    def register(self, name: str, username: str, email: str, senha: str, profile: str, ativo: bool)-> Dict:
        self.__validate_name(name)
        self.__validate_username(username)
        self.__validate_email(email)
        self.__validate_password(senha)
        self.__validate_lowercase(senha)
        self.__validate_special_characters(senha)
        self.__validate_length(senha)
        self.__validate_name(profile)
        self.__validate_boolean(ativo)
        
        self.__registry_user_informations(name, username, email, senha, profile, ativo)
        response = self.__format_response(name, username, email, senha, profile, ativo)
        return response

    @classmethod
    def __validate_name(cls, name: str) -> None:
        if not name.isalpha():
            raise Exception('Nome invalido para a busca')

        if len(name) > 18:
            raise Exception('Nome muito grande para a busca')

    @classmethod
    def __validate_username(cls, username: str) -> None:
        if not username.isalpha():
            raise Exception('Username invalido para a busca')

        if len(username) > 36:
            raise Exception('Username muito grande para a busca')

    @classmethod
    def __validate_email(cls, email: str) -> None:
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise Exception('Email inválido')


    @classmethod
    def __validate_password(cls, password: str) -> None:
        # Verifica se a senha tem pelo menos 1 letra maiúscula
        if not re.search(r'[A-Z]', password):
            raise Exception('A senha deve conter pelo menos 1 letra maiúscula')

    @classmethod
    def __validate_lowercase(cls, password: str) -> None:
        # Verifica se a senha tem pelo menos 1 letra minúscula
        if not re.search(r'[a-z]', password):
            raise Exception('A senha deve conter pelo menos 1 letra minúscula')

    @classmethod
    def __validate_special_characters(cls, password: str) -> None:
        # Verifica se a senha tem caracteres especiais
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise Exception('A senha deve conter caracteres especiais')

    @classmethod
    def __validate_length(cls, password: str) -> None:
        # Verifica se a senha tem mais de 6 caracteres
        if len(password) < 6:
            raise Exception('A senha deve ter pelo menos 6 caracteres')
                
    @classmethod
    def __validate_boolean(cls, ativo: bool) -> None:
        if not isinstance(ativo, bool):
            raise Exception(f'O campo {ativo} deve ser do tipo booleano (True ou False)')


    def __registry_user_informations(self, name: str, username :str, email: str, senha: str, profile: str, ativo: bool) -> None:
        self.__user_repository.insert_user(name, username, email, senha, profile, ativo)

    @classmethod
    def __format_response(cls, name: str, username :str, email: str, senha: str, profile: str, ativo: bool) -> Dict:
        response = {
            "type": "Users",
            "count": 1,
            "attributes": {
                "name": name,
                "username": username,
                "email": email,
                "senha": senha,
                "profile": profile,
                "ativo": ativo
            }
        }
        return response