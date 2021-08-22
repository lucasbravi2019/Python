class Producto:
    def __init__(self, nombre, precio):
        self.__nombreProducto = str(nombre)
        self.__precioProducto = float(precio)
    def getProducto(self):
        return self.__nombreProducto
    def getPrecio(self):
        return self.__precioProducto
    def __str__(self):
        return "{ producto: " + self.__nombreProducto + ", precio: " + str(self.__precioProducto) + " }"

    

