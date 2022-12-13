from abs import ABS, abstractmethod
from typing import Dict

class AbstractStorage(ABS):

    @abstractmethod
    def add(self, name: str, amount: int) -> None:
        pass

    @abstractmethod
    def remove(self, name: str, amount: int) -> None:
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_inique_items(self):
        pass

        