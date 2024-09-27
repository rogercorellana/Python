# Crear la clase biblioteca que tenga una coleccion de libros que contenga un metodo para ordernarlos por nombres e imprimilos por pantalla y otro metodo que me devuelva cual es el libro mas viejo de la biblioteca y la clase libro, que va a tener como atributos, nombre, autor, fecha de publicacion y sobreescribir el metodo __str__ para devolver todas las propiedades por pantalla. 

from Libro import *
from Biblioteca import * 

libro1 = Libro("patito feo","roro",2000)
libro2 = Libro("abc","ariel",1030)
libro3 = Libro("barba negra","shirojige",2020)

biblioteca1 = Biblioteca([libro1,libro2,libro3])


print(libro1)
print(biblioteca1)

print(biblioteca1.obtenerNombres())

print(biblioteca1.ordenarLibrosPorNombre())

print(biblioteca1.obtenerLibroMasViejo())



