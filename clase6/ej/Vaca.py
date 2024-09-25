from Animal import *

class Vaca(Animal):
    def __init__(self, posicion):
        super().__init__(posicion)
        
    def mover(self):
        return "La vaca se ha movido a una nueva posición."
    
    def interractuar(self):
        return "La vaca está interactuando con otro animal."

    def ladrar(self):
        return "MUUUUUU"