"""Ejercicio 04: El algoritmo de "Siguiente Mejor" (Optimización de despacho)
    En el mundo real de la investigación de operaciones, rara vez los requerimientos coinciden de forma 
    exacta. Si un cliente pide un camión para 12 toneladas y solo tienes camiones de 10 t y 15 t, 
    debes asignarle el de 15 t (el primero que cumpla).

    - Modificar el algoritmo de búsqueda binaria. Si el peso exacto no existe en tu lista de camiones ordenados
    por capacidad, la función debe retornar el primer camión que sea estrictamente mayor o igual al peso requerido 
    - Restricción: Si el peso requerido supera la capacidad del camión más grande de la lista, retorna None (exceso 
    de capacidad global). """

def buscar_mejor_camion(camiones: list[tuple[str, float]], peso_requerido: float):
    """
        Buscar el primer camión con capacidad >= peso_requerido usando búsqueda binaria.
        Retorna ID del camión o None si no hay capacidad suficiente.

        Args:
            camiones: Lista de tuplas (id_camion, capacidad_ton) ordenada por capacidad 
            peso_requerido: Peso que necesita transportar el cliente.

        Returns:
            id_camion si existe capacidad suficiente, None en caso contrario.
    """

    # Si el peso del requerido supera la capacidad máxima
    if not camiones or peso_requerido > camiones[-1][1]:
        return None
    
    izquierda = 0
    derecha = len(camiones) - 1
    resultado = None

    while izquierda <= derecha:
        medio = izquierda + (derecha - izquierda) // 2
        id_camion, capacidad = camiones[medio]

        if capacidad == peso_requerido:
            # Encontramos una coincidencia exacta, es la mejor opción
            return id_camion
        elif capacidad < peso_requerido:
            # Se necesita un camión más grande, buscamos a la derecha
            izquierda = medio + 1
        else: 
            resultado = id_camion
            derecha = medio - 1

    return resultado

flota_disponible = [("C-01", 5.0), ("C-02", 8.0), ("C-03", 10.0), ("C-04", 15.0), ("C-05", 20.0)]
peso_carga = 12.0

print(buscar_mejor_camion(flota_disponible, peso_carga))

