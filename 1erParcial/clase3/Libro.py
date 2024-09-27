# Crear la clase biblioteca que tenga una coleccion de libros que contenga un metodo para ordernarlos por nombres e imprimilos por pantalla y otro metodo que me devuelva cual es el libro mas viejo de la biblioteca y la clase libro, que va a tener como atributos, nombre, autor, fecha de publicacion y sobreescribir el metodo __str__ para devolver todas las propiedades por pantalla. 


class Libro:
    def __init__(self,nombre,autor,añoPublicacion):
        self.nombre = nombre
        self.autor = autor
        self.añoPublicacion = añoPublicacion

    def __str__(self):
        return f" nombre: {self.nombre}, autor: {self.autor}, añoPublicacion: {self.añoPublicacion} "
    
    