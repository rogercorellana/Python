from Persona import *

class Maestro(Persona):
    def __init__(self, nombre, cursada, listaDeAlumnos):
        super().__init__(nombre)
        self.listaDeAlumnos = []

        self.___cursada = cursada
        self.___listaDeAlumnos = listaDeAlumnos
        
    def getCursada(self):
        return self.___cursada 
    
    def setCursada(self,cursada):
        self.___cursada = cursada

    def getListaDeAlumnos(self):
        return self.___listaDeAlumnos 
    
    def setListaDeAlumnos(self,listaDeAlumnos):
        self.___listaDeAlumnos = listaDeAlumnos

    def mostrarAlumnos(self):
        print("Alumnos: ")
        for alumno in self.listaDeAlumnos:
            print(alumno)

    

    cursada = property(getCursada, setCursada)

    listaDeAlumnos = property(getListaDeAlumnos, setListaDeAlumnos)







    
 