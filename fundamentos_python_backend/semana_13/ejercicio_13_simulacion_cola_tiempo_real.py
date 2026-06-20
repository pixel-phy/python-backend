"""Endpoint "Stream-Insert" (Simulación de cola en tiempo real)
    En los sistemas Backend distribuidos, los datos de los sensores de telemetría o los camiones en 
    ruta llegan todos al mismo tiempo: llegan como un flujo continuo (stream).
    - Diseñar una arquitectura de funciones que simule este comportamiento:
    1. Tendrás una lista llamada inventario_ordenado que inicialmente tiene un registro base 
    ya ordenad. 
    2. Implementarás una función llamada recibir_e_insertar_item(lista_actual, nuevo_item) que use la lógica
    de inserción para colocar el nuevo_item (id_item, stock_unidades) en la posición correcta (de menor a mayor
    stock) de forma inmediata, asumiendo que la lista de entrada ya está ordenada.

    Restricción Backend: No puedes usar .append() y luego ordenar toda la lista con .sort(). Debes meter el elemento
    al final y desplazarlo hacia atrás usando el bucle while de inserción para garantizar eficiencia logarítmica/lineal 
    en cada inserción.
    """
from typing import Tuple
ItemInventario = tuple[str, int]

def recibir_e_insertar_item(inventario: list[ItemInventario], nuevo_item: ItemInventario):
    """
        Inserta un nuevo item en una lista ya ordenada (de menor a mayor stock)
        usando la lógica de inserción eficiente.

        Args:
            Lista_actual: Lista ordenada de tuplas (id_item, stock_unidades)
            nuevo_item: tupla(id_item, stock_unidades) a insertar

        Returns:
            La lista actualizada (modificación in place)

        Resticción: no usar append() mi .sort(), solo inserción """
    
    inventario.append(nuevo_item)

    i = len(inventario) - 1

    clave_item = inventario[i]

    j = i - 1

    while j >= 0 and inventario[j][1] > clave_item[1]:
        inventario[j + 1] = inventario[j]

        j -= 1

        inventario[j + 1] = clave_item

if __name__ == "__main__":
    # Estado inicial de la base de datos
    inventario_realtime: list[ItemInventario] = [
        ("PROD-A", 10), 
        ("PROD-B", 50), 
        ("PROD-C", 100)
    ]
    
    print("Inventario Inicial:", inventario_realtime)

evento_1 : ItemInventario = ("PROD-D", 5)
recibir_e_insertar_item(inventario_realtime, evento_1)
print(f"Evento 1 procesado (Insertar {evento_1}):")
print(f"    Inventario: {inventario_realtime}\n")

evento_2: ItemInventario = ("PROD-E", 75)
recibir_e_insertar_item(inventario_realtime, evento_2)
print(f"Evento 2 procesado (Insertar {evento_2}):")
print(f"    Inventario: {inventario_realtime}\n")

evento_3: ItemInventario = ("PROD-F", 120)
recibir_e_insertar_item(inventario_realtime, evento_3)
print(f"Envento 3 procesado (Insertar {evento_3}):")
print(f"    Inventario: {inventario_realtime}\n")
