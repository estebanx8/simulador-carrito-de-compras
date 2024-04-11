
# Carrito de Compras

Este es un carrito de compras simple que permite agregar, eliminar y ver productos comprados, así como calcular el total de precios. También permite guardar los productos comprados en un archivo de texto y cargarlos desde allí.

**Clases**

- `Producto`: Representa un producto con un nombre y un precio.
- `CarritoDeCompras`: Representa un carrito de compras con una lista de productos y métodos para agregar, eliminar y ver productos, así como calcular el total de precios y guardar y cargar productos comprados desde un archivo de texto.

**Métodos**

- `agregar_producto(producto)`: Agrega un producto al carrito de compras.
- `eliminar_producto(nombre_producto)`: Elimina un producto del carrito de compras según su nombre.
- `obtener_total_precio()`: Calcula y devuelve el total de precios de los productos en el carrito de compras.
- `guardar_productos_comprados()`: Guarda los productos comprados en un archivo de texto.
- `cargar_productos_comprados()`: Carga los productos comprados desde un archivo de texto.

### Ejemplo de uso

El siguiente código muestra un ejemplo de uso del carrito de compras:
```
# Productos de ejemplo
producto1 = Producto("Producto 1", 10)
producto2 = Producto("Producto 2", 20)
producto3 = Producto("Producto 3", 30)

# Crear un carrito de compras
carrito = CarritoDeCompras()

# Agregar productos al carrito de compras
carrito.agregar_producto(producto1)
carrito.agregar_producto(producto2)
carrito.agregar_producto(producto3)

# Ver total de precios
print("Total de precios:", carrito.obtener_total_precio())

# Eliminar un producto del carrito de compras
carrito.eliminar_producto("Producto 2")

# Ver productos comprados
for producto in carrito.productos:
    print(producto.nombre, "-", "$", producto.precio)

Guardar productos comprados en un archivo de texto
carrito.guardar_productos_comprados()

## Cargar productos comprados desde un archivo de texto
carrito.cargar_productos_comprados()
```
## Menú de opciones

El código también incluye un menú de opciones que permite al usuario interactuar con el carrito de compras a través de un menú de texto. 
El menú incluye las siguientes opciones:

+ Agregar producto
- Eliminar producto
* Ver total de precios
- Ver productos comprados
+ Guardar productos comprados
* Salir
### ***El usuario puede elegir una opción ingresando su número correspondiente. Si el usuario ingresa una opción inválida, se muestra un mensaje de error.***
