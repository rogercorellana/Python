from abc import *

class Animal(ABC):
    def __init__(self,posicion):
        self.posicion = posicion
    
    @abstractmethod
    def moverse(self):
        pass
    
    @abstractmethod
    def interactuar(self):
        pass

    def __str__(self):
        return f"Animal en la posicion {self.posicion}"