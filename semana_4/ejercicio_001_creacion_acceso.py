"""Creación y acceso de listas:
1. Crear una lista llamada frutas con los siguientes elementos:
- "manzana", "pera", "uva", "naranja", "sandia".
2. Muestra:
- El primer elemento.
- El último elemento.
- El tercer elemento.
- La longitud de la lista."""
print("\n== CREACIÓN Y ACCESO ===\n")
frutas = ["manzana", "pera", "uva", "naranja", "sandia"]

primer_elemento = frutas[0]
ultimo_elemento = frutas[-1]
tercer_elemento = frutas[2]
longitud_lista = len(frutas)

print(f"Primera fruta: {primer_elemento}")
print(f"Última fruta: {ultimo_elemento}")
print(f"Tercer fruta: {tercer_elemento}")
print(f"Cantidad de frutas: {longitud_lista}")