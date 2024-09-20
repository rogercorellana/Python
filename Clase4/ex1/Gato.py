from Mascota import *

class Gato(Mascota):
    def __init__(self, id, nombre, edad, estaCastrado, estaVacunado, nivelMiauMiauDeTristeza):
        super().__init__(id, nombre, edad, estaCastrado, estaVacunado)
        self.nivelMiauMiauDeTristeza = nivelMiauMiauDeTristeza
    
    def miaumiau(self):
        return "Miau miau"
    
    def miaumiaumiaumiau(self):
        if self.nivelMiauMiauDeTristeza > 5:
            return """(cancion triste) 
        miau miau miau miauuuu 
        miau miau miau miau miauuuuuu
        miau miau miau miauuuu 
        miau miau miau miau miauuuuuu
        """
        else:
            return "aqui no paso nada, tu gato esta feliz"
        
