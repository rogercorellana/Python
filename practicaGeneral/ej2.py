# Ejercicio 2: Números pares
# Escribe una función llamada numeros_pares que reciba un número entero positivo n como parámetro y devuelva una lista con todos los números pares desde 0 hasta n (incluyendo n si es par).

def numerosPares(num1):
    lista = []
    for i in range(1,num1+1,1):
        if i % 2 == 0:
            lista.append(i)
    return lista    
  

print(numerosPares(9)) #2,4,6,8
print(numerosPares(10))    #2,4,6,8,10