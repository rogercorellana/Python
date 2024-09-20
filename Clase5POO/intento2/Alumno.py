from Persona import *


class Alumno(Persona):
    def __init__(self, nombre, notasList):
        super().__init__(nombre)
        self.__notasList = notasList



    def getNotasList(self):
        return self.__notasList 
    
    def setNotasList(self,notasList):
        self.__notasList = notasList

    
    #toString
    def __str__(self):
        notas__str = ""
        for notas in self.notasList:
            notas__str = notas__str + str(notas)

        return f"Nombre: {self.nombre}, Notas: {notas__str}"


    # def verCalificaciones(self):
        
    #     calificaciones = {}
        
    #     for i in self.notasList:
    #         materia_nombre = i.getNombre().getNombre()
    #         calificacion = i.getCalificacion()
    #         calificaciones[materia_nombre] = calificacion

       
            
    #     return calificaciones
    
    
    def verCalificaciones(self):
        calificaciones = {}
        for nota in self.notasList:
            materia_nombre = nota.materia.getNombre()  # Nombre de la materia
            calificacion = nota.calificacion  # Calificación
        
            # Si la materia no está en el diccionario, inicializa una lista
            if materia_nombre not in calificaciones:
                calificaciones[materia_nombre] = [] 
        
            # Agrega la calificación a la lista, sin importar si es repetida
            calificaciones[materia_nombre].append(calificacion) 
    
        return f"Las notas del alumno {self.getNombre()} son: {calificaciones}"


    
    notasList = property(getNotasList, setNotasList)
