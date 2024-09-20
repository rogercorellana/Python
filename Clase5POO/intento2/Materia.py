

class Materia:
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

    #toString
    
    def __str__(self):
        alumnos_str = ""
        nota_str = ""
        for alumno in self.alumnosList:
            alumnos_str = alumnos_str + str(alumno) + "\n"
        for nota in self.notasAlumnos:
            nota_str = nota_str + str(nota) + "\n"


        return f"Nombre: {self.__nombre}, NotasAlumnos: {nota_str}, AlumnosList: {alumnos_str}"



    nombre = property(getNombre, setNombre)
    notasAlumnos = property(getNotasAlumnos, setNotasAlumnos)
    alumnosList = property(getAlumnosList, setAlumnosList)

        







    
 