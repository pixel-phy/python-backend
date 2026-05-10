"""Repaso básico:
Dada la lista frutas = ["manzana", "pera", "uva", "naranja", "sandia"], realizar las siguientes operaciones en orden:
1. Muestra el primer elemento.
2. Mostrar el último elemento.
3. Mostrar los primeros 3 elementos.
4. Mostrar los últimos 2 elementos.
5. Mostrar la lista en orden inverso (sin modificar la original).
6. Agregar "kiwi" al final. 
7. Agregar "mango" en la posición 2 (índice 2).
8. Eliminar "pera" de la lista.
9. Muestra la lista final."""

frutas = ["manzana", "pera", "uva", "naranja", "sandia"]
primer_elemento = frutas[0]
print(f"Primer elemento: {primer_elemento}")
ultimo_elemento = frutas[-1]
print(f"Último elemento: {ultimo_elemento}")
primeros_tres = frutas[0:3]
print(f"Primeros tres: {primeros_tres}")
ultimos_dos = frutas[-2:]
print(f"Últimos dos: {ultimos_dos}")
orden_inverso = frutas[::-1]
print(f"Orden inverso: {orden_inverso}")
frutas.append("kiwi")
print(f"Con 'kiwi': {frutas}")
frutas.insert(2, "mango")
print(f"Insertando 'mango': {frutas}")
frutas.remove("pera")
print(f"Sin 'pera': {frutas}")
print(f"Lista final: {frutas}")