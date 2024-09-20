from Alumno import *
from Maestro import *
from Persona import * 
from Cursada import *
from Nota import *



cursadaMatematica = Cursada(
    nombre="matematicas",
    notasAlumnos=[],
    alumnosList=[]
)

cursadaFisica = Cursada(
    nombre="fisica",
    notasAlumnos=[],
    alumnosList=[]
)

alumno1 = Alumno(
    nombre="roger",
    materiasList=[cursadaMatematica, cursadaFisica]
)
    
maestro1 = Maestro(
    nombre="lucia",
    materiasList=[cursadaMatematica]
)

maestro1.calificarAlumno(alumno1, 23)






