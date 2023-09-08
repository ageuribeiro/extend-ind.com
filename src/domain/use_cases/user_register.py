from abc import ABC, abstractmethod
from typing import Dict


class UserRegister(ABC):

    @abstractmethod
    def register(self, name: str, username :str, email: str, senha: str, profile: str, ativo: bool)-> Dict: pass
