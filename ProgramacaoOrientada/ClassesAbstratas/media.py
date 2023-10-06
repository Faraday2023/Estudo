from abc import ABC, abstractmethod

class Media(ABC):
    números = []

    @abstractmethod
    def calcula(self):
        pass
