"""Recorrer diccionarios anidados:
Esta es una habilidad crítica para Backend (procesar JSON de APIS, logs, etc). """

# Ejemplo: estructura de menú de API
api_endpoints = {
        "usuarios": {
            "GET": "/api/users",
            "POST": "/api/users",
            "metodos": ["listar", "crear"]
        },
        "productos": {
            "GET": "/api/products",
            "DELETE": "/api/products/{id}"
        }
    }

# Recorrer diccionario de dos niveles:
for endpoint, config in api_endpoints.items():
    print(f"\nEndpoint: {endpoint}")
    for clave, valor in config.items():
        print(f"    {clave}: {valor}")


