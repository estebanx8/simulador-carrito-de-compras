import os

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class CarritoDeCompras:
    def __init__(self):
        self.productos = []
        self.archivo = "productos_comprados.txt"

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, nombre_producto):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                self.productos.remove(producto)
                return
        print("Producto no encontrado")

    def obtener_total_precio(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total

    def guardar_productos_comprados(self):
        with open(self.archivo, "a") as archivo:
            for producto in self.productos:
                archivo.write(f"{producto.nombre} - ${producto.precio}\n")

    def cargar_productos_comprados(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as archivo:
                for linea in archivo:
                    nombre, precio = linea.strip().split(" - $")
                    self.productos.append(Producto(nombre, float(precio)))

# Productos de ejemplo
producto1 = Producto("Producto 1", 10)
producto2 = Producto("Producto 2", 20)
producto3 = Producto("Producto 3", 30)

# Crear un carrito de compras
carrito = CarritoDeCompras()

# Cargar productos comprados desde el archivo
carrito.cargar_productos_comprados()

# Menú principal
while True:
    print("\nMenú del carrito de compras:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Ver total de precios")
    print("4. Ver productos comprados")
    print("5. Guardar productos comprados")
    print("6. Salir")

    opcion = int(input("Ingrese su opción: "))

    if opcion == 1:
        print("\nProductos disponibles:")
        print("1. Producto 1 ($10)")
        print("2. Producto 2 ($20)")
        print("3. Producto 3 ($30)")

        opcion_producto = int(input("Ingrese el número del producto: "))

        if opcion_producto == 1:
            carrito.agregar_producto(producto1)
        elif opcion_producto == 2:
            carrito.agregar_producto(producto2)
        elif opcion_producto == 3:
            carrito.agregar_producto(producto3)
        else:
            print("Número de producto inválido")

    elif opcion == 2:
        nombre_producto = input("Ingrese el nombre del producto que desea eliminar: ")
        carrito.eliminar_producto(nombre_producto)

    elif opcion == 3:
        print("Total de precios:", carrito.obtener_total_precio())

    elif opcion == 4:
        for producto in carrito.productos:
            print(producto.nombre, "-", "$", producto.precio)

    elif opcion == 5:
        carrito.guardar_productos_comprados()

    elif opcion == 6:
        print("Saliendo del carrito de compras")
                print(""" by
 ▄▄▄██▀▀▀▓█████▄▄▄█████▓  ▄████ 
   ▒██   ▓█   ▀▓  ██▒ ▓▒ ██▒ ▀█▒
   ░██   ▒███  ▒ ▓██░ ▒░▒██░▄▄▄░
▓██▄██▓  ▒▓█  ▄░ ▓██▓ ░ ░▓█  ██▓
 ▓███▒   ░▒████▒ ▒██▒ ░ ░▒▓███▀▒
 ▒▓▒▒░   ░░ ▒░ ░ ▒ ░░    ░▒   ▒ 
 ▒ ░▒░    ░ ░  ░   ░      ░   ░ 
 ░ ░ ░      ░    ░      ░ ░   ░ 
 ░   ░      ░  ░              ░ 
""")
        break

    else:
        print("Opción inválida")
