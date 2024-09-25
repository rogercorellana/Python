from Animal import *

class Perro(Animal):
    def __init__(self, posicion):
        super().__init__(posicion)
        
    def mover(self, grilla, pasos):       
        posicionAnteriorPerro = self.getPosicion()
        posicionNuevaPerro = posicionAnteriorPerro + pasos

        grilla[posicionAnteriorPerro] = 0
        grilla[posicionNuevaPerro] = "perro"
        self.setPosicion(posicionNuevaPerro)

        return f"el perro se movio"
    
    def interractuar(self, animal):     
        
        diferencia = self.getPosicion() - animal.getPosicion() 

        if diferencia > 0:
            mayor = self.getPosicion()
            menor = animal.getPosicion()
        else : 
            mayor = animal.getPosicion()
            menor = self.getPosicion()
        
        if mayor - menor < 3:
            return self.ladrar()
        
        else:
            return "el perro esta lejos del animal para comunicarse, acercate mas"

    def ladrar(self):
        return "guau guau guau"
    
    