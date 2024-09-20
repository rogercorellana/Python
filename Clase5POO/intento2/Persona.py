

from abc import ABC


class Persona(ABC):
    def __init__(self, nombre):
        self.__nombre = nombre
        
    def getNombre(self):
        return self.__nombre 
    
    def setNombre(self,nombre):
        self.__nombre = nombre

    nombre = property(getNombre, setNombre)
