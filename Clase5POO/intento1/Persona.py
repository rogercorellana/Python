from abc import *



class Persona(ABC):
    def __init__(self, nombre):
        self.___nombre = nombre
        
    def getNombre(self):
        return self.___nombre 
    
    def setNombre(self,nombre):
        self.___nombre = nombre


    nombre = property(getNombre, setNombre)

    
    def __str__(self, nombre):
       print(f"Hola soy: {self.nombre} ")
