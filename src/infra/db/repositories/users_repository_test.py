import pytest
from sqlalchemy import text
from src.infra.db.settings.connection import DBConnectionHandler
from .users_repository import UsersRepository

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()

@pytest.mark.skip(reason="Sensive test")
def test_insert_user():
    mocked_name = 'name'
    mocked_username = 'username'
    mocked_email = 'email'
    mocked_senha = 'senha'
    mocked_profile ='profile'
    mocked_ativo = True

    users_repository = UsersRepository()
    users_repository.insert_user(mocked_name, mocked_username, mocked_email, mocked_senha, mocked_profile, mocked_ativo)

    sql = '''
        SELECT * FROM users
        WHERE name ='{}'
        AND username ='{}'
        AND email ='{}'    
    '''.format(mocked_name, mocked_username, mocked_email)
    response = connection.execute(text(sql))
    registries = response.fetchall()

    if registries:
        registry = registries[0]

        assert registry.name == mocked_name
        assert registry.username == mocked_username
        assert registry.email == mocked_email
    
        connection.execute(text(f'''
            DELETE FROM users WHERE id = {registry.id}
        '''))
        connection.commit()

        print()
        print(registry)
    else:
        assert False, "Nenhum registro encontrado para os criterios especificados."

@pytest.mark.skip(reason="Sensive test")
def test_select_user():
    mocked_name = 'name2'
    mocked_username = 'username2'
    mocked_email = 'email2'
    mocked_senha = 'senha2'
    mocked_profile ='profile2'
    mocked_ativo = True

    sql = '''
        INSERT INTO users (name, username, email, senha, profile, ativo) VALUES('{}','{}','{}','{}','{}','{}')
    '''.format(mocked_name, mocked_username, mocked_email, mocked_senha, mocked_profile, mocked_ativo)
    connection.execute(text(sql))
    connection.commit()


    users_repository = UsersRepository()
    response = users_repository.select_user(mocked_name)
    
    assert response[0].name == mocked_name
    assert response[0].username == mocked_username
    assert response[0].email == mocked_email

    connection.execute(text(f'''
        DELETE FROM users WHERE id = {response[0].id}
    '''))
    connection.commit()