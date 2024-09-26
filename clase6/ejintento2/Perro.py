from Animal import *

class Perro(Animal):
    def __init__(self, posicion, raza):
        super().__init__(posicion)
        self.raza = raza
    
    def moverse(self):
        return "me muevo wuuu"
    
    def interactuar(self):
        return "interactuo wuuu"
    
    def __str__(self):
        return super().__str__() + f", Raza = {self.raza}"