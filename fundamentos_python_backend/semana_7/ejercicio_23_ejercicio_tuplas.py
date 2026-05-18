"""Ejercicio corto de tuplas
Una tienda tiene productos con dódigo, nombre y precio. Usa una tupla para cada producto.
producto1 = (101, "Laptop", 800)
producto2 = (102, "Mouse", 25)
producto3 = (103, "Teclado", 60)
Requisitos:
1. Crear una lista de tuplas con los 3 productos.
2. Recorrer la lista y mostrar cada producto con formato: "101 - Laptop - $800".
3. Buscar un producto por código (pedir código al usuario) y mostrar su nombre y precio.
4. Intentar modificar el precio de un producto directamente."""

# Lista de tuplas:
lista = [(101, "Laptop", 800), (102, "Mouse", 25), (103, "Teclado", 60)]

# Recorrer la lista y mostrar formato
for tupla in lista:
    print(f"{tupla[0]} - {tupla[1]}: ${tupla[2]}")

# Pedir código al usuario y mostrar información del producto
codigo = input("Código de artículo: ").strip()
for tupla in lista:
    if int(codigo) == tupla[0]:
        print(f"{tupla[1]}: ${tupla[2]}")
        break
else:
    print("Código de artículo no encontrado.")

# Intento de modificación de precio
try: 
    lista[0][2] = 600
except (TypeError, ValueError):
    print("No es posible modificar elementos de una tupla.")