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
from Alumno import * 
from Maestro import * 
from Cursada import *


maestro1 = Maestro("lucia", None)
maestro2 = Maestro("balich", None)
alumno1 = Alumno("roger", None)
alumno2 = Alumno("pepito", None)

cursada1 = Cursada("matematica",maestro1,[alumno1,alumno2], {alumno1.nombre : 9, alumno2.nombre : 5})
cursada2 = Cursada("fisica",maestro2,[alumno1,alumno2], {alumno1.nombre : 3, alumno2.nombre : 5})

maestro1.cursada = cursada1
maestro2.cursada = cursada2

alumno1.cursadaList = [cursada1,cursada2]
alumno2.cursadaList = [cursada1]



print(cursada1)
print(cursada2)

print(alumno1)

print(alumno1.verCursadas())

