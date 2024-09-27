from Animal import *

class Gato(Animal):
    def __init__(self, posicion):
        super().__init__(posicion)
    
        
    def mover(self,grilla,pasos):
        posicionFinal = self.getPosicion()+pasos
      
        if posicionFinal > len(grilla):
            return "excede el camino el gato no se puede mover fuera del rango"
        
        if grilla[posicionFinal-1] != 0:
            return "no se puede mover ahi, hay un animal"

        else:
            grilla[posicionFinal-1] = "gato"
            grilla[self.getPosicion()-1] = 0
            self.setPosicion(posicionFinal)
            
            
            return "gato se movio exitosamente"
    
    
    def interractuar(self, animal):
        distancia = abs(self.getPosicion() - animal.getPosicion())
        if distancia < 2:
            return "miauuu"
        else:
            return "el gato esta muy lejos para interactuar"
        




    def __str__(self):
        return "gato " + super().__str__() 