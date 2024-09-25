from Animal import *

class Vaca(Animal):
    def __init__(self, posicion):
        super().__init__(posicion)
        
    def mover(self, grilla, pasos):       
        posicionAnteriorVaca = self.getPosicion()
        posicionNuevaVaca = posicionAnteriorVaca + pasos

        grilla[posicionAnteriorVaca] = 0
        grilla[posicionNuevaVaca] = "vaca"
        self.setPosicion(posicionNuevaVaca)

        return f"la vaca se movio"
    
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
            return "la vaca esta lejos del animal para comunicarse, acercate mas"

    def ladrar(self):
        return "muuuuuuuuuuu"
    
    