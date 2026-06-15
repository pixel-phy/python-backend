"""El extractor de Capacidad de Plantas (DictReader)
Crear un archivo de texto llamado plantas.csv y agregarle el continido:
planta,capacidad_max,costo_operacion
Bogota,1500,4200
Medellin,2200,5100
Cali,1100,3800

Escribir un script que abra el archivo con with open y csv.DictReader. Recorrerlo con un bucle for 
e imprimir en la consola únicamente el nombre de la planta y su capacidad máxima 
multiplicada por 0.85 (simulando que las plantas operan al 85% de su capacidad real por mantenimiento). """

# Abirmos el archivo

import csv
from pathlib import Path

ruta_archivo = Path("plantas.csv") 
# Abrimos el archivo
with open (ruta_archivo, mode="r", encoding="utf-8", newline= "") as archivo:
    lector_csv = csv.DictReader(archivo)

    for fila in lector_csv:

        planta = fila["planta"]
        capacidad_max = float(fila["capacidad_max"]) * 0.85

        print(f"Planta: {planta} | Capacidad Máxima: {capacidad_max}")
