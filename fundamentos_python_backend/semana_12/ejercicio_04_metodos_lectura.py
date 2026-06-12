"""Métodos de lectura en Python
    Se utilizan para que no se congele o se caigan los servidores según sus especificaciones y la información
    que reciben.
    1. archivo.read(size=-1)
    Lee todo el contenido del archivo de golpe y lo devuelve como un único sting gigantesco.
        - Peligro: Se recomienda usarlo sólo si tienes la certeza absoluta de que el archivo
        es pequeño (archivos de configuración, JSON pequeños, etc...)
    2. archivo.readline()
    Lee el archivo línea por línea. Cada vez que lo llamas, se mueve a la siguiente línea y 
    se detiene al encontrar un saldo de línea (\n).
        - Utilidad: Útil si solo necesitas inspeccionar las primeras líneas de un archivo (por ejemplo:
        para leer encabezados de una tabla). 3. archivo.readlines()
    Lee todo el archivo y empaqueta cada línea como un elemento dentro de una lista de python.
        - Peligro: Al igual que read(), carga todo el archivo en la memoria RAM, por lo que no es ideal
        para archivos masivos.

    En Python, un objeto de archivo es iterable. Puedes pasarlo directamente por un bucle for.
    Python irá leyendo lína por línea bajo demanda (sin cargar todo el archivo en la RAM). """

# Ejemplo:
# Leer el archivo errores.log que creamos en el ejercicio anterior.

# Abrimos el archivo en modo de lectura.
archivo_log = open("errores.log", mode="r", encoding="utf-8")

print("--- Iniciando lectura de logs ---")

# Recorremos el archivo línea por línea de forma eficiente.
for linea in archivo_log:
    # .strip() elimina los saltos de línea '\n' y espacios invisibles al inicio y al final.
    linea_limpia = linea.strip()
    print(f"Registro procesado: {linea_limpia}")

# Cerramos el flujo
archivo_log.close()

print("--- Fin de la lectura ---")
