from Animal import *

class Perro(Animal):
    def __init__(self, posicion):
        super().__init__(posicion)
        
    def mover(self):
        return "El perro se ha movido a una nueva posición."
    
    def interractuar(self):
        return "El perro está interactuando con otro animal."

    def ladrar(self):
        return "Guau guau"