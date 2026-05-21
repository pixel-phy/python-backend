""" Primer acercamiento a los SETS
1. Crear un set llamado colores con: "rojo", "verde", "azul", "rojo".
2. Agrega "amarillo" usando .add().
3. Elimina "verde" usando .remove().
4. Muestra la longitud del set.
5. Recorre el set e imprime cada color."""

colores = {"rojo", "verde", "azul", "rojo"}
colores.add("amarillo")
colores.remove("verde")
print(f"La longitud del set es: {len(colores)}")

for color in colores:
    print(color)