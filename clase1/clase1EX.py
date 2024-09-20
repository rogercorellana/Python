#crear un array de numeros y obtener el menor
#ingresar por teclado un array de numeros y obtener el mayor
#ingresar por consola un numero de dos cifras y averiguar si es multiplo de 3 y de 5 a la vez
#ingresar por teclado una matriz de 3x3 y mostrarla por pantalla


#crear un array de numeros y obtener el menor
array = [12,1,66,32]
array.sort()
print(f"primer valor array ordenado {array[0]}")

array2 = [12,100,66,1]
minimo = array2[0]

for e in array2:
    if e < minimo:
        minimo = e
print("segundo ordenado")
print(minimo)


#funcion para calcular minimos
def encontrarMinimos(arrayRecibido):
    minimo = arrayRecibido[0]

    for e in arrayRecibido:
        if e < minimo:
            minimo = e

    return minimo


arrayFuncion = [15,66,88,23,3,2]
print(f"usando la funcion {arrayFuncion} y ordenando el array : el minimo es: {encontrarMinimos(arrayFuncion)} ----")

print(encontrarMinimos(arrayFuncion))



#ingresar por teclado un array de numeros y obtener el mayor

# datoEntrada = 0
# array4 = []

# while(datoEntrada == 0):
#     dato1 = int(input("ingrese un numero: "))
#     array4.append(dato1)
#     datoEntrada = int(input("Ingrese 0 para seguir cargando numeros: "))

# print(array4)

# def calcularMayor(array4bis):
#     mayor = array4bis[0]
#     for e in array4bis:
#         if e > mayor:
#             mayor = e
#     return mayor

# print(calcularMayor(array4))




#ingresar por consola un numero de dos cifras y averiguar si es multiplo de 3 y de 5 a la vez

# numeroIngresado = int(input("INGRESE UN NUMERO: "))

# if numeroIngresado%3 == 0 and numeroIngresado%5 == 0:
#     print("es multiplo de 3 y 5")
# elif numeroIngresado%3 == 0:
#     print("es multiplo unicamente de 3")
# elif numeroIngresado%5 == 0:
#     print("es multiplo unicamente de 5")
# else:
#     print("el numero ingresado no es multiplo de 3 ni de 5")





#ingresar por teclado una matriz de 3x3 y mostrarla por pantalla

print("cargue nueve valores para llenar una matriz 3x3")
matriz = []

for index in range (1,10,1):
    cargarMatriz = int(input(f"ingrese el {index} valor : "))
    matriz.append(cargarMatriz)

print(matriz)

###


# Inicializar una matriz vacía
matriz = []

# Bucle para ingresar los valores de la matriz
for i in range(3):  # Para cada fila (3 filas)
    fila = []  # Crear una nueva lista para la fila actual
    for j in range(3):  # Para cada columna en la fila (3 columnas)
        valor = int(input(f"Ingrese el valor para la posición [{i+1}][{j+1}]: "))
        fila.append(valor)  # Agregar el valor a la fila
    matriz.append(fila)  # Agregar la fila completa a la matriz

# Imprimir la matriz ingresada
print("Matriz ingresada:")
for fila in matriz:
    print(fila)



