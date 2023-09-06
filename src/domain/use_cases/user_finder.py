from typing import Dict


class UserFinder():

    @abstractmethod
    def find(self, name: str)-> Dict: 
        pass
