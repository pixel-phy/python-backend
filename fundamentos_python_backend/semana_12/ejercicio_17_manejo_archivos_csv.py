"""Manejo de archivos CSV (DictReader y DictWriter)
En el mundo de Operations Research, el formato de texto plano (.txt) se quedar corto. Los datos de inventarios,
costos de transporte, demandas de clientes y capacidades de plantas casi siempre se estructuran en tablas. Por eso,
el formato CSV es el rey indicutible para mover datos antes de meterlos a un modelo matemático.

Python incluye un módulo nativo llamado csv. Aunque existen librerías pesadas como pandas, en el backend preferimos
usar el módulo nativo cuando necesitamos un consumo de memoria mínimo y máxima velocidad.

Las herramientas estrella: Diccionarios para leer y escribir
Olvídate de separar por comas usando .split(","). python nos da dos clases espectaculares que convierten 
cada fila del archivo en un diccionario, mapeando automáticamente los encabezados con los valores.

1. csv.DictReader(archivo)
Lee un archivo CSV y transforma cada fila en un diccionario de Python, donde las claves son los nombres de las columnas
(la primera línea del archivo) y los valores son los datos de esa fila.

2. csv.DictWriter(archivo, fiednames)
Hace el proceso inverso. Le das una lista con los nombres de las columnas (fieldnames) y luego puedes pasarle diccionarios
de Python directamente para que los escriba como filas en el CSV. """

# Ejemplo:

""" Tenemos un archivo llamado consumos.csv con los costos de materia prima para una fábrica. Así los leemos 
de forma ultra-eficiente en el Backend para pasarlos a un optimizador:"""

import csv
from pathlib import Path

ruta_csv = Path("insumos.csv")

with open(ruta_csv, mode="r", encoding="utf-8", newline="") as archivo:
    # DictReader detecta automáticamente que la primera línea son las cabeceras
    lector_csv = csv.DictReader(archivo)

    print("--- Datos cargados para el Optimizador de Costos ---")
    for fila in lector_csv:
    # Cada 'fila' es un diccionario: {'producto': 'Acero', 'costo_usd': '500', ...}
        nombre = fila["producto"]

    # Todos los datos de un CSV entran como texto (strings).
    # Si vamos a trabajar matemáticas en IO, debes convertirlos a float o int:
    costo = float(fila["costo_usd"])

    print(f"Material: {nombre} | Costo por tonelada: ${costo} USD")

    # Siempre que utilicemos el módulo csv, agregar el argumento newline="" dentro de open(). 
    # Es una recomendación oficial para evitar líneas vacías huérfanas en algunos sistemas operativos.
