from FiguraGeometrica import *

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__(base, altura)


    # si no hereda nada solo pongo pass

    def calcularArea(self):
        area = self.base * self.altura
        return area
