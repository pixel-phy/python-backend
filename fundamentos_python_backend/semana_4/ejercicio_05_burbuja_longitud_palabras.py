"""Ordenar palabras por longitud
Ordenar una lista de palabras de menor a mayor longitud."""

palabras = ["Python", "c", "java", "rust", "javascript", "go"]
longitud_lista = len(palabras)

for i in range(longitud_lista):
    intercambio = False
    for j in range(longitud_lista - i - 1):
        if len(palabras[j]) > len(palabras[j+1]):
            palabras[j] , palabras[j+1] = palabras[j+1] , palabras[j]
            intercambio = True
    
    if not intercambio:
        break

print(f"Lista ordenada: {palabras}")