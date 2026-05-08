"""Filtrado de números pares e impares:
Procesar una lista de números:
1. Crear la lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
2. Crear dos listas vacía: pares e impares.
3. Usar for para recorrer números.
4. Si es par enviar a la lista de pares. Si es impar a la lista de impares.
5. Mostrar ambas listas. """

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f"Pares: {pares}")
print(f"Impares: {impares}")