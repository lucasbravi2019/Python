class Carrito:
    def __init__(self):
        self.__productos = []
    def agregar_producto(self, producto, cantidad):
        self.__productos.append({
            "producto": {
                'nombre_producto': producto.getProducto(),
                'precio_producto': producto.getPrecio()
            },
            "cantidad": cantidad
            })
    def getCarrito(self):
        return self.__productos
    def limpiarCarrito(self):
        self.__productos = []
    def __str__(self):
        string = ""
        for i in range(0, len(self.__productos)):
            if i < len(self.__productos) - 1: 
                string += str(self.__productos[i]) + "\n"
            else:    
                string += str(self.__productos[i]) 
        return string