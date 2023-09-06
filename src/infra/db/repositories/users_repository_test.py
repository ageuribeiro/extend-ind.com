from .users_repository import UsersRepository


def test_insert_user():
    mocked_name = 'name'
    mocked_username = 'username'
    mocked_email = 'email'
    mocked_senha = 'senha'
    mocked_profile ='profile'
    mocked_ativo = True

    users_repository = UsersRepository()
    users_repository.insert_user(mocked_name, mocked_username, mocked_email, mocked_senha, mocked_profile, mocked_ativo)