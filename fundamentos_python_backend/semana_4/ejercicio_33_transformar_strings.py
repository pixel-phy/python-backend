"""Transformar strings:
Dada la lista palabras = ["hola", "mundo", "python", "es", "genial"], crea una nueva lista con las palabras en mayúsculas."""

palabras = ["hola", "mundo", "python", "es", "genial"]
mayusculas = [p.upper() for p in palabras]
print(f"Palabras: {palabras}")
print(f"Mayúsculas: {mayusculas}")