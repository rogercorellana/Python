from Persona import *




class Alumno(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

        self__listaDeMaterias = {}
        
    def getListaDeMaterias(self):
        return self.__listaDeMaterias 
    
    def setListaDeMaterias(self, listaDeMaterias):
    
        self.__listaDeMaterias = listaDeMaterias

    
    listaDeMaterias = property(getListaDeMaterias, setListaDeMaterias)


    def __str__(self):
        return f"Materias: {self.getListaDeMaterias()}"



 