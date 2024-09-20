#type() veo tipo de dato

#operadores aritmeticos +-*/ 
# % devuelve resto de la division
# ** exponente 
# 7//3 me quedo con el entero la parte decimas la deja

a = 1
b = 2

print(type(a))

c = "roro "

print(c * 3)

#and or not para condicionales



#concatenar con f string, toma un dato y lo convierte a string
nombre = "RORITO"
num = 10
bienvenida = f"hola {nombre} como estas? tenes {num} pesitos?"
print(bienvenida)



#al declarar variables es posible
a,b = 2,5


#LISTAS
array=["roger","peedrito","papita",True,56]
print(array)
print(array[4])
array[0] = "daniel"
print(array[0])


#matriz, es una lista de listas
lista = [22,True, "una lista", [1,2,"holaRORO"]]
print(lista[3][-1]) #ACCEDO AL ULTIMO CON EL -1


#ejemplo listas 
l = [99, True, "UNA LISTA"]
print(l[0:]) #me trae desde el ppio al final o yo elijo desde q indice

#TUPLA es un array q no se puede modificar es UNA LISTA INMUTABLE
tupla=("pablito","comio","papita",True,56)
print(tupla)
print(tupla[0])
#tupla[0] = 22  #NO ME VA DEJAR
#tupla = ("pepe","grillo")
#es estatico, no modificable, inmutable, tamaño fijo al definirla, ocupa menos memoria solo para eso sirve,



#DICCIONARIO = {clave : valor}

diccionario = {
    "nombre" : "roro RORO roroooooooooooooooooooo",
    'altura' : 171,
    'dato duplicado' : "soy roro"
}

print(diccionario["nombre"])
print(diccionario["dato duplicado"])

diccionario["nombre"] = "PAPITA"
print(diccionario["nombre"])


#FUNCIONES con def y return 

#hacer factorial ejercicio con for, usar libreria time, docstring





