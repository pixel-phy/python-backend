""" Ejercicio 10: El filtro K-Óptimo (optimización de memoria en grandes volúmenes)

    Un algoritmo de ruteo de vehículos genera 10.000 combinaciones de rutas posibles con sus respectivas distancias
    en km: (id_ruta, distancia_km). Al cliente solo le intereas ver las 3 rutas más cortas. Si ordenamos las 10.000
    rutas completas usando un algoritmo tradicional, desperdiciaríamos CPU. El ordenamiento por selección tiene una
    propiedad maravillosa: en la pasada i, garantiza que el elemento en la posición i ya es el i-ésimo elemento óptimo global.

    - Escribir una función que reciba la lista de rutas y un número entero k. Modifica el ordenamiento por selección para 
    que solo ejecute las primeras k pasadas. Al final, trunca la lista y retorna únicamente los k mejores elementos ordenados. """

def filtro_k_mejores_rutas(rutas: list[tuple[str, float]], k: int):
    """
        Encuentra y retorna las k rutas más cortas usando selección parcial.

        Args:
            rutas: lista de tuplas (id_ruta, distancia_km)
            k: Número de mejores rutas a retornar
        
        Returns: 
            Lista con las k rutas más cortas ordenadas
    """

    if k<= 0:
        return []

    if k >= len(rutas):
        return ordenar_completo_seleccion(rutas)[:k]

    n = len(rutas)

    # Solo ejecutamos las primeras k pasadas
    for i in range(k):
        # Encontramos el indice del elemento con menor distancia.
        indice_min = i
        for j in range(i + 1, n):
            if rutas[j][1] < rutas[indice_min][1]:
                indice_min = j

        # Intercambiamos si es necesario
        if indice_min != i:
            rutas[i], rutas[indice_min] = rutas[indice_min], rutas[i]

    return rutas[:k]

def ordenar_completo_seleccion(rutas: list[tuple[str, float]]):
    """ Ordena todas las rutas por distancia usando selección"""
    n = len(rutas)

    for i in range(n - 1):
        indice_min = i
        for j in range(i + 1, n):
            if rutas[j][1] < rutas[indice_min][1]:
                indice_min = j

        if indice_min != i:
            rutas[i], rutas[indice_min] = rutas[indice_min], rutas[i]

    return rutas

# Prueba:
rutas = [("Ruta-1", 150.5), ("Ruta-2", 80.2), ("Ruta-3", 300.1), ("Ruta-4", 95.4), ("Ruta-5", 42.0)]
k = 3

print("\nLas 3 rutas más cortas son:")
mejores_rutas = filtro_k_mejores_rutas(rutas, k)
for i, (ruta, distancia) in enumerate(rutas, 1):
    print(f"{i}: {ruta} - {distancia} km")


