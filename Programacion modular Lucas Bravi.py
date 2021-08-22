# Hacer un programa que permita a un comercio registrar los precios de 10 productos, para esto deberá guardar en una lista los precios de lista de los productos. Además de la lista de precios se debe contar con una segunda lista que registre los precios de promoción. La promoción consiste en precio de lista con un 15% de descuento. Para esto se deberá contar con las siguientes funciones:
# * CargaPrecio (carga los precios de lista).
# * CargaPromo (la función debe cargar la segunda lista, esto se logra leyendo de la primera el precio y se le aplica el descuento. Ese valor se guarda en la segunda lista).
# * MuestraPrecios (la función muestra por pantalla tanto el precio de lista como el de promoción).
def cargarPrecios(productos):
    for i in range(10):
        print("Ingrese el precio de lista")
        precio_lista = float(input())
        productos.append(precio_lista)

def cargaPromo(productos, productos_descuento):
    for i in productos:
        productos_descuento.append(i * .85)

def muestraPrecios(productos, productos_descuento):
    print("Precios lista")
    for i in productos:
        print("$ ", "{:.2f}".format(i))
    print("Precios con descuento")
    for i in productos_descuento:
        print("$ ", "{:.2f}".format(i))

productos = []
productos_descuento = []
cargarPrecios(productos)
cargaPromo(productos, productos_descuento)
muestraPrecios(productos, productos_descuento)