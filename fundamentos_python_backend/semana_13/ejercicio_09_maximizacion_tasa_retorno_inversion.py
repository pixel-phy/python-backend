"""Ejercicio 09: Maximización de la Tasa de Retorno de Inversión (ROI)

    En la gestión de portafolios de proyectos, los recursos son limitados y se deben priorizar los proyectos
    que dejen más ganancias. Tenemos una lista de proyectos representados por: (id_proyecto, porcentaje_roi).
    - Implementar el algoritmo de ordenamiento por selección para ordenar los proyectos de forma descendente
    (de mayor a menor ROI), para que el Backend exponga primero los proyectos más rentables. 
    - Mantener la eficiencia del algoritmo evitando hacer un intercambio si el elemento actual ya resulta ser
    máximo de esa pasada (tal como se muestra en la teoría). """

def ordenamiento_seleccion_roi(proyectos:list[tuple[str,float]]):
    """
        Ordena una lista de proyectos por ROI de forma descendente (mayor a menor)
        usando el algoritmo de selección optimizado.

        Args:
        proyectos: Lista de tuplas (id_proyecto, porcentaje_roi)

        Returns:
        Lista ordenada de forma descendente por ROI
    """

    n = len(proyectos)

    for i in range(n - 1):
        indice_max = i
        for j in range(i + 1, n):
            if proyectos[j][1] > proyectos[indice_max][1]:
                indice_max = j

        # Solo intercambiamos si el máximo no está ya en la posición i
        if indice_max != i:
            proyectos[i], proyectos[indice_max] = proyectos[indice_max], proyectos[i]

    return proyectos

# Prueba:

proyectos = [("PROJ-A", 12.5), ("PROJ-B", 25.0), ("PROJ-C", 8.2), ("PROJ-D", 18.9)]

print("Lista original:")
for proyecto, roi in proyectos:
    print(f"    {proyecto}: {roi}%")

proyectos_ordenados = ordenamiento_seleccion_roi(proyectos)

print("\nLista ordenada:")
for proyecto, roi in proyectos_ordenados:
    print(f"    {proyecto}: {roi}%")
