from src.infra.db.tests.users_repository import UsersRepositorySpy
from .user_finder import UserFinder


def test_find():

    name = 'menuNome'

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    response = user_finder.find(name)

    assert repo.select_user_attributes["name"] == name

    assert response["type"] == "Users"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"] != []

def test_find_error_in_valid_name():
    name = 'meuNome123'

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(name)
        assert False
    except Exception as exception:
        assert str(exception) == "Nome inválido para a busca"


def test_find_error_in_too_long_name():
    name = 'meuNomeAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvXxYyZz'

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(name)
        assert False
    except Exception as exception:
        assert str(exception) == "Nome muito grande para a busca"



def test_find_error_user_not_found():

    class UsersRepositoryError(UsersRepositorySpy):
        def select_user(self, name: str):
            return []

    name = 'meuNome'

    repo = UsersRepositoryError()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(name)
        assert False
    except Exception as exception:
        assert str(exception) == "Usuario não encontrado"
