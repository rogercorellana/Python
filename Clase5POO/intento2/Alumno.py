from Persona import *


class Alumno(Persona):
    def __init__(self, nombre, materiasList):
        super().__init__(nombre)
        self.__materiasList = materiasList
        # self.__calificaciones = calificaciones


    def getMateriasList(self):
        return self.__materiasList 
    
    def setMateriasList(self,materiasList):
        self.__materiasList = materiasList

    # def getCalificaciones(self):
    #     return self.__calificaciones
    
    # def setCalificaciones(self,calificaciones):
    #     self.__calificaciones = calificaciones


    def verCalificaciones(self,calificaciones):
        return "ok"

    
    materiasList = property(getMateriasList, setMateriasList)
    # calificaciones = property(getCalificaciones, setMateriasList)


    def __str__(self):
        return f"Materias: {self.getListaDeMaterias()}"



 