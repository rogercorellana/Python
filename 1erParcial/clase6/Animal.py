from abc import *

class Animal(ABC):
    def __init__(self,posicion):
        self.__posicion = posicion

    def getPosicion(self):
        return self.__posicion
    
    def setPosicion(self, posicion):
        self.__posicion = posicion

    @abstractmethod
    def mover(self):
        pass
    
    @abstractmethod
    def interractuar(self):
        pass

    def __str__(self):
        return f"en posicion {self.getPosicion()}"
