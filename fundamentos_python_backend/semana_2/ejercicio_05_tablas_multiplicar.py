"""Tablas de multiplicar del 1 al 5:
Un programa que muestre las tablas de multiplicar del 1 al 5. Para cada número, mostrar su tabla del 1 al 10.
Requisitos:
- Bucle externo: recorre los números del 1 al 5.
- Bucle interno: recorre los multiplicadores del 1 al 10.
- Mostrar cada tabla por separado."""

for i in range(1, 6):
    print(f"\nTabla del {i}:")
    for j in range (1, 11):
        multiplicacion = i * j
        print(f"{i} x {j} = {multiplicacion}")
