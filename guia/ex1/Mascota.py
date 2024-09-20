class Mascota:
    def __init__(self,id,nombre,edad,estaCastrado,estaVacunado):

        # privado con _
        self._id = id
        self.nombre = nombre
        self.edad = edad
        self.estaCastrado = estaCastrado
        self.estaVacunado = estaVacunado

    pass

    

    # toString
    def __str__(self):
        return "blablabla"



    def comer(self):
        return "estoy comiendo"
    
    def castrar(self):
        if self.edad > 2:
            if self.estaCastrado:
                return f"{self.nombre} fue castrado anteriormente"
            else:
                self.estaCastrado = True
                return f"{self.nombre} castrado exitosamente"

        else:
            return f" {self.nombre} no puede ser castrado"
        
    def vacunar(self):
        if self.estaVacunado:
            return f"{self.nombre} vacunado anteriormente"
        else:
            self.estaVacunado = True
            return f"{self.nombre} vacunado exitosamente"

