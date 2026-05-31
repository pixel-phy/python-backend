"""Agrupación múltiple (backend real)

Tienes logs de acceso a una API. Cada log es un diccionario con:
    - "endpoint": string ("/users", "/products")
    - "metodo": strin ("GET", "POST", etc)
    - "status": int (200, 404, 500)
    - "tiempo_ms": int (milisegundos que tardó la respuesta)

Construir un diccionario de estadísticas. """

logs = [
    {"endpoint": "/users", "metodo": "GET", "status": 200, "tiempo_ms": 45},
    {"endpoint": "/users", "metodo": "POST", "status": 201, "tiempo_ms": 120},
    {"endpoint": "/products", "metodo": "GET", "status": 200, "tiempo_ms": 30},
    {"endpoint": "/users", "metodo": "GET", "status": 404, "tiempo_ms": 15},
    {"endpoint": "/products", "metodo": "GET", "status": 200, "tiempo_ms": 25},
    {"endpoint": "/users", "metodo": "POST", "status": 500, "tiempo_ms": 300}
]

estadisticas = {}

for log in logs:
    endpoint = log["endpoint"]
    metodo = log["metodo"]

    if endpoint not in estadisticas:
        estadisticas[endpoint] = {}

    if metodo not in estadisticas[endpoint]:
        estadisticas[endpoint][metodo] = {
                "total_requests": 0,
                "success": 0,
                "suma_tiempos": 0,
                "avg_time": 0.0
                }

    estadisticas[endpoint][metodo]["total_requests"] += 1

    if 200 <= log["status"] <= 299:
        estadisticas[endpoint][metodo]["success"] += 1

    estadisticas[endpoint][metodo]["suma_tiempos"] += log["tiempo_ms"]

    print(f"\nProcesado: {endpoint} {metodo}")
    print(estadisticas)

print("\n--- CALCULO DE PROMEDIOS ---")

for endpoint, metodos in estadisticas.items():
    for metodo, datos in metodos.items():
        if datos["total_requests"] > 0:
            datos["avg_time"] = datos["suma_tiempos"] / datos["total_requests"]

        del datos["suma_tiempos"]

print("\n--- Estadísticas finales ---")
for endpoint, metodos in estadisticas.items():
    print(f"\nEndpoint: {endpoint}")
    for metodo, datos in metodos.items():
        print(f" {metodo}: total={datos['total_requests']}, success={datos['success']}, avg_time={datos['avg_time']}")

