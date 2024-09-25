from Gato import Gato
from Perro import Perro
from Vaca import Vaca
from Animal import Animal


size = 20
arr = [0] * size

gato1 = Gato(1)
perro1 = Perro(1)
vaca1 = Vaca(1)

gato1.setPosicion = 1
perro1.setPosicion = 1
vaca1.setPosicion = 1

print(gato1.mover(arr,3))



