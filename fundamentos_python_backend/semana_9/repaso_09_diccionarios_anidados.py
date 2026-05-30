"""Diccionarios anidados:
En Backend esto es todos los días (JSON de APIs, respuestas de bases de datos, etc.) """

# Ejemplo: respuesta de API de usuarios
respuesta = {
        "status": "success",
        "data": {
            "usuarios": [
                {"id": 1, "nombre": "Ana", "activo": True},
                {"id": 2, "nombre": "Carlos", "activo": False}
            ],
            "total": 2
        }
    }

# Acceder a elementos anidados
print(respuesta["data"]["usuarios"][0]["nombre"])
print(respuesta["data"]["total"])

# Modificar elemento anidado
respuesta["data"]["usuarios"][1]["activo"] = True
print(respuesta["data"]["usuarios"][1]["activo"])

