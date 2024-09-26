from Animal import *

class Gato(Animal):
    def __init__(self, posicion,pelo):
        super().__init__(posicion)
        self.pelo = pelo
    
    def moverse(self, grilla, pasos):
        posicionAnterior = self.posicion
        posicionNueva = self.posicion + pasos
        tamañogrilla = len(grilla)

        if posicionNueva >= tamañogrilla:
            return "no se puede mover ahi, excede el tamaño del camino existente"
        else:
            if grilla[posicionNueva] != 0:
                return "no se puede mover ahi, ya hay un animal en ese espacio"
            else:
                grilla[posicionAnterior] = 0
                grilla[posicionNueva] = "gato"
                return "gato movido exitosamente"
    
    def interactuar(self, grilla, animal):
        diferencia = abs(self.posicion - animal.posicion)
        if diferencia <= 2:
            return "miauuuuu"
        else:
            return "el gato debe acercarse mas"

    def __str__(self):
        return super().__str__() + f", Pelo = {self.pelo}"
