

class Nota:
    def __init__(self, materia, alumno, calificacion):
        self.__materia = materia
        self.__alumno = alumno
        self.__calificacion = calificacion


    def getNombre(self):
        return self.__materia 
    
    def setNombre(self,materia):
        self.__materia = materia

    def getAlumno(self):
        return self.__alumno 
    
    def setAlumno(self,alumno):
        self.__alumno = alumno

    def getCalificacion(self):
        return self.__calificacion 
    
    def setCalificacion(self,calificacion):
        self.__calificacion = calificacion

    
    def __str__(self):
        return f"\nMateria: {self.__materia.getNombre()}, Alumno: {self.__alumno.getNombre()}, Calificación: {self.__calificacion}\n"



    materia = property(getNombre, setNombre)
    alumno = property(getAlumno, setAlumno)
    calificacion = property(getCalificacion, setCalificacion)

        







    
 