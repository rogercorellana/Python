from Animal import *
from Gato import *
from Perro import *

camino = [0] * 10

gato1 = Gato(1,"negro")
perro1 = Perro(3,"pitbul")

camino[gato1.posicion] = "gato"
camino[perro1.posicion] = "perro"

print(camino)

print(gato1.moverse(camino,1))
print(gato1.moverse(camino,10))

print(gato1.interactuar(camino,perro1))
