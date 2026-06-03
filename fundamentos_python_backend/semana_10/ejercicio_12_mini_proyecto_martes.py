""" Mini proyecto: API simulada con configuración flexible.
Crear una función:
    crear_cliente_api(base_url="https://api.ejemplo.com", version="v1", timeout=10, retries=3, auth_token=None)
    que:

    1. Retorne una tupla (funcion_obtener, funcion_enviar) donde cada fución usa la configuración capturada (esto es una closure)
    2. La función obtener(endpoint) simule una petición GET imprimiendo:
        "GET {base_url}/{version}/{endpoint} timeout = {timeout}"
    3. La función enviar(endpoint, datos) simule una petición POST """

def crear_cliente_api(base_url="https://api.ejemplo.com", version="v1", timeout=10, retries=3, auth_token=None):
    def obtener(endpoint):
        """Simula una petición GET a la API"""
        url = f"{base_url}/{version}/{endpoint}"
        # Base del mensaje
        mensaje = f"GET {url} timeout={timeout}"

        # Si hay auth_token, se muestra (simulando auth)
        if auth_token:
            mensaje += f"(auth={auth_token[:5]}...)" # Solo primeros 5 caracteres por seguridad
        print(mensaje)

    def enviar(endpoint, datos):
        """Simula una petición POST a la API con datos."""
        url = f"{base_url}/{version}/{endpoint}"
        mensaje = f"POST {url} datos={datos} timeout={timeout}"

        if auth_token:
            mensaje += f"(auth={auth_token[:5]}...)"
        print(mensaje)

    return obtener, enviar
print("\n--- Cliente por defecto ---")
obtener, enviar = crear_cliente_api()
obtener("usuarios")
enviar("usuarios", {"nombre": "Ana", "email":"ana@mail.com"})

print("\n--- Cliente personalizado ---")
obtener2, enviar2 = crear_cliente_api(base_url="https://mi-api.com", version="v2", timeout=30, auth_token="secret123456")
obtener2("productos")
enviar2("productos", {"nombre": "laptop", "precio": 1500})

print("\n--- Cambiar algunos valores ---")
obtener3, enviar3 = crear_cliente_api(timeout=5, version="v3")
obtener3("health")
enviar3("logs", {"level": "INFO", "message": "Servidor iniciado"})
