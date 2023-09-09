from abc import ABC, abstractmethod
from typing import Dict


class UserRegister(ABC):

    @abstractmethod
    def register(self, name: str, username :str)-> Dict: pass
