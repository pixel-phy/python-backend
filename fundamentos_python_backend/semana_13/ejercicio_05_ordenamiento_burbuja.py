"""Ordenamiento burbuja (Bubble sort)

    El Ordenamiento burbuja es un algoritmo clásico con una complejidad temporal de O(n²) en el peor
    de los casos. Aunque en el desarrollo Backend rara vez se utilizará para ordenar millones de registros,
    su lógica es fundamental en la investigación de operaciones por dos razones:
    - Lógica de intercambio local (Swap): Enseña a modificar estructuras de datos en memoria si usar
    colecciones auxiliares, lo cual optimiza el uso de la memoria RAM del servidor. 
    - Priorización por pares: en IO, se asemeja a los procesos donde comparamos continuamente las tareas adyacentes
    en una línea de producción y las reordenadas según su penalización o urgencia. 
    
    Funcionamiento: Recorre la lista múltiples veces. En cada iteración, compara elementos adyacentes y los intercambia
    si están en el orden incorrecto. De esta forma, los elementos más "pesados" van cayendo hacia el final de la lista 
    en cada pasada, como burbujas subiendo a la superficie.  """

# Ejemplo: Reorganización de Cola de despacho

""" Imagina que un backend recibe las órdenes de producción retrasadas. Cada orden tiene un ID y los
    "días retraso". Para mitigar el impacto con los clientes, queremos ordenar la cola para que las 
    órdenes con más días de retraso queden al principio (orden descendente) para ser atendidas de inmediato. """

def ordenar_por_retraso_burbuja(ordenes: list[tuple[str, int]]):
    """ Ordena la lista in-place (modifica la original) de forma descendente
        según los días de retraso """

    n = len(ordenes)

    for i in range(n):
        for j in range(0, n - i - 1):
            if ordenes[j][1] < ordenes[j + 1][1]:
                ordenes[j], ordenes[j + 1] = ordejes[j + 1], ordenes[j]



