from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, posicion):
        self.__posicion = posicion
        
    def getPosicion(self):
        return self.__posicion 
    
    def setPosicion(self,posicion):
        self.__posicion = posicion

    #es necesario? o solo uso gys es lo mismo?
    #nombre = property(getPosicion, setPosicion)

    @abstractmethod
    def mover():
        pass

    @abstractmethod
    def interractuar():
        pass