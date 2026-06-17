"""Minimización del tiempo de configuración

    En la programación de la producción (Scheduling de IO), se busca secuencias los trabajos
    en una máquina para minimizar el tiempo de configuración. Tienes una lista de trabajos
    representados por tuplas: (id_trabajo, tiempo_configuracion_horas).

    - Ordena los trabajos de forma ascendente según su tiempo de configuración utilizando la lógica
    de burbuja optimizada con bandera. 
    - Añade un contador de "comparaciones totales" y "intercambios totales" realizados durante el algoritmo.
    Imprime estos dos contadores al final para demostrar de forma empírica cómo la bandera evitó iteraciones
    innecesarias si la lista ya estaba parcialmente ordenada. """

def burbuja_con_contadores(trabajos: list[tuple[str, float]]):
    """Ordena trabajos por tiempo de configuración usando burbuja con bandera y 
    contadores

    Args: 
        trabajos: Lista de tuplas (id_trabajo, tiempo_configuracion_horas)

    Returns: 
        tuple: (lista_ordenada, comparaciones, intercambios)
    """

    n = len(trabajos)

    # Inicializamos contadores
    comparaciones = 0
    intercambios = 0

    # Bucle externo: controla el número de pasadas
    for i in range(n - 1):
        # Bandera que detecta si hubo intercambio en esta pasada
        intercambiado = False

        # Bucle interno: compara elementos adyacentes
        for j in range(0, n - 1 - i):
            # Comparar por tiempo_configuracion_horas
            comparaciones += 1
            if trabajos[j][1] > trabajos[j + 1][1]:
                # Intercambiar los trabajos
                trabajos[j], trabajos[j + 1] = trabajos[j+1], trabajos[j]
                intercambios += 1
                intercambiado = True

        if not intercambiado:
            print(f"Lista ordenada en la pasada {i + 1}. Optimización break aplicado.")
            break

    return trabajos, comparaciones, intercambios

trabajos = [("T-1", 1.5), ("T-2", 0.5), ("T-3", 2.0), ("T-4", 1.0)]

ordenados, comparaciones, intercambios = burbuja_con_contadores(trabajos)

print("Trabajos ordenados: ")
for id_trabajo, tiempo in ordenados:
    print(f"    {id_trabajo}: {tiempo} horas")

print(f"\nComparaciones: {comparaciones}")
print(f"Intercambiado: {intercambios}")

