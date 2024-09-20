# Dada una lista de números, invierte el orden de los elementos.

print("""
1) Dada una lista de números, invierte el orden de los elementos.
      """)

lista1 = ["papita","pepita","manteca","azucar"]
lista1invertida = []

for i in lista1:
    lista1invertida.insert(0,i)

print(f"la lista normal es : {lista1}")
print(f"la lista invertida es : {lista1invertida}")


# Dada una lista, elimina los elementos duplicados y devuelve la lista sin duplicados.

print("""
2) Dada una lista, elimina los elementos duplicados y devuelve la lista sin duplicados.
      """)

lista2 = ["azucar","flores","muchos colores","azucar","papita","flores"]
lista2nueva = []

for i in lista2:
    if i not in lista2nueva:
        lista2nueva.append(i)

print(lista2nueva)


# Escribe una función que reciba una lista de números y devuelva la suma de todos los elementos.

print("""
3) Escribe una función que reciba una lista de números y devuelva la suma de todos los elementos.
      """)

lista3 = [2,2,4,2,10,2]

def sumaTotalDeLaLista(lista):
    acumulador3 = 0
    for i in lista:
        acumulador3 = acumulador3 + i
    return acumulador3

print(sumaTotalDeLaLista(lista3))

# Dada una tupla, conviértela en una lista.

print("""
4) Dada una tupla, conviértela en una lista.
      """)

tupla4 = ("papa","zanahoria","cebolla","tomate")
lista4 = []

for i in tupla4:
    lista4.append(i)


print(lista4)



# Itera sobre las claves y valores de un diccionario e imprime cada uno de ellos.

print("""
5) Itera sobre las claves y valores de un diccionario e imprime cada uno de ellos.
      """)

diccionario5 = {
    "nombre" : "rodrigo",
    "apellido" : "gomez",
    "dni" : 95673281
}

claves5 = list(diccionario5.keys())


for i in claves5:
    print(f" clave: {i}      valor: {diccionario5[i]}")


# Escribe una función que cuente cuántos pares clave-valor tiene un diccionario.

print("""
6) Escribe una función que cuente cuántos pares clave-valor tiene un diccionario.
      """)


diccionario6 = {
    "remera" : "rosa",
    "origen" : "nacional",
    "cantidad" : 3
}

def cantClaveValor(diccionario):
    acumuladorClaveValor = 0
    for i in diccionario:
        acumuladorClaveValor = acumuladorClaveValor + 1
    return acumuladorClaveValor

print("Cantidad clave valor:  ", cantClaveValor(diccionario6))



