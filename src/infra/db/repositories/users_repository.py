from typing import List
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.users import Users as UsersEntity
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users

class UsersRepository(UsersRepositoryInterface):

    @classmethod
    def insert_user(cls, name:str, username:str)->None:
        with DBConnectionHandler() as database:

            try:
                new_registry = UsersEntity(
                    name=name,
                    username=username,
                   
                )
                database.session.add(new_registry)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def select_user(cls, name: str) -> List[Users]:
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