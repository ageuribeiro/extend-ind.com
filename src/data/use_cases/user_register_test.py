from src.infra.db.tests.users_repository import UsersRepositorySpy
from .user_register import UserRegister

def test_register():
    name = "Ageu"
    username = "ageuribeiro"

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    response = user_register.register(name, username)
    
    print()
    print(repo.insert_user_attributes)

    assert repo.insert_user_attributes["name"] == name
    assert repo.insert_user_attributes["username"] == username
    
    assert response["type"] == "Users"
    assert response["count"] == 1
    assert response["attributes"]

def test_register_name_error():

    name = "Ageu134679"
    username = "ageuribeiro"
  

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    try:
        user_register.register(name, username)
        assert False
    except Exception as exception:
        assert str(exception) == "Nome invalido para a busca"