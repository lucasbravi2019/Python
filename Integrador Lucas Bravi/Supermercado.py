from Entidades.Carrito import Carrito
from Productos.BDProductos import obtener_productos
productos = obtener_productos()
carrito = Carrito()

def mostrar_productos():
    for producto in productos:
        print(producto.getProducto())

def obtener_producto(nombreProducto):
    for producto in productos:      
        if nombreProducto.lower() in producto.getProducto().lower():
            return producto
def calcular_total(productos):
    total = 0
    for producto in productos:
        total += producto['producto']['precio_producto'] * producto['cantidad']
    print("El total a pagar es de: $" + "{:.2f}".format(total))
def obtener_carrito(productos):
    for producto in productos:
        print("Producto: " + producto['producto']['nombre_producto'])
        print("Precio:  ", "$ " + "{:.2f}".format(producto['producto']['precio_producto']))
        print("Cantidad:" ,producto['cantidad'])

def comprar():
    print("Bienvenido al Supermercado Bravi")
    confirmacion = "s"
    print("\tQue desea llevar?")
    while confirmacion.lower() == "s":
        mostrar_productos()
        productoAgregado = input()
        encontrado = False
        for producto in productos:
            if productoAgregado.lower() in producto.getProducto().lower():
                encontrado = True
                print("\tIndique la cantidad de productos que llevara")
                cantidad = input()
                while not cantidad.isdigit():
                    print("Especifico una cantidad invalida, por favor indique en numeros la cantidad de productos que va a llevar")
                    cantidad = input()
                cantidad = int(cantidad)
                carrito.agregar_producto(obtener_producto(productoAgregado), cantidad)
                print("\tDesea agregar un nuevo producto? S/N")
                confirmacion = input()
                while confirmacion.lower() != "s" and confirmacion.lower() != "n":
                    print("\tOpcion erronea, por favor ingrese S o N")
                    confirmacion = input()
        if not encontrado:
            print("\tEspecifico un producto invalido")
    print("Su carrito es")
    obtener_carrito(carrito.getCarrito())
    calcular_total(carrito.getCarrito())
    print("Desea pagar o cancelar su compra?")
    print("1. Pagar")
    print("2. Cancelar")
    pagar = input()
    while pagar != "1" and pagar != "2":
        print("Especifico un valor invalido. Por favor especifique 1 o 2")
        pagar = input()
    if pagar == "1":
        obtener_carrito(carrito.getCarrito())
        calcular_total(carrito.getCarrito())
        print("Pagado. Gracias por su compra. Vuelva pronto!")
    if pagar == "2":
        print("Cancelado. Desea repetir su compra o salir?")
        print("1. Repetir")
        print("2. Salir")
        repetir = input()
        while repetir != "1" and repetir != "2":
            print("Especifico un valor invalido. Por favor especifique 1 o 2")
            repetir = input()
        if repetir == "1":
            carrito.limpiarCarrito()
            comprar()
        if repetir == "2":
            print("Vuelva pronto!")

comprar()




