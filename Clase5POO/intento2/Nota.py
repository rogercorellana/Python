

class Nota:
    def __init__(self, cursada, notasAlumnos, alumnosList):
        self.__cursada = cursada
        self.__notasAlumnos = notasAlumnos
        self.__alumnosList = alumnosList


    def getNombre(self):
        return self.__cursada 
    
    def setNombre(self,cursada):
        self.__cursada = cursada

    def getNotasAlumnos(self):
        return self.__notasAlumnos 
    
    def setNotasAlumnos(self,notasAlumnos):
        self.__notasAlumnos = notasAlumnos

    def getAlumnosList(self):
        return self.__alumnosList 
    
    def setAlumnosList(self,alumnosList):
        self.__alumnosList = alumnosList



    cursada = property(getNombre, setNombre)
    notasAlumnos = property(getNotasAlumnos, setNotasAlumnos)
    alumnosList = property(getAlumnosList, setAlumnosList)

        







    
 