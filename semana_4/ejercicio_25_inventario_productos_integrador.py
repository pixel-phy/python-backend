"""Inventario de productos
Una tienda necesita gestionar su inventario. Cada producto es un diccionario con:
- nombre
- precio
- stock
- categoria

1. Mostrar todos los productos con su información.
2. Filtrar productos con stock < 30 (productos por agotarse).
3. Filtrar productos de la categoría "electronica" con precio > 50.
4. Ordenar productos por precio (de menor a mayor).
5. Calcular el valor total del inventario (precio * stock sumado para todos).
6. Agregar un nuevo producto (pide los datos por consola).
7. Mostrar el inventario actualizado después de agregar."""

inventario = [
    {"nombre": "laptop", "precio": 800, "stock": 10, "categoria": "electronica"},
    {"nombre": "mouse", "precio": 25, "stock": 50, "categoria": "electronica"},
    {"nombre": "camiseta", "precio": 20, "stock": 100, "categoria": "ropa"},
    {"nombre": "libro python", "precio": 45, "stock": 30, "categoria": "libros"},
    {"nombre": "teclado", "precio": 60, "stock": 20, "categoria": "electronica"},
    {"nombre": "pantalon", "precio": 40, "stock": 40, "categoria": "ropa"}
]
# Mostrar productos con información
print("\nProductos:")
for i in inventario:
    print(i)

# Productos con stock < 30
filtro = [p for p in inventario if p["stock"] < 30]
print("\nProductos con stock < 30:")
for p in filtro:
    print(f"{p['nombre']}: {p['stock']}")

# Productos de electrónica precio > 50
electronica = [p for p in inventario if p["categoria"] == "electronica" and p["precio"] > 50]
print("\nProductos de electrónica con precio > 50:")
for p in electronica:
    print(f"{p['nombre']}: {p['precio']}")

# Ordenar por precio (de menor a mayor)
inventario.sort(key=lambda x : x["precio"])
print("\nDe menor a mayor precio: ")
for a in inventario:
    print(f"{a['nombre']}: {a['precio']}")

# Valor total del inventario actual
total_inventario = 0
for i in inventario:
    total_inventario += i["precio"] * i["stock"]
print(f"\nValor total del inventario: {total_inventario}")

# Agregar nuevo producto
print("\n--- Agregar nuevo producto ---")
while True:
    nombre = input("Nombre: ").strip().lower()
    if nombre == "":
        print("Ingrese un nombre válido.")
        continue
    else:
        break
while True:
    try:
        precio = float(input("Precio: "))
        if precio < 0:
            raise ValueError ("El precio debe ser mayor que 0")
        else:
            break
    except ValueError as e:
        print(f"Error: {e}")
        continue
while True:
    try:
        stock = int(input("Stock: "))
        if stock < 0:
            raise ValueError ("El stock debe ser mayor que 0")
        else:
            break
    except ValueError as e:
        print(f"Error: {e}")
        continue

categoria = ["electronica", "ropa", "libros"]
while True:
    entrada_categoria = input("Categoria: ").strip().lower()
    if entrada_categoria not in categoria:
        print("\nEscriba una categoría válida (electronica, ropa, libros)")
        continue
    else:
        break

nuevo_producto = {
    "nombre": nombre,
    "precio": precio,
    "stock": stock,
    "categoria": entrada_categoria
}
inventario.append(nuevo_producto)

#Mostramos inventario actualizado
print("\nInventario actualizado: ")
for p in inventario:
    print(f"{p['nombre']}: ${p['precio']} ({p['stock']} en stock) categoria: {p['categoria']}")
