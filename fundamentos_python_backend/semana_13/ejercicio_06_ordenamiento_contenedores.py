""" Ordenamiento de contenedores por prioridad

    El ordenamiento burbuja clásico, siempre ejecuta todos los ciclos, incluso si la lista
    ya se ordenó en la primera pasada (lo que sería un desperdicio de tiempo de CPU en el servicio Backend).

    Implementa el algoritmo de ordenamiento burbuja para ordenar una lista de contenedores (id_contenedor, nivel_prioridad)
    de forma ascendente (de menor a mayor prioridad).

    Requisito Backend de optimización: Se debe incluir una variable boolenada (bandera) llamada intercambiado. 
    Si en una pasada completa por la lista no se realiza ningún intercambio, significa que la lista ya está completamente
    ordenada. El algoritmo debe hacer un break inmediatamente para ahorrar ciclos de reloj del procesador. """

def ordenamiento_burbuja(contenedores: list[tuple[str, int]]):
    """Se ordena una lista de contenedores por prioridad.

        Args:
            contenedores: Lista de tuplas(id_contenedor, nivel_prioridad)

        Returns:
            Lista ordenada
    """

    n = len(contenedores)
    # Bucle externo: controla el número de pasadas
    for i in range(n-1):
        # Bandera para detectar cambios en cada pasada
        intercambio = False

        # Bucle interno: compara elementos adyacentes
        for j in range(0, n - 1 - i):
            # Comparar por nivel_prioridad
            if contenedores[j][1] > contenedores[j + 1][1]:
                # Intercambiar los contenedores
                contenedores[j], contenedores[j + 1] = contenedores[j + 1], contenedores[j]
                intercambio = True # Se marca el intercambio

        if not intercambio:
            print(f"La lista ordenada en la pasada {i + 1} optimización")
            break
    return contenedores

contenedores = [("CONT-05", 8), ("CONT-02", 3), ("CONT-09", 12), ("CONT-01", 1)]

print("Lista original:")
for contenedor in contenedores:
    print(f"ID: {contenedor[0]}, Prioridad: {contenedor[1]}")

contenedores_ordenados = ordenamiento_burbuja(contenedores)

print("\nLista ordenada:")
for contenedor in contenedores_ordenados:
    print(f"ID: {contenedor[0]}, prioridad: {contenedor[1]}")
