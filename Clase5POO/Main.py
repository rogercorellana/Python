from Alumno import *
from Maestro import *
from Persona import * 

alumno1 = Alumno("Juan")

alumno1.listaDeMaterias = {"Matemáticas": 85, "Física": 90}

print (alumno1)


for c in alumno1.listaDeMaterias:
    print(c)
# alumno2 = Alumno("Pepito",{
#                            "matematicas" : 23,
#                            "fisica" : 51
#                            })
maestro = Maestro("Roro","matematicas",alumno1)

maestro.mostrarAlumnos()


