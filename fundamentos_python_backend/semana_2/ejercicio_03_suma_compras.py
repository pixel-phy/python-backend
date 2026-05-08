"""Suma de compras:
Un supermercado quiere un programa que sume el total de una compra. El usuario ingresará la cantidad de productos
y el precio de cada uno.

Requisitos:
1. Solicitar la cantidad de productos (número entero positivo).
2. Validar que sea un número entero mayor a 0.
3. Usar for para pedir el precio de cada producto.
4. Acumular la suma total.
5. Mostrar el total de la compra y el promedio por producto.

Validaciones:
1. Cantidad de productos debe ser un número entero positivo (1 o más).
2. Precio de cada producto debe ser un número positivo (puede tener decimales).
3. Si el usuario ingresa un precio negativo o cero, mostrar error y repetir la solicitud para ese producto (sin salir del programa)."""

print("\n=== SUMADOR DE COMPRAS ===\n")

# Inicializamos variables
suma_total = 0.0

# Entrada de cantidad
while True:
    entrada_cantidad = input("¿Cuántos productos? ").strip()
    try:
        cantidad = int(entrada_cantidad)
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")
        break  # Salimos del bucle si es válido
    except ValueError as e:
        print(f"Error: {e}")

# Bucle para cada producto
for i in range(1, cantidad + 1):
    while True:
        try:
            precio = float(input(f"Producto {i}: $").strip())
            if precio <= 0:
                print("El precio debe ser mayor a 0")
                continue
            suma_total += precio
            break
        except ValueError:
            print("Ingrese un número válido")

# Resultados
promedio = suma_total / cantidad

print("\n--- RESUMEN ---")
print(f"Total de la compra: ${suma_total:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")