"""Ordenar letras del alfabeto
Ordenar una lista de letras desordenadas usando el algoritmo de burbuja."""

letras = ['m', 'a', 'z', 'c', 'b', 'f']
l = len(letras)
for i in range(l):
    intercambiado = False
    for j in range(0, l - i - 1):
        if letras[j] > letras[j+1]:
            letras[j], letras[j+1] = letras[j+1] , letras[j]
            intercambiado = True

    if not intercambiado:
        break
print(f"Lista ordenada de menor a mayor: {letras}")