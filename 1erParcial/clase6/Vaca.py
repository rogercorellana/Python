from Animal import *

class Vaca(Animal):
    def __init__(self, posicion):
        super().__init__(posicion)

    def mover(self,grilla,pasos):
        posicionFinal = self.getPosicion() + pasos
        if posicionFinal > len(grilla):
            return "excediste el camino"
        if grilla[posicionFinal-1] != 0:
            return "hay un animal en ahi no podes moverte"
        else:
            grilla[posicionFinal-1] = "vaca"
            grilla[self.getPosicion()-1] = 0
            self.setPosicion(posicionFinal)
            return "vaca movida exitosamente"
        
    def interractuar(self,animal):
        distancia = abs(self.getPosicion() - animal.getPosicion())
        if distancia <= 2:
            return "muuuuuuuuu"
        else:
            return "vaca muy lejos, acercate mas"

    def __str__(self):
        return "vaca " + super().__str__()