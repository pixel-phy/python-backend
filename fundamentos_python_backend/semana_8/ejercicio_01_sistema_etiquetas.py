"""Sistema de etiquetas
Una plataforma de contenido tiene artículos con etiquetas. Usa sets para gestionarlas."""

#Etiquetas de dos artículos
articulo1 = {"python", "backend", "api"}
articulo2 = {"python", "data", "machine learning"}

#1. Etiquetas únicas de ambos artículos
print(f"Todas las etiquetas: {articulo1 | articulo2}")

#2. Etiquetas comunes
print(f"Etiquetas comunes: {articulo1 & articulo2}")

#3. Etiquetas exclusivas
print(f"Solo etiquetas de artículo 1: {articulo1 - articulo2}")
print(f"Solo etiquetas de artículo 2: {articulo2 - articulo1}")

#4. Etiquetas que están en solo uno de los dos
print(f"Etiquetas exclusivas: {articulo1 ^articulo2}")

#5. Agregar una nueva etiqueta al artículo 1
articulo1.add("docker")
print(f"Artículo 1 actualizado: {articulo1}")

#6. Agregamos una etiqueta existente
articulo2.add("data")
print(f"Artículo 2 actualizado: {articulo2}")

if "python" in articulo1:
    print("La etiqueta sí está en el artículo 1")
else:
    print("La etiqueta no está en el artículo 1")