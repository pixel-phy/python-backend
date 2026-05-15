"""Simular escritura y deshacer en un editor de texto"""

historial = []
texto_actual = ""

historial.append(texto_actual)
entrada_texto = input("Escribe algo: ")
historial.append(entrada_texto)
print(f"Texto: {entrada_texto}")
texto_actual += entrada_texto

entrada_otro_texto = input("Añade algo: ")
historial.append(entrada_otro_texto)
texto_actual += " " + entrada_otro_texto
print(f"Texto: {texto_actual}")

if historial:
    texto_actual = historial.pop()
    print(f"Deshecho. Texto: '{texto_actual}'")

if historial:
    texto_actual = historial.pop()
    print(f"Deshecho: '{texto_actual}'")

