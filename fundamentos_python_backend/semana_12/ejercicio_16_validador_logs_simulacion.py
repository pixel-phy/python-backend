""""El validador de Logs de Simulación
Crea un script que intente abrir en modo lectura el archivo de texto que creamos ayer:
    segurdidad.log:
    - Hazlo utilizando Context Manager.
    - Dentro del bloque, lee el archivo línea por línea y muestra los resultados en la consola. """

with open ("seguridad.log", mode="r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip()")

