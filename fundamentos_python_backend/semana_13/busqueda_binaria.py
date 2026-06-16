""" Búsqueda binaria (O(log n))

    En el Backend y la investigación de operaciones, la búsqueda binaria es fundamental cuando manejamos volúmenes masivos
    de datos y necesitamos respuestas en milisegundos.

    Mientras que la búsqueda lineal toma un tiempo proporcional al tamaño de la lista (O(n)), la búsqueda 
    binaria divide el espacio de búsqueda a la mitad en cada paso. Esto reduce drásticamente
    el número de comparaciones: se puede buscar en una lista de 1 millón de elementos ordenados en un máximo de 
    20 pasos.

    Restricción sagrada: Para que la búsqueda binaria funcione, la colección debe estar ordenada 
    bajo algún criterio (ascendente o descendente). Si los datos no están ordenados, el algoritmo fallará.
    """
    
# Se importa Optional de la librería typing para indicar que una función puede devolver un valor o nulo

from typing import Optional
# Tipo de dato: Tuple[distancia_km, costo_flete]
tarifa = tuple[int, float]

def buscar_tarifa_por_distancia(tabla_tarifas: list[tarifa], distancia_objetivo: int):
    izquierda = 0
    derecha = len(tabla_tarifas) - 1

    while izquierda <= derecha:
        # Usamos // para división entera (obtenemos el índice medio)
        medio = (izquierda + derecha) // 2
        distancia_actual, costo = tabla_tarifas[medio]

        if distancia_actual == distancia_objetivo:
            return costo # encontrado
        elif distancia_actual < distancia_objetivo:
            izquierda = medio + 1 # Descartamos la mitad izquierda
        else:
            derecha = medio - 1 # Descartamos la mitad derecha
    return None # No existe una tarifa exacta para esa distancia. 

    
