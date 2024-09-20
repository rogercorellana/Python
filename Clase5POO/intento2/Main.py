from Alumno import *
from Maestro import *
from Persona import * 
from Materia import *
from Nota import *



cursadaMatematica = Materia(
    nombre="matematicas",
    notasAlumnos=[],
    alumnosList=[]
)

cursadaFisica = Materia(
    nombre="fisica",
    notasAlumnos=[],
    alumnosList=[]
)

alumno1 = Alumno(
    nombre="roger",
    notasList=[]
)
    
maestro1 = Maestro(
    nombre="lucia",
    materiasList=[]
)

maestro1.materiasList.append(cursadaMatematica)
maestro1.materiasList.append(cursadaFisica)

cursadaMatematica.alumnosList.append(alumno1)
cursadaFisica.alumnosList.append(alumno1)


print(cursadaMatematica)

print(alumno1)

print(maestro1)

maestro1.calificarAlumno(alumno1,cursadaMatematica,10)
maestro1.calificarAlumno(alumno1,cursadaFisica,4)

print(cursadaMatematica)

print(alumno1)

print(maestro1)


print(alumno1.verCalificaciones())

maestro1.calificarAlumno(alumno1,cursadaMatematica,8)

print(alumno1.verCalificaciones())

