""" Ejemplo 1: Configuración que no debe modificarse """

DB_HOST = "localhost"
DB_PORT = 5432
API_KEY = "sk-123456"

def conectar_bd():
    # Solo Lee las globales, no las modifica
    print(f"Conectando a {DB_HOST}:{DB_PORT}")
    return {"Conectado": True}

conectar_bd()

"""Ejemplo 2: Contador de requests (simulado)"""

def procesar_request(contador):
    return contador + 1, f"Procesando request #{contador + 1}"

contador = 0
contador, mensaje = procesar_request(contador)
print(mensaje)
contador, mensaje = procesar_request(contador)
print(mensaje)

""" Ejemplo 3: Usuario Logueado (simulación de sesión) """
def login(sesion, nombre):
    sesion["usuario"] = nombre
    return sesion

def obtener_usuario(sesion):
    return sesion.get("usuario")

sesion = {}
sesion = login(sesion, "Ana")
print(obtener_usuario(sesion))
