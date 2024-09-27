from Animal import *

class Perro(Animal):
    def __init__(self,posicion):
        super().__init__(posicion)

    def mover(self,grilla,pasos):
        
        posicionFinal = pasos + self.getPosicion()
        if posicionFinal > len(grilla):
            return "no podes moverte ahi, estas fuera del rango"
        
        if grilla[posicionFinal-1] != 0:
            return "no podes moverte ahi, hay un animal"
        
        grilla[posicionFinal-1] = "perro"
        grilla[self.getPosicion()-1] = 0 

        self.setPosicion(posicionFinal)


        
    
    
    def interractuar(self):
        pass


    def __str__(self):
        return "perro "+super().__str__()