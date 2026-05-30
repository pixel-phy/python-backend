"""Ejercicio: recorrer diccionarios
Dado el diccionario de base de datos. Usando .items(), imprime cada configuración en el formato:
    host = localhost
    port = 5432
    database = tienda
    user = admin """

db_config = {
        "host": "localhost",
        "port": 5432,
        "database": "tienda",
        "user": "admin"
}

for clave, valor in db_config.items():
    print(f"{clave} = {valor}")

