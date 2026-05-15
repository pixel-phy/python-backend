"""Palíndromo con pila:
Una palabra es un palíndromo si se lee igual al revés (ana, reconocer)"""

palabra = input("Palabra: ").strip().lower()

lista = list(palabra)
invertida = []

while lista:
    invertida.append(lista.pop())

cadena_invertida = "".join(invertida)

if cadena_invertida == palabra:
    print(f"Es un palíndromo!")
else:
    print("No es un palíndromo")