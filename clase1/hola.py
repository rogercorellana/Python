print (2 + 2)

#tipos de datos

datos = "string"

datos = """tus datos son
        nombre :roger
        edad :26"""

print(datos)

40
40.2
True,False


#concatenar strings

nombre = "roger"
#concatenar con +
bienvenida = "hola " + nombre + " como estas?"

print(nombre)
print(bienvenida)

#concatenar con f string, toma un dato y lo convierte a string
nombre = "cosita"
num = 222
bienvenida = f"hola {nombre} como estas? tenes {num} pesos?"
print(bienvenida)


#borrar variables
del num
del nombre

#print(num)
print(bienvenida)

#buscar si algo existe o no en una variable, asumiendo premisas correctas
print("cosita" in bienvenida)
print("cosita" not in bienvenida)


#LISTAS

array=["roger","peedrito","papita",True,56]
print(array)
print(array[4])
array[0] = "daniel"
print(array[0])

#TUPLA es un array q no se puede modificar
tupla=("pablito","comio","papita",True,56)
print(tupla)
print(tupla[0])
#tupla[0] = 22  #NO ME VA DEJAR
#tupla = ("pepe","grillo")

#CONJUNTO, puedo redefinirla entera pero tampoco puedo modificar sus indices
conjunto = {"primerConjunto", 56, 22, True}
conjunto = {"pie"}
print(conjunto)
#print(conjunto[1])     no puedo accedder por indice tampoco repetir datos

#DICCIONARIO = {clave : valor}

diccionario = {
    'nombre' : "roro",
    'altura' : 171,
    'dato duplicado' : "soy roro"
}

print(diccionario["nombre"])
print(diccionario["dato duplicado"])


#operadores aritmeticos +-*/ 
# % devuelve resto de la division
# ** exponente 
# 7//3 me quedo con el entero la parte decimas la deja

#condicionales
datoA = "papita"
datoB = "pepito"

if datoA == datoB:
    print("correcto")
else:
    print("incorrecto")


#else if, si primera condicion no se cumplo voy a elif sino sigo,

ingreso = 100000
gastoMensual = 500
if ingreso > 10000:
    print("sos rico")
    if gastoMensual > 499:
        print("deja de gastar tanto")
    else:
        print("no gastas lo suficiente")

elif ingreso > 500:
    print("sos sudaca")
else:
    print("sos re pobre ")

##operadores and(*) & or(+) | not (!) 