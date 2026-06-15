"""Reto 1: 
    Nuestro optimizador de la cadena de suministro necesita leer una lista de proveedores
    de un archivo CSV llamado proveedores.csv, pero el algoritmo solo debe ejecutarse con 
    aquellos que tengan excelente calificación de confianza (un score mayor o igual a 85)
    para evitar riesgos de entrega.

    1. Crear manualmente un archivo proveedores.csv con los siguientes datos:
    id_proveedor,nombre,score,costo_fijo
    P01,Logistica_Express,90,450
    P02,Envios_Sura,78,300
    P03,Transportes_Saman,88,520
    P04,Carga_Rapida,82,400
    2. Escribir un script en Python que lea este archivo de forma eficiente.
    3. Filtrar las filas: si el score del proveedor es mayor o igual a 85, agrégalo a una nueva 
    lista de diccionarios en memoria.
    4. Guardar los proveedores aprobados en un nuevo archivo CSV llamado proveedores_filtados.csv
    usando DictWriter. Asegúrate de incluuir los encabezados originales.
    """
import csv
from pathlib import Path

ruta_archivo1 = Path("proveedores.csv")
ruta_archivo2 = Path("proveedores_filtrados.csv")
proveedores_aprobados = []

with open(ruta_archivo1, mode="r", encoding="utf-8") as archivo:
    lector_csv = csv.DictReader(archivo)

    for fila in lector_csv:
        score = int(fila["score"])
        if score >= 85:
            proveedores_aprobados.append(fila)

if proveedores_aprobados:
    with open(ruta_archivo2, mode="w", encoding="utf-8", newline="") as archivo:
        encabezados = proveedores_aprobados[0].keys()
        escritor = csv.DictWriter(archivo, fieldnames=encabezados)

        escritor.writeheader()
        escritor.writerows(proveedores_aprobados)

    print(f"Archivo guardado: {ruta_archivo2}")
    print(f"Total proveedores aprobados: {len(proveedores_aprobados)}")
    print(f"Contenido de {ruta_archivo2}:")

    with open(ruta_archivo2, mode="r", encoding="utf-8") as archivo:
        print(archivo.read())
else:
    print("No hay proveedores con score >= 85")
