"""remove(), pop() vs del
Entender las diferencias entre estas tres formas de eliminar elementos.
Dada la lista frutas = ["manzana", "pera", "uva", "pera", "naranja"]
1. Usa .remove() para eliminar "pera"
2. Usa .pop() para eliminar el elemento de la 2da posición.
3. Usa del frutas() para eliminar el primer elemento
4. Muestra la lista final.
"""
frutas = ["manzana", "pera", "uva", "pera", "naranja"]
print(f"\nLista original: {frutas}")
frutas.remove("pera")
print(f".remove('pera'): {frutas}")
frutas.pop(2)
print(f".pop(): {frutas}")
del frutas[0]
print(f"del frutas[0]: {frutas}")