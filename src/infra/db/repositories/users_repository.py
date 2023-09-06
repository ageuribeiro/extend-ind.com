from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.users import Users as UsersEntity

class UsersRepository:

    @classmethod
    def insert_user(cls, name:str, username:str, email:str, senha:str, profile:str, ativo:bool)->None:
        with DBConnectionHandler() as database:

            try:
                new_registry = UsersEntity(
                    name=name,
                    username=username,
                    email=email,
                    senha=senha,
                    profile=profile,
                    ativo=ativo
                )
                database.session.add(new_registry)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def select_user(cls, name:str)->any:
        with DBConnectionHandler() as database:
            try:
                users = (
                    database.session
                    .query(UsersEntity)
                    .filter(UsersEntity.name == name)
                    .all()
                )
                return users
            except Exception as exception:
                database.session.rollback()
                raise exception