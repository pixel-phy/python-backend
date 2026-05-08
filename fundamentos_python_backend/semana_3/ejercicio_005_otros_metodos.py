"""Dada la variable: datos = "manzana,pera,platano,uva"
1. Convertir el string en una lista.
2. Mostrar cada fruta en una línea.
3. Unir la lista original con el separador " - ".
4. Convertir el string original a una lista separada por espacios (en lugar de comas).
5. Unir la lista con el separador " | "."""
datos = "manzana,pera,platano,uva"
datos_espacios = "manzana pera platano uva"
datos_lista_comas = datos.split(",")

separador = " - ".join(datos_lista_comas)
datos_lista_espacios = datos_espacios.split(" ")
datos_separador_barra = " | ".join(datos_lista_comas)

print("\n--- RESULTADOS ---\n")
print(f"String original: {datos}")
print(f"String convertida en lista: {datos_lista_comas}")
print(f"Así se ven si mostramos las frutas en una línea: ")
for fruta in datos_lista_comas:
    print(f"{fruta}")
print(f"La lista unida con el separado  ' - ': {separador}")
print(f"La lista separada por espacios: {datos_lista_espacios}")
print(f"Con el separador ' | ': {datos_separador_barra}")

