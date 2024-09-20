
# Dada una lista de números, invierte el orden de los elementos.

print("Dada una lista de números, invierte el orden de los elementos")
numeros = [1,2,3,4,3,5,6]
#numeros.reverse()
#print(numeros)

numerosTamaño = len(numeros)
numerosInvertidos = [] * numerosTamaño

for i in numeros:
    numerosInvertidos.insert(0, i)

print(numerosInvertidos)


# Dada una lista, elimina los elementos duplicados y devuelve la lista sin duplicados.

lista1 = [1,2,2,3,4,5,6,6,7,99]
lista2 = []

for i in lista1:
    if i not in lista2:
        lista2.append(i)
print(lista2)


# Escribe una función que reciba una lista de números y devuelva la suma de todos los elementos.
lista3 = [1,2,3]

def sumaTotal(lista3):
    suma = 0
    for i in lista3:
        suma = suma + i
    return suma

print(sumaTotal(lista3))

# Dada una tupla, conviértela en una lista.

#TUPLA es un array q no se puede modificar es UNA LISTA INMUTABLE
tupla=("pablito","comio","papita",True,56)
lista4 = []

for i in tupla:
    lista4.append(i)

print(lista4)


#Itera sobre las claves y valores de un diccionario e imprime cada uno de ellos
print("Itera sobre las claves y valores de un diccionario e imprime cada uno de ellos")
diccionario = {
    'nombre' : "roro",
    'altura' : 171,
    'dato duplicado' : "soy roro"
}

print(diccionario.items())

for i,j in diccionario.items():
    print(f"{i} - {j}")
    





#Escribe una función que cuente cuántos pares clave-valor tiene un diccionario
print("Escribe una función que cuente cuántos pares clave-valor tiene un diccionario.")

diccionario2 = {
    'nombre' : "roro",
    'altura' : 171,
    'dato duplicado' : "soy roro"
}

contador2 = 0
for i in diccionario2:
    contador2 = contador2 + 1

print(contador2)


