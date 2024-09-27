# Escribe una función llamada es_palindromo que reciba una cadena de texto como parámetro y devuelva True si la cadena es un palíndromo (se lee igual de adelante hacia atrás), y False en caso contrario.

def esPalindromo(cadena):
    value = True
    longitud = len(cadena)


    for i in range(longitud // 2):
        if cadena[i] != cadena[longitud - i - 1]:
            value = False



    return value


print(esPalindromo("reconocer"))