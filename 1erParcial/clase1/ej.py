#crear un array de numeros y obtener el menor

# array = [3,4,5,10,5,11,556,121,150]

# def obtenerMenor(array):
#     menor = array[0]
#     for i in array:
#         if i <= menor:
#             menor = i
#     return f"El numero menor es: {menor}"

# print(obtenerMenor(array))


#ingresar por teclado un array de numeros y obtener el mayor

# arrayMayor = []
# ingresoWhile = 0

# while ingresoWhile == 0:
#     numeroIngresado = int(input("ingrese un numero: "))
#     arrayMayor.append(numeroIngresado)
#     ingresoWhile = int(input("desea continuar?   \n 0 para si \n 1 para no\n"))
     

# mayor = arrayMayor[0]
# for i in arrayMayor:
#     if mayor < i:
#         mayor = i
    

# print(arrayMayor)
# print(mayor)




#ingresar por consola un numero de dos cifras y averiguar si es multiplo de 3 y de 5 a la vez

# numDosCifras = int(input("Ingresar un numero: "))

# if numDosCifras % 3 == 0 and numDosCifras % 5 == 0:
#     print(f"{numDosCifras} es multiplo de 3 y 5")
# else:
#     print(f"{numDosCifras} no es multiplo de 3 ni de 5")


#ingresar por teclado una matriz de 3x3 y mostrarla por pantalla

# matriz3x3 = []

# for i in range(3):
#     filadelamatriz = []
#     for j in range(3):
#         valor = int(input("Ingresar un numero: "))
#         filadelamatriz.append(valor)
#     matriz3x3.append(filadelamatriz)
        


    

# print(matriz3x3)

# for i in matriz3x3:
#     print(i)


#crear un array de numeros y obtener el menor

array = [111,2,3,6,11]

menor = array[0]
for i in array:
    if i < menor:
        menor = i

print(menor)