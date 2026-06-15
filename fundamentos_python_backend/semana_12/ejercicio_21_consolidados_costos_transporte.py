"""Reto 2: El consolidador de Costos de Transporte:
    Antes de correr un modelo de Programación Lineal para minimizar costos de envío entre ciudades,
    el sistema necesita calcular el costo total por kilómetro sumando el costo base de la ruta más
    un impuesto ambiental estandarizado del 12%.

    1. Crear un archivo llamado rutas_operativas.csv con el siguiente contenido:
    origen,destino,costo_base_km
    Bogota,Ibague,12.5
    Medellin,Pereira,14.2
    Cali,Buenaventura,18.5
    2. Escribe un script que lea el archivo línea por línea (usando DictReader).
    3. Por cada ruta, calcula el costo total combinando la fórmula:

        costo_total = costo_base_km x 1.12

    4. En lugar de escribir un archivo nuevo, imprime en consola un informe limpio que se vea 
    exactamente así:
    --- INFORME DE COSTOS PARA MODELADO LINEAL ---
    Ruta: Bogota -> Ibague | Costo Final/Km: $14.0 USD
    Ruta: Medellin -> Pereira | Costo Final/Km: $15.9 USD
    Ruta: Cali -> Buenaventura | Costo Final/Km: $20.72 USD """

import csv
from pathlib import Path

ruta_archivo1 = Path("rutas_operativas.csv")

print("--- INFORME DE COSTOS PARA MODELADO LINEAL ---")
with open(ruta_archivo1, mode="r", encoding="utf-8") as archivo:
    lector_csv = csv.DictReader(archivo)
    
    for fila in lector_csv:
        origen = fila["origen"]
        destino = fila["destino"]
        costo_base_km = float(fila["costo_base_km"])

        costo_total = costo_base_km * 1.12
        print(f"Ruta: {origen} -> {destino} | Costo Final/km: ${round(costo_total, 2)} USD")

