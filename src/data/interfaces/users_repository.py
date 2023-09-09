from typing import List
from abc import ABC, abstractmethod
from src.domain.models.users import Users

class UsersRepositoryInterface(ABC):

    @abstractmethod
    def insert_user(self, name:str, username:str) -> None: pass
    
    @abstractmethod
    def select_user(self, name:str) -> List[Users]: pass
        