from Persona import *

class Maestro(Persona):
    def __init__(self, nombre, materiasList):
        super().__init__(nombre)
        self.__materiasList = materiasList

    def getMateriasList(self):
        return self.__materiasList 
    
    def setMateriasList(self,materiasList):
        self.__materiasList = materiasList



    def calificarAlumno(self, Cursada):
        print("Calificando Alumno.... ")
        

    

    materiasList = property(getMateriasList, setMateriasList)








    
 