""" Balanceo de carga de trabajo descendente:

    Un despachador de tareas de manufactura flexible necesita ordenar las órdenes de trabajo
    según las horas de procesamiento requeridas de forma descendente para aplicar una regla heurítica
    de IO conocida como Longest Processing Time.
    - Modifica el algoritmo de ordenamiento por inserción para que ordene una lista de trabajos 
    (id_trabajo, horas_procesamiento) de forma estrictamente descendente. """

def ordenamiento_insercion_descendente(trabajos: list[str, float]):
    """
        Ordena una lista de trabajos (id_trabajo, horas_procesamiento)
        de forma estrictamente descendente por horas_procesamiento.

        Args:
            trabajos: lista de tuplas
        Returns:
            La misma lista ordenada """

    for i in range(1, len(trabajos)):
        # se guarda el trabajo actual
        trabajo_actual = trabajos[i]
        j = i - 1

        while j >= 0 and trabajos[j][1] < trabajo_actual[1]:
            trabajos[j + 1] = trabajos[j]
            j -= 1

        # Insertamos el trabajo en su pocisión correcta
        trabajos[j + 1] = trabajo_actual

    return trabajos

trabajos = [("JOB-1", 3.5), ("JOB-2", 1.2), ("JOB-3", 5.0), ("JOB-4", 2.8)]

print("Lista original:", trabajos)
ordenamiento_insercion_descendente(trabajos)
print("Lista ordenada:", trabajos)
