"""Utilizando la misma lista de frutas:
1. Extraer las primeras 2 frutas.
2. Extraer las últimas 2 frutas.
3. Extraer desde la posición 1 hasta la 3 (sin incluir la 3).
4. Extraer todas las frutas pero en orden inverso."""

frutas = ["manzana", "pera", "uva", "naranja", "sandia"]
primera_dos = frutas[0:2]
ultimas_dos = frutas[-2:]
rango = frutas[1:3]
inverso = frutas[::-1]

print(f"Primeras dos: {primera_dos}")
print(f"Últimas dos: {ultimas_dos}")
print(f"Índices 1 a 3: {rango}")
print(f"Orden inverso: {inverso}")