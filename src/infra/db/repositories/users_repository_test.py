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
   

    users_repository = UsersRepository()
    users_repository.insert_user(mocked_name, mocked_username)

    sql = '''
        SELECT * FROM users
        WHERE name ='{}'
        AND username ='{}'  
    '''.format(mocked_name, mocked_username)
    response = connection.execute(text(sql))
    registries = response.fetchall()

    if registries:
        registry = registries[0]

        assert registry.name == mocked_name
        assert registry.username == mocked_username
   
    
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
   

    sql = '''
        INSERT INTO users (name, username) VALUES('{}','{}')
    '''.format(mocked_name, mocked_username)
    connection.execute(text(sql))
    connection.commit()


    users_repository = UsersRepository()
    response = users_repository.select_user(mocked_name)
    
    assert response[0].name == mocked_name
    assert response[0].username == mocked_username
 
    connection.execute(text(f'''
        DELETE FROM users WHERE id = {response[0].id}
    '''))
    connection.commit()