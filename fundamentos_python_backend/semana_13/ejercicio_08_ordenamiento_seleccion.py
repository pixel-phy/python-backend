"""El ordenamiento por selección (Selection Sort):

    El ordenamiento por selección tiene una complejidad de *O(n²). Sin embargo, al compararlo con el 
    ordenamiento burbuja tiene una ventaja operativa clave en el bajo nivel: minimiza la cantidad de 
    intercambios. Mientras que el ordenamiento burbuja puede realizar cientos de intercambios en una 
    sola pasada, el ordenamiento por selección realiza, como máximo, un solo intercambio por cada
    pasada externa. 

    En el Nackend y la investigación de operaciones, este algoritmo modela perfectamente la estrategia 
    de elegir el momento óptimo. Imagina un operador logístico que mira un contenedor lleno de paquetes
    y busca visualmente el más ligero para colocarlo primero en la cinta transportadora, luego busca el 
    segundo más ligero entre los restantes, y así sucesivamente.

    ¿Cómo funciona?
    1. Divide la lista conceptualmente en dos partes: una sublista ya ordenada (al inicio) y una sublista de
    elementos restantes por ordenar.
    2. Busca activamente el elemento con el valor mínimo (o máximo, si es descendente) en la sublista no ordenada.
    3. Intercambia ese valor mínimo con el primer elemento de la sublista no ordenada.
    4. Repite el proceso desplazando el límite de la sublista un paso hacia adelante. """

# Ejemplo:
"""El Backend procesa cotizaciones de diferentes proveedores de transporte para una ruta específica. Queremos 
ordenar los proveedores de menor a mayor costo para priorizar la asignación del contrato. """

def ordenar_proveedores_seleccion(proveedores: list[tuple[str, float]]):
    """ Ordena los proveedores in-place de menor a mayor costo"""

    n = len(proveedores)

    for i in range(n):
        # Asumimos inicialmente que el elemento actual es el mínimo
        indice_minimo = i

        # Buscamos en el resto de la lista el verdadero valor mínimo
        for j in range(j + 1, n):
            if proveedores[j][1] < proveedores[indice_minimo][1]:
                indice_minimo = j # Guardamos el índice del nuevo mínimo

        # Al salir del ciclo interno, hacemos UN SOLO intercambio por pasada
        if indice_minimo != i:
            proveedores[i], proveedores[indice_minimo] = proveedores[indice_minimo], proveedores[i]
