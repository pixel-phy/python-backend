"""Tuplas - Desempaquetado
1. Crea una tupla con tres coordenadas.
2. Desempaqueta la tupla en varibales.
3. Mostrar las variables.
4. Intercambia los valores de x e y usando tuplas.
5. Usar desempaquetado para mostrar el primer y último elemento de una tupla. """

coordenadas = (10, 20, 30)

x, y, z = coordenadas

print(f"x: {x}, y: {y}, z:{z}")

x, y = y, x

print(f"x: {x}, y: {y}")

dias = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")

primero, *resto, ultimo = dias

print(f"Primedo: {primero} | Último: {ultimo} | Resto: {resto}")