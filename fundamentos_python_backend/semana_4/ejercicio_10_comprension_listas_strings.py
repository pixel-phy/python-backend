"""Comprensión de listas con elementos STRINGs
Dada la lista: ["manzana", "pera", "uva", "platano", "mango"]
1. Crea una lista con las frutas que tengan más de 4 letras.
2. Crea una lista con las frutas en mayúsculas.
3. Crear una lista con la primera letra de cada fruta."""

frutas = ["manzana", "pera", "uva", "platano", "mango"]
largas = [f for f in frutas if len(f) > 4]
print(f"Más de 4 letras: {largas}")
mayus = [f.upper() for f in frutas]
print(f"Lista con elementos en mayúscula: {mayus}")
letras = [f[0] for f in frutas]
print(f"Lista con primeras letras: {letras}")