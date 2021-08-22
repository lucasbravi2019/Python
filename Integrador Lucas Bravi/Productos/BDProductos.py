from Entidades.Producto import Producto 
productos = []
def obtener_productos():
    productos.append(Producto("Aceite", 15.4))
    productos.append(Producto("Sal", 10.2))
    productos.append(Producto("Asado", 150.54))
    productos.append(Producto("Lechuga", 25.99))
    productos.append(Producto("Tomate", 9.99))
    productos.append(Producto("Pan", 5.35))
    productos.append(Producto("Coca Cola", 33.12))
    productos.append(Producto("Cerveza", 30.45))
    return productos