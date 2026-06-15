""" Fábrica de muebles:
    Una fábrica produce sillas y mesas. Para el próximo mes, el departamento de producción necesita saber cuántas unidades de cada 
    una debe hacer para maximizar las ganancias. El script actuará como el módulo de preparación y persistencia de datos de ese 
    optimizador.

    Tendrás dos archivos de entrada:
    1. disponibilidad.txt: Contiene las horas de mano de obra disponibles en la planta este mes.
    2. productos.csv: Contiene la materia prima que usa cada producto, su ganancia y su demanda.

    Escribir un script que:
    Paso 1: Lea los recursos disponibles (Con manejo de errores)
    Crear manualmente un archivo llamado disponibilidad.txt que tenga solo este número: 160 (representan 160 horas de trabajo).
        - El script debe abrir este archivo, leer el número y guardarlo en una variable como entero.
        - Protege esta lectura con un bloque try-except por si el archivo no existe. Si no existe, lanza un mensaje controlado y asigna
        por defecto.
    
    Paso 2: Leer el catálogo de productos (CSV DictReader)
    Crea manualmente un archivo llamado productos.csv con este contenido:
        producto,horas_requeridas,ganancia_usd,demanda_max
        Silla,2,20,50
        Mesa,4,45,25
            - El script debe leer este CSV. Por cada producto, calcula cuánta ganancia teórica máxima podría generar si se cumpliera toda 
            su demanda (ganancia_usd * demanda_max).
            - Guarda esa información calculada agregando una nueva clave ("ganancia_potencial") a cada diccionario de producto.
    Paso 3: Guardar el escenario de simulación (CSV DictWriter)
            - Toma la lista de procductos modificada en el Paso 2 y expórtala a un nuevo archivo CSV llamado escenario_optimizacion.csv.
            - Este archivo debe contener los encabezados originales más la nueva columna:
            producto,horas_requeridas,ganancia_usd,demanda_max,ganancia_potencial.
    Paso 4: Emitir el Log de éxito en Backend (Persistencia y .flush())
            - Para dejar registro de que el Backend procesó todo con éxito, ebre un archivo llamado ejecuciones.log en modo append.
            - Escribe la lína: "LOG: Escenario cargado con éxito. Horas disponibles en planta: 160.\n".
            - Forzar la escritura inmediata con .flush(). """

import csv
from pathlib import Path

# Paso 1
ruta_archivo1 = Path("archivos_proyecto_semana_12") / "disponibilidad.txt"

try: 
    with open(ruta_archivo1, mode="r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
            disponibilidad = int(contenido)
    print(f"La variable se ha guardado exitosamente. Valor leído desde archivo: {disponibilidad}")
except FileNotFoundError:
    print("No se ha encontrado ningún archivo. Se asignará 160 a disponibilidad por defecto")
    disponibilidad = 160
    print(f"Valor asignado: {disponibilidad}")

# Paso 2
ruta_archivo2 = Path("archivos_proyecto_semana_12") / "productos.csv"
lista_productos = []

try: 
    with open(ruta_archivo2, mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            fila["horas_requeridas"] = int(fila["horas_requeridas"])
            fila["ganancia_usd"] = int(fila["ganancia_usd"])
            fila["demanda_max"] = int(fila["demanda_max"])
            
            # Calculamos y agregamos clave
            fila["ganancia_potencial"] = fila["ganancia_usd"] * fila["demanda_max"]

            # Se guarda el producto
            lista_productos.append(fila)

except FileNotFoundError:
    print(f"Error: No se encontró el archivo {ruta_archivo2}")

# Paso 3:
ruta_archivo_creado = Path("archivos_proyecto_semana_12") / "escenario_optimizacion.csv"

try:
    with open(ruta_archivo_creado, mode="w", encoding="utf-8", newline="") as archivo:

        encabezados = ["producto", "horas_requeridas", "ganancia_usd", "demanda_max", "ganancia_potencial"]

        escritor = csv.DictWriter(archivo, fieldnames=encabezados)

        escritor.writeheader()
        escritor.writerows(lista_productos)

    print(f"Archivo exportado exitosamente: {ruta_archivo_creado}")
    print(f"Total de productos exportados: {len(lista_productos)}")

except Exception as e:
    print(f"Error al guardar el archivo: {e}")

# Paso 4:
ruta_log = Path("archivos_proyecto_semana_12") / "ejecuciones.log"

try:
    with open(ruta_log, mode="a", encoding="utf-8") as archivo_log:
        archivo_log.write(f"LOG: Escenario cargado con éxito. Horas disponibles en planta: {disponibilidad}.\n")
        archivo_log.flush()

    print("Log registrado exitosamente")

except Exception as e:
    print(f"Error al escribir el log: {e}")
