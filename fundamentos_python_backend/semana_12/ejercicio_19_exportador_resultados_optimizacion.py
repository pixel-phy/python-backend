""" El exportador de Resultados de Optimización (DictWriter)

Después de que un algoritmo de IO calcula las rutas óptimas, el Backend debe guardar los 
resultados en un archivo CSV para que el equipo de logística los vea. Tenemos la siguiente
lista de diccionarios con los resultados del modelo:

    rutas_optimas = [
        {"origen": "Bogota", "destino": "Chia", "distancia_km": 25, "costo_envio": 120},
        {"origen": "Medellin", "destino": "Envigado", "distancia_km": 12, "costo_envio": 65},
        {"origen": "Cali", "destino": "Yumbo", "distancia_km": 18, "costo_envio": 90}
]

Escribe un script que:
    1. Cree un archivo llamado report_rutas.csv en modo escritura.
    2. Defina una lista de cabeceras llamada columnas = ["origen", "destino", "distancia_km", "costo_envio"].
    3. Configure el escritor usando escritor = csv.DictWriter (archivo,fieldnames=columnas).
    4. Escriba las cabeceras usando escritor.writeheader().
    5. Use un bucle for para recorrer la lista rutas_optimas y escribir cada diccionario en el archivo 
    usando escritor.writerow(fila). """

import csv
from pathlib import Path

rutas_optimas = [
        {"origen": "Bogota", "destino": "Chia", "distancia_km": 25, "costo_envio": 120},
        {"origen": "Medellin", "destino": "Envigado", "distancia_km": 12, "costo_envio": 65},
        {"origen": "Cali", "destino": "Yumbo", "distancia_km": 18, "costo_envio": 90}
]

ruta_csv = Path("rutas_optimas.csv")

with open(ruta_csv, mode="w", encoding="utf-8", newline="") as archivo:

    columnas = ["origen", "destino", "distancia_km", "costo_envio"]

    # Le pasamos la lista con los nombres de las columnas
    escritor = csv.DictWriter(archivo, fieldnames=columnas)
    escritor.writeheader()

    for fila in rutas_optimas:
        escritor.writerow(fila)
