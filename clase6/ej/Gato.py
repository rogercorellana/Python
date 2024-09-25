from Animal import *

posicionGato = [0]

class Gato(Animal):
    def __init__(self, posicion):
        super().__init__(posicion)
        
    def mover(self, grilla, pasos):
        posicionGato = grilla[pasos]
        return posicionGato

    
    def interractuar(self, grilla):
        posicion1 = grilla[self.getPosicion]
        posicion2 = grilla[perro1.getPosicion]
    

            
        

        return "El GATO está interactuando con otro animal."

    def ladrar(self):
        return "miau miau miau miau"