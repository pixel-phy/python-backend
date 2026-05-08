"""Orden descendente (mayor a menor):
Únicamente cambiamos la condición del intercambio."""
numeros = [5, 2, 8, 1, 9, 3, 12, 15, 4]
n = len(numeros)
for i in range(n):
    intercambio = False
    for j in range(n - i - 1):
        if numeros[j] < numeros[j+1]:
            numeros[j] , numeros[j+1] = numeros[j+1] , numeros[j]
            intercambio = True
    if not intercambio:
        break

print(f"Números ordenados: {numeros}")