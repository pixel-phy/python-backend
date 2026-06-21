"""Sistema de Asignación de Rutas Cross Docking (MDS)

Una empresa de retail utiliza un centro de distribución tipo Cross-Docking, donde la mercancía llega 
en camiones de proveedores, se descarga, se consolida y debe salir inmediatamente en camiones de resparto 
en ventanas de tiempo críticas.

El sistemas Backend recibe continuamente un lote masivo de solicitudes de envío. Cada solicitud contiene 
un ID de detino, la distancia en kilómetros, la prioridad del cliente y el volumen de carga. El objetivo 
es diseñar el motor algortimico que limpie, ordene y asigne afecientemente estas solicitudes.

Requisitos:
Construir un script de Python con tres módulos o funciones principales que trabajem en cadena:
    1. Módulo de sanitización y filtrado
    El payload de entrada viene de una API externa y contiene datos sucios. Se debe crear una función 
    que procese la lista original y:
    - Descarte registros incompletos o con ID nulos.
    - Valide que las distancias y volúmenes sean números positivos.
    - Filtre y conserve las solicitudes que pertenezcan a clientes de prioridad "ALTA" o "CRÍTICA".

    2. Móduglo de secuenciación LPT
    Para maximizar el uso de la flota disponible temprano en la mañana, la empresa aplica la heurítica
    de IO llamada Longest Processing Time, pero adaptada a transporte: se deben despachar primero los 
    viajes con las distancias más largas (en km).
    - Tomar la lista de solicitudes ya limpias del paso anterior y ordenarla de forma descendente según la distancia en kilómetros.
    - Implementar uno de los algoritmos de ordenamiento clásico.

    3. Módulo de Búsqueda y ventanas críticas
    Una vez ordenada la colsa por distancia, el gerente de operaciones necesita auditar rápidamente si en ese 
    lote optimizado existe alguna ruta hacia un destino específico para asignarle un chofer escolta.
    - Implementar una función de búsqueda para encontrar los detalles de la ruta buscada. """

# Módulo de sanitización y filtrado

def sanitizar_y_filtrar(payload):
    """
        Limpia y filtra los datos de entrada.

        Args:
        payload: Lista de tuplas (id_destino, distancia_km, prioridad_cliente, volumen_m3)

        Returns:
        Lista de solicitudes válidas
    """

    solicitudes_validas = []

    for solicitud in payload:
        # Validar que la solicitud tenga todos los campos
        if len(solicitud) != 4:
            continue

        id_destino, distancia_km, prioridad_cliente, volumen_m3 = solicitud

        # 1. Verificar ID no nulo
        if id_destino is None:
            continue

        # 2. Verificar que distancia sea número positivo
        if not isinstance(distancia_km, (int, float)) or distancia_km <= 0:
            continue

        # 3. Verificar que volumen sea número positivo
        if not isinstance(volumen_m3, (int, float)) or volumen_m3 <= 0:
            continue

        # 4. Verificar prioridad ALTA o Crítica
        if prioridad_cliente not in ["ALTA", "CRÍTICA"]:
            continue

        # Si pasa todas las validaciones, agregar a la lista
        solicitudes_validas.append(solicitud)

    return solicitudes_validas

# Módulo de secuenciación LPT (ordenamiento)

def ordenar_por_distancia(solicitudes):
    """
        Ordena las solicitudes por distancia de forma descendente usando ordenamiento por inserción
        Args:
            solicitudes: Lista de tuplas (id_destino, distancia_km, prioridad_cliente, volumen_m3)

        Returns:
            solicitudes: Lista ordenada por distancia descendente
    """

    if not solicitudes:
        return []

    # Se crea copia para no modificar la ooriginal
    lista_ordenada = solicitudes.copy()

    # Ordenamiento por inserción
    for i in range(1, len(lista_ordenada)):
        # Guardar el elemento actual
        elemento_actual = lista_ordenada[i]
        distancia_actual = elemento_actual[1]  # índice 1 = distancia_km
        
        # Mover elementos mayores a la derecha
        j = i - 1
        while j >= 0 and lista_ordenada[j][1] < distancia_actual:
            lista_ordenada[j + 1] = lista_ordenada[j]
            j -= 1
        
        # Insertar el elemento en su posición
        lista_ordenada[j + 1] = elemento_actual
    
    return lista_ordenada

# Módulo de búsqueda

def buscar_ruta_por_destino(solicitudes, id_buscado):
    """
        Busca una ruta específica por ID de destino usando búsqueda lineal.

        Args:
            solicitudes: Lista de tuplas (id_destino, distancia_km, prioridad_cliente, volumen_m3)

            id_buscado: ID del destino a buscar

        Returns:
            Tupla con los datos de la ruta o None si no se encuentra
    """

    for solicitud in solicitudes:
        if solicitud[0] == id_buscado:
            return solicitud
    return None

def main():
    """
    Función principal que ejecuta todo el flujo del sistema.
    """
    # Datos de entrada proporcionados
    payload_entrante = [
        ("DEST-01", 150.5, "ALTA", 25.0),
        ("DEST-02", -40.0, "CRÍTICA", 10.0),   # Invalido: distancia negativa
        (None, 80.0, "ALTA", 15.0),             # Invalido: ID nulo
        ("DEST-03", 420.0, "BAJA", 30.0),       # Invalido: prioridad baja
        ("DEST-04", 95.4, "CRÍTICA", 12.0),     # Válido
        ("DEST-05", 310.2, "ALTA", 18.5),       # Válido
        ("DEST-06", 120.0, "ALTA", "corrupto"), # Invalido: volumen no numérico
        ("DEST-07", 500.0, "CRÍTICA", 40.0),    # Válido
    ]
    
    print("SISTEMA DE ASIGNACIÓN DE RUTAS CROSS DOCKING\n")
    
    # Paso 1: Sanitización y filtrado
    print("1. SANITIZANDO Y FILTRANDO DATOS...")
    solicitudes_limpias = sanitizar_y_filtrar(payload_entrante)
    print(f"    Solicitudes válidas: {len(solicitudes_limpias)} de {len(payload_entrante)}")
    print("     Solicitudes válidas:", solicitudes_limpias, "\n")
    
    # Paso 2: Ordenamiento por distancia (LPT)
    print("2. ORDENANDO POR DISTANCIA (LPT - Mayor distancia primero)...")
    solicitudes_ordenadas = ordenar_por_distancia(solicitudes_limpias)
    print("     Solicitudes ordenadas:")
    for i, solicitud in enumerate(solicitudes_ordenadas, 1):
        print(f"      {i}. {solicitud}")
    print()
    
    # Paso 3: Búsqueda de ruta específica
    print("3. BÚSQUEDA DE RUTA ESPECÍFICA...")
    id_buscar = "DEST-05"
    ruta_encontrada = buscar_ruta_por_destino(solicitudes_ordenadas, id_buscar)
    
    if ruta_encontrada:
        print(f"    Ruta encontrada para {id_buscar}:")
        print(f"    ID: {ruta_encontrada[0]}")
        print(f"    Distancia: {ruta_encontrada[1]} km")
        print(f"    Prioridad: {ruta_encontrada[2]}")
        print(f"    Volumen: {ruta_encontrada[3]} m³")
    else:
        print(f"    No se encontró la ruta con ID: {id_buscar}")

if __name__ == "__main__":
    main()
