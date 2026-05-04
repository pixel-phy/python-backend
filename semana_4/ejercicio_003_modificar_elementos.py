"""Modificar elementos en una lista:
Con la misma lista de frutas:
1. Cambiar "pera" por "mango".
2. Cambia la última fruta por "piña".
3. Agrega "fresa" al final.
4. Muestra la lista final."""

frutas = ["manzana", "pera", "uva", "naranja", "sandia"]
frutas[1] = "mango"
frutas[-1] = "piña"
frutas.append("fresa")

print(f"Lista modificada: {frutas}")
print(f"{len(frutas)}")