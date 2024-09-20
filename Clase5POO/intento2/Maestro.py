from Persona import *
from Nota import *

class Maestro(Persona):
    def __init__(self, nombre, materiasList):
        super().__init__(nombre)
        self.__materiasList = materiasList

    def getMateriasList(self):
        return self.__materiasList 
    
    def setMateriasList(self,materiasList):
        self.__materiasList = materiasList



    def calificarAlumno(self, Alumno, Materia, nota):

        print("Calificando Alumno.... ")
        if Materia in self.materiasList:
            print("el maestro si puede calificar al alumno")
        else:
            print("el maestro no da clases en la materia")


        def crearNota(self, Alumno, Materia, nota):
            nota1 = Nota(
                materia= Materia,
                alumno= Alumno,
                calificacion= nota
            )
            Materia.notasAlumnos.append(nota1)
            Alumno.notasList.append(nota1)
        
        crearNota(self, Alumno, Materia, nota)
        print("Calificacion subida exitosamente")
        

    def __str__(self):
        materias__str = ""
        
        for materia in self.materiasList:
            materias__str = materias__str + str(materia) + "\n"    
        
        return f"Nombre: {self.nombre}, Materias Asignadas: {materias__str}"
        
        

    

    materiasList = property(getMateriasList, setMateriasList)








    
 