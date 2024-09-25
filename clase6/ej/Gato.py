from Animal import *

class Gato(Animal):
    def __init__(self, posicion):
        super().__init__(posicion)
        
    def mover(self, grilla, pasos):       
        posicionAnteriorGato = self.getPosicion()
        posicionNuevaGato = posicionAnteriorGato + pasos

        grilla[posicionAnteriorGato] = 0
        grilla[posicionNuevaGato] = "gato"
        self.setPosicion(posicionNuevaGato)

        return f"el gato se movio"

    def interractuar(self, animal):     
        
        diferencia = self.getPosicion() - animal.getPosicion() 

        if diferencia > 0:
            mayor = self.getPosicion()
            menor = animal.getPosicion()
        else : 
            mayor = animal.getPosicion()
            menor = self.getPosicion()
        
        if mayor - menor < 3:
            return self.maullear()
        
        else:
            return "el gato esta lejos del animal para comunicarse, acercate mas"
        
        
    # def interractuar(self, animal):
    # diferencia = abs(self.getPosicion() - animal.getPosicion())
    
    # if diferencia < 3:
    #     return self.maullear()
    # else:
    #     return "El gato está lejos del animal para comunicarse, acércate más"

    def maullear(self):
        return "miau miau miau miau"

    def __str__(self):
        return f"gato {self.getPosicion()}"
   