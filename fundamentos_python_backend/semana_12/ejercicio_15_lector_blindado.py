"""El lector blindado de Modelos
En los problemas de IO, los datos de las plantas de distribución se aguardan en carpetas organizadas.
    1. Importa pathlib y define una ruta hacia un archivo llamado demandas.txt que debería estar 
    teóricamente dentro de una carpeta llamada entradas.
    2. Diseña un bloque try-except para intentar abrir ese archivo en modo lectura utilizando un Context
    Manager.
    3. Como la carpeta entradas y el archivo no existen en la computadora, el código entrará al except FileNotFoundError.
    En esa sección, haz que el programa imprima un mensaje controlado: "Error controlado: El archivo no existe. Inicializando
    optimización con demanda cero." """

from pathlib import Path 

ruta_demandas = Path("entradas") / ("demandas.txt")
try:
    with open(ruta_demandas, mode="r", encoding="utf-8") as archivo:
        datos = archivo.read()
        print("El archivo se abrió correctamente: ")
        print(datos)
except FileNotFoundError:
    print("Error controlado: El archivo no existe. Inicializando optimización con demanda cero.")


