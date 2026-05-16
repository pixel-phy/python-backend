"""Tuplas con datos mixtos y métodos
1. Crea una tupla con datos mixtos (nombre, edad, ciudad, activo).
2. Mostrar cada elemento utilizando índices.
3. Desempaquetar la tupla usando variables.
4. Usar el método count() para contar cuántas veces aparece un valor.
5. Usar el método index() para encontrar la primera posición de un valor.
6. Crear nueva tupla agregando otra tupla.
7. Verificar si un elemento existe en una tupla."""

tupla = ("Kquioty", 31, "Pereira", True)

print(f"Nombre: {tupla[0]}")
print(f"Edad: {tupla[1]}")
print(f"Ciudad: {tupla[2]}")
print(f"Activo: {tupla[3]}")

nombre, edad, ciudad, activo = tupla

numeros = (1, 2, 3, 4, 5, 4, 6, 7, 4, 8, 9, 4, 10, 4, 4, 12, 4, 8, 4)
print("El 4 aparece ", numeros.count(4), "veces en la tupla.")
print("El índice de 4 es: ", numeros.index(4))

nueva_tupla = numeros + (11, 12)

if "Ana" in numeros:
    print("\nElemento sí está en la tupla.")
else: 
    print("\nElemento no está en la tupla")
