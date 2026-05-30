"""Ejercicio 1: Acceder a valores dentro de diccionarios
Crear un diccionario api_response que represente la respuesta de una API con estos datos:
    - "status": "success"
    - "code": 200
    - "data": {"id": 1, "nombre": "producto X"}

1. Imprimir el status
2. Imprimir el "nombre" dentro de "data". """

api_response = {
        "status": "success",
        "code": 200,
        "data": {"id": 1, "nombre": "Producto X"}
        }
print(f"Status: {api_response['status']}")
print(f"Nombre dentro de 'data': {api_response['data']['nombre']}")

