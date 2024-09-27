from Animal import *
from Gato import *
from Perro import *
from Vaca import *

gato1 = Gato(3)
perro1 = Perro(4)

camino = [0] * 10

print(camino)

camino[gato1.getPosicion()-1] = "gato"
camino[perro1.getPosicion()-1] = "perro"

print(camino)

print(gato1)
print(perro1)

print(gato1.mover(camino,4))
print(camino)


print(perro1.mover(camino,3))

print(camino)

print(perro1.getPosicion())

print(camino)
print(gato1.mover(camino,3))

print(gato1.getPosicion())
print(gato1.interractuar(perro1))
print(camino)


vaca1 = Vaca(1)
camino[vaca1.getPosicion()-1] = "vaca"
print(camino)
print(vaca1.mover(camino,1))
print(vaca1.mover(camino,6))
print(camino)
print(vaca1.interractuar(gato1))
print(vaca1)