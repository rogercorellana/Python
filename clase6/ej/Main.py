from Gato import Gato
from Perro import Perro
from Vaca import Vaca
from Animal import Animal

size = 12
grilla = [0] * size

gato1 = Gato(1)
perro1 = Perro(1)
vaca1 = Vaca(1)

gato1.setPosicion(0)
perro1.setPosicion(1)
vaca1.setPosicion(2)

grilla[gato1.getPosicion()] = "gato"
grilla[perro1.getPosicion()] = "perro"
grilla[vaca1.getPosicion()] = "vaca"

print(grilla)
print(grilla[0])
print(gato1.mover(grilla,4))
print(grilla)
print(gato1.interractuar(vaca1))

print(perro1.interractuar(vaca1))
print(vaca1.interractuar(gato1))
print(perro1.interractuar(gato1))
