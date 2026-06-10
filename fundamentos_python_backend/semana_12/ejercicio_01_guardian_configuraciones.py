"""El guardián de Configuraciones (Modo x):
    Crear un script que intente crear un archivo de configuración llamado config.txt 
    usando el modo de creación.
    - La primera vez que lo ejecutes, debe escribir dentro: VERSION=1.0.0
    - La segunda vez que lo ejecutes, revisar el error que arroja Python. """

# 1. Crear el archivo 
archivo = open("config.txt", mode="x", encoding="utf-8")

# 2. Escribimos dentro:
archivo.write("VERSION=1.0.0")

# 3. Cerramos el archivo
archivo.close()

print("¡Archivo creado y editado con éxito!")
