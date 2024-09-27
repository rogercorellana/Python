# Crear la clase biblioteca que tenga una coleccion de libros que contenga un metodo para ordernarlos por nombres e imprimilos por pantalla y otro metodo que me devuelva cual es el libro mas viejo de la biblioteca y la clase libro, que va a tener como atributos, nombre, autor, fecha de publicacion y sobreescribir el metodo __str__ para devolver todas las propiedades por pantalla. 


class Biblioteca:
    def __init__(self,librosList):
        self.librosList = librosList

    def obtenerNombres(self):
        arraynombre = []
        for i in self.librosList:
            arraynombre.append(i.nombre)

        return arraynombre
    

    def ordenarLibrosPorNombre(self):
        array = self.obtenerNombres()
        array.sort()
        return array
            


        
    
    def obtenerLibroMasViejo(self):
        libroMasViejo = self.librosList[0]
        
        for i in self.librosList:
            if i.añoPublicacion < libroMasViejo.añoPublicacion:
                libroMasViejo = i 

        return libroMasViejo
            



    def __str__(self):
        libros = ""
        for i in self.librosList:
            libros = libros + str(i)
        return libros
    
