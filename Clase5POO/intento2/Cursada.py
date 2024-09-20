

class Cursada:
    def __init__(self, nombre, notasAlumnos, alumnosList):
        self.__nombre = nombre
        self.__notasAlumnos = notasAlumnos
        self.__alumnosList = alumnosList


    def getNombre(self):
        return self.__nombre 
    
    def setNombre(self,nombre):
        self.__nombre = nombre

    def getNotasAlumnos(self):
        return self.__notasAlumnos 
    
    def setNotasAlumnos(self,notasAlumnos):
        self.__notasAlumnos = notasAlumnos

    def getAlumnosList(self):
        return self.__alumnosList 
    
    def setAlumnosList(self,alumnosList):
        self.__alumnosList = alumnosList



    nombre = property(getNombre, setNombre)
    notasAlumnos = property(getNotasAlumnos, setNotasAlumnos)
    alumnosList = property(getAlumnosList, setAlumnosList)

        







    
 