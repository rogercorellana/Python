'''
Crear 3 clases 
persona, maestro, alumno donde maestro y alumno hereden de persona sus atriubutos fundamentales, 
maestro tenga una cursada y uina lista de alumnos y un alumno tenga una lista de materias(diccionario)
donde tenga cursada,nota 

poder ingresar por consola la creacion de un maestro tambien la del alumno y poder mostrar del maestro
cuales son sus alumnos 
del alumno cuales son sus materias y notas 
y poder imprimir por pantalla nombre apellido de maestros y alumnos junto con su clase //si es un maestro o alumno'''


from Persona import *

class Alumno(Persona):
    def __init__(self, nombre, cursadaList):
        super().__init__(nombre)
        self.cursadaList = cursadaList

    def verCursadas(self):
        diccionario = {}
        
        for i in self.cursadaList:
            #capturo nombre materia
            materia = i.nombre
            # si el nombre del alumno esta en cursada.calificacionesAlumnos
            if self.nombre in i.calificacionesAlumnos:
                nota = i.calificacionesAlumnos[self.nombre]
                #agrego
                diccionario[materia] = nota
        return diccionario    


    def __str__(self):
        return self.nombre 

    