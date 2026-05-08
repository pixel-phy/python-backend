"""Filtrar palabras:
Dada la lista palabras = ["sol", "luna", "estrella", "mar", "planeta"], crea una nueva lista solo
con las palabras que tengan más de 4 letras."""

palabras = ["sol", "luna", "estrella", "mar", "planeta"]
mas_de_4 = [p for p in palabras if len(p) > 4]
print(f"Palabras: {palabras}")
print(f"Más de 4 letras: {mas_de_4}")