"""Comprensión de listas (filtros y transformaciones)

Dada la lista numeros = [10, 15, 20, 25, 30, 35, 40, 45, 50], usar comprensión de listas para:
1. Pares.
2. mayores_30
3. Cuadrados
4. Mitades
5. pares_y_mayores
6. transformados. """

numeros = [10, 15, 20, 25, 30, 35, 40, 45, 50]
pares = [n for n in numeros if n % 2 == 0]
mayores_30 = [n for n in numeros if n > 30]
cuadrados = [n**2 for n in numeros]
mitades = [n/2 for n in numeros]
pares_y_mayores = [n for n in numeros if n % 2 == 0 and n > 25]
transformados = [n **2 if n % 2 == 0 else n for n in numeros]

print(f"pares: {pares}")
print(f"Mayores de 30: {mayores_30}")
print(f"Cuadradros: {cuadrados}")
print(f"Mitades: {mitades}")
print(f"Pares y mayores: {pares_y_mayores}")
print(f"Transformados: {transformados}")
