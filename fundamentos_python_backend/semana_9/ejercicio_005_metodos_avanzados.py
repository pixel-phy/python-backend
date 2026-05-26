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

