""" Reto 1: Optimización de Despacho en flotas (Capacidad crítica)
    Un centro de distribución tiene una lista de camiones en cola para salir. Cada camión tiene un 
    identificador y un peso de carga actual (en toneladas). Los camiones están ordenados por orden 
    de llegada (no por peso).
    - Escribir una función que recorra la cola secuencialmente y encuentre el primer camión que 
    supere un "límite crítico de carga" (X) para dirigirlo a una báscula de control de seguridad.
    - Requisito Backend: Si ningún camión supera el límite, debes manejarlo adecuadamente 
    (retornar un valor centinela o lanzar una excepción personalizada de negocio). """

from typing import Optional, Union

# Definimos un alias de tipo para mejorar la ligibilidad del contrato de la función
Camion = tuple[str, float]

def buscar_primer_excedido(camiones: list[Camion], limite: float):
    """
        Args:
            camiones: Lista de tuplas con formato (id_camion, peso_toneladas).
            limite: límite crítico de peso en toneladas.

        Returns:
            La tupla (id, peso) del primer camión infractor, o None si la flota cumple.
    """
    # Validación inicial (sanitización de datos)
    if not camiones:
        return None

    for id_camion, peso in camiones:
        if peso > limite:
            return (id_camion, peso) #O(1) si es el primero 
    return None

if __name__ == "__main__":
    flota: list[Camion] = [
        ("A001", 10.5), 
        ("A002", 8.2), 
        ("A003", 12.0), 
        ("A004", 9.5)
    ]
    limite_critico: float = 11.0

    resultado = buscar_primer_excedido(flota, limite_critico)

    if resultado is not None:
        id_camion, peso = resultado
        print(f"[ALERTA BÁSCULA] Redirigir camión {id_camion} (Peso: {peso} t).")
    else:
        print("[OK] Todos los camiones operan bajo el límite crítico de carga.")
