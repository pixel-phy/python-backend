""" Ejercicio 03: Búsqueda de Capacidad Exacta en Almacenes Automatizados

Un sistema de gestión de almacenes (WMS) tiene una lista de estantes con posiciones de 
almacenamiento de pallets. La lista está estrictamente ordenada de menor a mayor según
el peso máximo que soporta cada estante (en kg).
    -  Una lista de tuplas (id_estante, capacidad_kg) ordenada por capacidad_kg, y un peso 
    requerido exato por un brazo robótico.
    - Implementar una función con búsqueda binaria que retorne el id_estante que tenga 
    exactamente esa capacidad. Si no existe un estante con esa capacidad matemática exacta, 
    se retorna None. """

def buscar_capacidad_exacta(estantes: list[tuple[str, int]], peso_requerido: float):
    """ Buscar un estante con capacidad exacta usando búsqueda binaria.

        Args:
        estantes: Lista de tuplas (id_estante, capacidad_kg) ordenada por capacidad.
        peso_requerido: Capacidad exacta que se busca.

        Returns:
        id_estante si se encuentra, None en caso contrario.
    """

    izquierda = 0
    derecha = len(estantes) - 1

    while izquierda <= derecha:
        medio = izquierda + (derecha - izquierda) // 2
        id_estante, capacidad = estantes[medio]

        if capacidad == peso_requerido:
            return id_estante
        elif capacidad < peso_requerido:
            izquierda = medio + 1
        else: # capacidad > peso_requerido
            derecha = medio - 1

    return None

# Prueba

estantes = [("E-101", 500), ("E-102", 1000), ("E-103", 1500), ("E-104", 2000), ("E-105", 2500)]
capacidad_buscada = 1500

print(buscar_capacidad_exacta(estantes, capacidad_buscada))
