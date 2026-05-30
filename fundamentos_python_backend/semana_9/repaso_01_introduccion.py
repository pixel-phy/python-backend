"""Creación y acceso a diccionarios
¿Qué es un diccionario?
Es una colección de elementos que contienen pares 'clave: valor' y se separan con comas. Como una lista de contactos en un teléfono"""

# Ejemplo en Backend: configurar servidor
config = {
        "host": "localhost",
        "puerto": 8080,
        "debug": True
        }

# Crear diccionarios
# Forma 1: con {}
usuario = {
        "nombre": "Ana",
        "email": "ana@mail.com"
        }

# Forma 2: con dict()
producto = dict(nombre="laptop", precio=800)

# Forma 3: vacío y luego llenar
pedido = {}
pedido["id"] = "ORD-001"
pedido["total"] = 850

# Acceder a valores
usuario = {"nombre": "Ana", "email": "ana@mail.com"}

# Con corchetes
print(usuario["nombre"])

# Con .get() (no da error si falta la clave)
print(usuario.get("telefono"))
print(usuario.get("telefono", "No disponible"))
print(usuario.get("email"))


