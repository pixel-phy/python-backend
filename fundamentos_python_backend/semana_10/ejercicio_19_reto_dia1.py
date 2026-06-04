""" Reto: Formateador de respuestas HTTP

Imagina que estás construyendo una API. Cada vez que el frontend nos pide datos, el backend debe 
responder con una estructura limpia estándar.
Crear una función llamada generar_respuesta_api:
    - Debe recibir tres parámetros: estado (un string con "success" o "error"), mensaje (un string) y datos (un diccionario con información)
    - La función debe retornar un único diccionario con la siguiente estructura exacta:
    { 
    "status": estado,
    "message": mensaje,
    "data": datos
    } """

def generar_respuesta_api(estado: str, mensaje: str, datos: dict):
    estadoOptions = ["success", "error"]
    if estado not in estadoOptions:
        return {
                "status": "error",
                "mensaje": f"'{estado}' no reconocido. Debe ser 'success' o 'error'.",
                "data": None
                }

    if not isinstance(mensaje, str):
        return {
                "status": "error",
                "mensaje": "El formato del mensaje debe ser un texto (str).",
                "data": None
                }

    if not isinstance(datos, dict):
        return {
                "status": "error",
                "mensaje": "El formato de datos debe ser un diccionario (dict).",
                "data": None
                }
    return {
            "status": estado,
            "message": mensaje,
            "data": datos
            }
print(generar_respuesta_api("success", "Todo correcto por este lado", {"nombre": "Miguel", "Edad": 31}))
print(generar_respuesta_api("success", "Hola", "Esto es un string, no un dict"))
