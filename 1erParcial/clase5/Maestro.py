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

class Maestro(Persona):
    def __init__(self, nombre,cursadaAsignada):
        super().__init__(nombre)
        self.cursadaAsignada = cursadaAsignada

    def calificar(self, alumno, nota):
        return "califique"
    
    def verAlumnos(self,materia):
        pass
        




    def __str__(self):
        return super().__str__() + f", cursada asignada: {self.cursadaAsignada}"
    


