""" Invertir una cadena usando pila
Un sistema necesita invertir el orden de los caracteres de un texto.

- Pedir una cadena al usuario.
- Usar una pila para invertirla.
- Mostrar el resultado."""

texto = input("Texto: ")
pila = []

for letra in texto:
    pila.append(letra)

invertido = ""
while pila:
    invertido += pila.pop()

print(f"Invertido: {invertido}")