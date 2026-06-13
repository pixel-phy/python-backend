"""Manejo de errores en Backend

Si un algoritmo de optimización intenta leer un archivo de inventarios que el usuario olvidó subir,
el servidor arrojará un FileNotFoundError y se apagará. En Backend, un servidor nunca debe morir 
por un error predecible. Usamos bloques try-except para capturar el fallo y reaccionar con elegancia. """

# Ejemplo:

"""Imagina un script de IO que intenta cargar los parámetros de optimización de una plata de producción desde una
ruta específica."""

from pathlib import Path

# Definimos la ruta

ruta_parametros = Path("configuracion") / "parametros_planta.txt"

try:
    # Intentamos abrir el archivo usando un Context Manager
    with open(ruta_parametros, mode="r", encoding="utf-8") as archivo:
        datos = archivo.read()
        print("--- Parámetros cargados con éxito para el modelo de IO ---")
        print(datos)

except FileNotFoundError:
    # Si el archivo no existe, el servidor no muere; ejecutamos un plan de respaldo B 
    print(f"Alerta Backend: El archivo en '{ruta_parametros}' no fue encontrado.")
    print("Cargando parámetros de optimización por defecto (Modo seguro)...")

except PermissionError:
    print(f"Error de permisos: No se puede acceder a '{ruta_parametros}'.")
