""" Ejercicio de modificación de diccionarios
Dada una respuesta de API.
1. Agregar una clave "telefono" con valor "555-1234" dentro del diccionario "usuario"
2. Modifica el "email" a "carlos.nuevo@mail.com"
3. Agrega una clave "ultimo_acceso" al diccionario principal (no dentro de usuario) con valor "2026-05-30"
4. Imprime todo el diccionario 'respuesta_api' actualizado. """

respuesta_api = {
        "success": True,
        "data": {
            "usuario": {
                "nombre": "Carlos",
                "email": "carlos@mail.com"
                }
            }
        }
# Agregar clave teléfono
respuesta_api["data"]["usuario"]["telefono"] = "555-1234"

# Modificar el "email"
respuesta_api["data"]["usuario"]["email"] = "carlos.nuevo@mail.com"

# Agregar clave "ultimo_acceso"
if "ultimo_acceso" not in respuesta_api:
    respuesta_api["ultimo_acceso"] = "2026-05-30"

print(respuesta_api)
