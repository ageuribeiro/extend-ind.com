from src.infra.db.tests.users_repository import UsersRepositorySpy
from .user_register import UserRegister

def test_register():
    name = "Ageu"
    username = "ageuribeiro"
    email = "ageu87@gmail.com" 
    senha = "A@a123"
    profile = "admin"
    ativo = True

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    response = user_register.register(name, username, email, senha, profile, ativo)
    
    print()
    print(repo.insert_user_attributes)

    assert repo.insert_user_attributes["name"] == name
    assert repo.insert_user_attributes["username"] == username
    assert repo.insert_user_attributes["email"] == email
    assert repo.insert_user_attributes["senha"] == senha
    assert repo.insert_user_attributes["profile"] == profile
    assert repo.insert_user_attributes["ativo"] == ativo

    assert response["type"] == "Users"
    assert response["count"] == 1
    assert response["attributes"]

def test_register_name_error():

    name = "Ageu134679"
    username = "ageuribeiro"
    email = "ageu87mail.com" 
    senha = "A@123"
    profile = "admin"
    ativo = True

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    try:
        user_register.register(name, username, email, senha, profile, ativo)
        assert False
    except Exception as exception:
        assert str(exception) == "Nome invalido para a busca"