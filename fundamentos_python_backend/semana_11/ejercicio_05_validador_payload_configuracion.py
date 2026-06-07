"""El validador de Payload de configuración:
    Cuando una aplicación backend arranca, lee un diccionario de configuración. Necesitamos
    asegurar que ciertas llaves obligatorias estén presentes para que el servidor no se apague.
    - Requerimiento: Crear una función validar_configuracion_servidor. No recibe parámetros
    obligatorios, solo configuraciones dinámicas.
    - Lógica: La función debe revisar que ambas llaves, "db_host" y "bd_port"m existan dentro de los parámetros.
        - Si existen las dos, retorna: {"status": "ready", "msg": "Conexión segura"}.
        - Si falta alguna de las dos, retorna: {"status": "critical", "msg": "Faltan credenciales de base de datos"}.
    Prueba:
    print(validar_configuracion_servidor(dv_host="localhost", db_port=3306, debug=True)) """

def validar_configuracion_servidor(**kwargs):
    if "db_host" in kwargs and "db_port" in kwargs:
        return {"status": "ready", "msg": "Conexión segura"}
    return {"status": "critical", "msg": "Faltan credenciales de base de datos"}

print(validar_configuracion_servidor(db_host="localhost", db_port=3306, debug=True))
