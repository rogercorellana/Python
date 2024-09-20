from Mascota import *

class Perro(Mascota):
    def __init__(self, id, nombre, edad, estaCastrado, estaVacunado,nivelDeEntrenamiento):
        super().__init__(id, nombre, edad, estaCastrado, estaVacunado)
        self.nivelDeEntrenamiento = nivelDeEntrenamiento

    def entrenar(self):
        if self.nivelDeEntrenamiento < 5:
            self.nivelDeEntrenamiento = self.nivelDeEntrenamiento + 1
            return f"el perro ha sido entrenado exitosamente con nivel {self.nivelDeEntrenamiento} de 5"

        else:
            return "el perro llego al maximo nivel de entrenamiento"

    def ladrar(self):
        if self.nivelDeEntrenamiento > 3:
            return "tu perro hace GUAU GUAU exitosamente"
        else:
            return "tu perro necesita entrenamiento, no sabe ladrar"

