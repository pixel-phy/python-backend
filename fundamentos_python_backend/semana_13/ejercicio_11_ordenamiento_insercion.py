"""Ordenamiento por inserción

Modela a la perfección sistemas de ingreso dinámico de inventario o colas de prioridades en tiempo real. 

    Propiedades clave para producción:
    - Algoritmo Online: Puede ordenar una lista a medida que recibe elementos uno por uno. Si llega un 
    nuevo dato, lo inserta en teimpo O(k) donde k es la posicíon actual, ideal para arquitecturas de
    Streaming de datos.

    - Estabilidad: Si dos elementos tienen la misma prioridad, conserva su orden original de llegada 
    (algo vital en colas FIFO logísticas). """

# Ejemplos: Inserción continua de pedidos por urgencia. 

"""Imagina un Backend que gestiona las entregas de última milla. Los pedidos existentes ya están
    ordenados en el camión por su ventana de tiempo crítica (en minutos restantes). Cuando un 
    cliente solicita un servicio exprés de último minuto, el backend usa inserción para colocarlo
    en su sitio sin tocar el resto del orden preestablecido """

def insertar_pedido_en_cola(cola_pedidos: list[tuple[str, int]]):
    """Ordena in place una lista utilizando Insetion Sort (O(n²))
    
    Simula cómo un nuevo pedido busca su lugar óptimo de menor a mayor tiempo """

    n = len(cola_pedidos)

    for i in range(1, n):
        # Seleccionamos el elemento que queremos insertar
        clave_pedido = cola_pedidos[i]
        j = i - 1

        # Movemos los elementos de la sublista ordenada que sean mayores
        # que la clave, una posición hacia adelante de su posición actual
        while j >= 0 cola_pedidos[j][1] > clave_pedido[1]:
            cola_pedidos[j + 1] = cola_pedidos[j]
            j -= 1

        # Insertamos la clave en su posición correcta
        cola_pedidos[j + 1] = clave_pedido
