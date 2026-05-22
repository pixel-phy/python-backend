"""Gestión de etiquetas en artículos
Un blog tiene artículos con etiquetas. Debes implementar funciones básicas usando sets.
Requisitos:
1. Mostrar todas las etiquetas únicas de los tres artículos.
2. Mostrar las etiquetas que están en todos los artículos.
3. Mostrar las etiquetas que están solo en el artículo 1. 
4. Agregar la etiqueta "fastapi" al artículo 1.
5. Eliminar la etiqueta "data" del artículo 2 (Si existe, sin error).
6. Verificar si el artículo 1 y artículo 2 tienen etiquetas en común.
7. Mostrar el resumen final de los tres artículos."""

articulo1 = {"python", "backend", "api"}
articulo2 = {"python", "data", "machine-learning"}
articulo3 = {"backend", "api", "docker"}

# Mostrar todas las etiquetas únicas de los tres elementos
todas = articulo1 | articulo2 | articulo3
print(f"Todas las etiquetas: {todas}")

# Mostrar etiquetas que están en todos los artículos
etiquetas_en_todos = articulo1 & articulo2 & articulo3
print(f"Etiquetas que están en todos los artículos: {etiquetas_en_todos}")

# Etiquetas en un solo artículo
un_solo_articulo = articulo1 - articulo2 - articulo3
print(f"En un solo artículo: {un_solo_articulo}")

# Agregar fastapi
articulo1.add("fastapi")

#Eliminar data
articulo2.discard("data")

# Etiquetas en común
if articulo1.isdisjoint(articulo2):
    print("No tienen etiquetas en común.")
else:
    print("Si tienen etiquetas en común.")

# Los tres artículos quedan:
print("\n--- RESULTADOS ---")
print(f"Artículo1: {articulo1}")
print(f"Artículo2: {articulo2}")
print(f"Artículo3: {articulo3}")