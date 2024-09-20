from abc import *


class FiguraGeometrica(ABC):
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    @abstractmethod
    def calcularArea(self):
        pass