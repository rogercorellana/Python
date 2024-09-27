# Escribe una función llamada suma_digitos que reciba un número entero positivo como parámetro y devuelva la suma de sus dígitos.


def sumaDigitos(num1):

    num1str = str(num1)
    acumuladorDeDigitos = 0

    for i in num1str:
        acumuladorDeDigitos += int(i)
    return acumuladorDeDigitos





print(sumaDigitos(12))