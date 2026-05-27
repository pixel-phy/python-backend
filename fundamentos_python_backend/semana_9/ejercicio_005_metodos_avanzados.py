usuario = {"nombre": "Ana", "edad":25, "ciudad": "Madrid"}

print(f"\nDiccionario Original: {usuario}\n")
# 1. .pop(clave) - elimina y devuelve el valor
edad = usuario.pop("edad")
print(f"Eliminado: {edad}")
print(f"Diccionario después de pop: {usuario}")

# 2. .update(otro_dict) - funsiona otro diccionario:
usuario.update({"profesion": "Ingeniera", "ciudad": "Barcelona"})
print(f"Después de update: {usuario}")

# 3. .setdefault(clave, default) - obtiene valor o lo crea si no existe
telefono = usuario.setdefault("telefono", "000-000")
print(f"Telefono: {telefono}")
print(f"Diccionario después de setdefault: {usuario}")

# 4. .clear() - vacía el diccionario
usuario.clear()
print(f"Después de clear: {usuario}")

# En el diccionario libro
""" 1. Eliminar la clave año usando .pop() y guardar el valor.
    2. Agrega una nueva clave "idioma" con valor "Español" usando .updat()
    3. Usa .setdefault() para agregar "paginas" con valor 300 (si no existe)
    4. Muestra el diccionario final. """

# Eliminar la clave año
libro = {"titulo": "Más allá del bien y del mal", "autor": "Nietzsche", "año": 1650}
año = libro.pop("año")
libro.update({"idioma": "Español"})
paginas = libro.setdefault("paginas", "300")
print(f"Diccionario final: {libro}")
