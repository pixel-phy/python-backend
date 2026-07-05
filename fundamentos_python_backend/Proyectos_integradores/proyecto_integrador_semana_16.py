"""Proyecto integrador - Infraestructura logística y Distribución Capacitada
Para este proyecto utilizaremos una arquitectura orientada a objetos que simula el esqueleto de un motor 
de optimización (Solver) corporativo:

El objetivo es codificar y extender el framework anterior para construir las funciones del Solver Logístico Principal de la empresa.

Módulo 1: Auditoría de Resiliencia ante Disrupciones
Implementar un método basado en recorridos de grafos que reciba una lista de aristas o nodos 'caídos' y devuelva:
- Un reporte analítico qué clientes han quedado completamente aislado de cualquier fábrica productora.

Módulo 2: Motor de Ruteo MultiObjetivo con filtros de Infraestructura
Implementa el algoritmo de optimización de rutas que encuentre el camino óptimo desde una fábrica hasta un cliente específico.
El usuario debe poder seleccionar mediante un parámetro el criterio de optimización:

- Criterio = 'Costo': Minimizar la sumatoria de costes económicos financieros.
- Criterio = 'Tiempo': Minimizar el tiempo de tránsito total.
- Criterio = 'Confiabilidad': Maximizar la probabilidad de éxito de llegada segura de la carga.
- Restricción física obligatoria: El algoritmo debe filtrar el vuelo e ignorar cualquier tramo cial cuyo
  max_weight sea menor al peso del envío actual.

Módulo 3: Análisis de Cuellos de botella en Nodos Intermedios
Modifica la reconstrucción de la ruta del Módulo 2 para que verifique la capacidad de procesamiento 
de los nodos intermedios utilizados en el itinerario. Si el tamaño del lote de carga supera la capacidad disponible 
de un CEDI intermedio, la ruta debe ser reportada como 'Inviable por saturación de Infraestructura' o buscar una alternativa válida.

"""
from enum import Enum
from typing import Dict, List, Tuple, Set, Optional, Any
import heapq
import math
from collections import defaultdict

class NodeType(Enum):
    FACTORY = "Fábrica"
    HUB = "CEDIS"
    CLIENT = "Cliente"

class Node:
    def __init__(self, name: str, node_type: NodeType, capacity: float = float('inf')):
        self.name = name
        self.type = node_type
        self.capacity = capacity

class Edge:
    def __init__(self, target: str, cost: float, time: float, max_weight: float, reliability: float):
        self.target = target
        self.cost = cost
        self.time = time
        self.max_weight = max_weight
        self.reliability = reliability

class SupplyChainNetwork:
    def __init__(self):
        self.nodes: Dict[str, Node] = {}
        self.graph: Dict[str, List[Edge]] = {}

    def add_node(self, name: str, node_type: NodeType, capacity: float = float('inf')) -> None:
        self.nodes[name] = Node(name, node_type, capacity)
        if name not in self.graph:
            self.graph[name] = []

    def add_route(self, source: str, target: str, cost: float, time: float, max_weight: float, reliability: float) -> None:
        edge = Edge(target, cost, time, max_weight, reliability)
        self.graph[source].append(edge)

    # ==================== MÓDULO 1: Auditoría de Resiliencia ====================
    def audit_resilience(self, failed_nodes: Set[str] = None, failed_edges: Set[Tuple[str, str]] = None) -> Dict[str, Any]:
        """
        Analiza la conectividad de la red ante fallos y reporta clientes aislados de fábricas.
        """
        if failed_nodes is None:
            failed_nodes = set()
        if failed_edges is None:
            failed_edges = set()

        # Construir red activa (excluyendo nodos y aristas fallidas)
        active_graph = defaultdict(list)
        active_nodes = set(self.nodes.keys()) - failed_nodes
        
        for source in active_nodes:
            for edge in self.graph.get(source, []):
                if edge.target in active_nodes and (source, edge.target) not in failed_edges:
                    active_graph[source].append(edge.target)

        # Obtener todas las fábricas activas
        factories = {name for name, node in self.nodes.items() 
                    if node.type == NodeType.FACTORY and name in active_nodes}
        
        # Realizar BFS desde todas las fábricas
        reachable = set(factories)
        queue = list(factories)
        
        while queue:
            current = queue.pop(0)
            for neighbor in active_graph.get(current, []):
                if neighbor not in reachable:
                    reachable.add(neighbor)
                    queue.append(neighbor)

        # Identificar clientes aislados
        isolated_clients = []
        for name, node in self.nodes.items():
            if node.type == NodeType.CLIENT and name in active_nodes:
                if name not in reachable:
                    isolated_clients.append(name)

        # Generar reporte detallado
        report = {
            "total_nodes": len(self.nodes),
            "failed_nodes": len(failed_nodes),
            "failed_edges": len(failed_edges),
            "active_factories": len(factories),
            "total_clients": sum(1 for n in self.nodes.values() if n.type == NodeType.CLIENT),
            "isolated_clients": isolated_clients,
            "is_resilient": len(isolated_clients) == 0,
            "connectivity_analysis": {
                "reachable_nodes": len(reachable),
                "isolated_nodes": len(active_nodes) - len(reachable) if active_nodes else 0
            }
        }
        
        return report

    # ==================== MÓDULO 2: Motor de Ruteo Multi-Objetivo ====================
    def find_optimal_route(self, source: str, target: str, shipment_weight: float, 
                          criterion: str = "COSTO") -> Dict[str, Any]:
        """
        Encuentra la ruta óptima según el criterio especificado.
        """
        if source not in self.nodes or target not in self.nodes:
            return {"error": "Nodo origen o destino no existe"}
        
        if self.nodes[source].type != NodeType.FACTORY:
            return {"error": "El origen debe ser una fábrica"}
        
        if self.nodes[target].type != NodeType.CLIENT:
            return {"error": "El destino debe ser un cliente"}

        # Filtrar aristas según peso máximo
        def valid_edge(edge: Edge) -> bool:
            return edge.max_weight >= shipment_weight

        # Configurar optimización según criterio
        criterion_functions = {
            "COSTO": lambda path: sum(edge.cost for edge in path),
            "TIEMPO": lambda path: sum(edge.time for edge in path),
            "CONFIABILIDAD": lambda path: -sum(math.log(edge.reliability) for edge in path)  # Minimizar -log
        }

        if criterion not in criterion_functions:
            return {"error": f"Criterio '{criterion}' no válido. Use: COSTO, TIEMPO, CONFIABILIDAD"}

        # Dijkstra personalizado
        distances = {node: float('inf') for node in self.nodes}
        previous = {node: None for node in self.nodes}
        previous_edge = {node: None for node in self.nodes}
        distances[source] = 0
        priority_queue = [(0, source)]

        while priority_queue:
            current_dist, current_node = heapq.heappop(priority_queue)
            
            if current_dist > distances[current_node]:
                continue
            
            if current_node == target:
                break

            for edge in self.graph.get(current_node, []):
                if not valid_edge(edge):
                    continue
                
                # Calcular costo según criterio
                if criterion == "CONFIABILIDAD":
                    edge_cost = -math.log(edge.reliability) if edge.reliability > 0 else float('inf')
                elif criterion == "COSTO":
                    edge_cost = edge.cost
                else:  # TIEMPO
                    edge_cost = edge.time
                
                new_dist = current_dist + edge_cost
                
                if new_dist < distances[edge.target]:
                    distances[edge.target] = new_dist
                    previous[edge.target] = current_node
                    previous_edge[edge.target] = edge
                    heapq.heappush(priority_queue, (new_dist, edge.target))

        # Reconstruir ruta
        if distances[target] == float('inf'):
            return {
                "success": False,
                "message": f"No se encontró ruta válida para peso {shipment_weight}",
                "criterion": criterion
            }

        # Reconstruir ruta y detalles
        path_nodes = []
        path_edges = []
        current = target
        
        while current is not None and current != source:
            if previous_edge[current] is None:
                return {"success": False, "message": "Error en reconstrucción de ruta"}
            path_edges.append(previous_edge[current])
            path_nodes.append(current)
            current = previous[current]
        
        path_nodes.append(source)
        path_nodes.reverse()
        path_edges.reverse()

        # Calcular métricas de la ruta
        total_cost = sum(e.cost for e in path_edges)
        total_time = sum(e.time for e in path_edges)
        total_reliability = math.prod(e.reliability for e in path_edges)
        
        return {
            "success": True,
            "path": path_nodes,
            "edges": [(path_nodes[i], path_nodes[i+1]) for i in range(len(path_nodes)-1)],
            "criterion": criterion,
            "total_cost": total_cost,
            "total_time": total_time,
            "total_reliability": total_reliability,
            "shipment_weight": shipment_weight,
            "path_details": [(path_nodes[i], path_nodes[i+1], 
                            {"cost": path_edges[i].cost, 
                             "time": path_edges[i].time, 
                             "reliability": path_edges[i].reliability,
                             "max_weight": path_edges[i].max_weight}) 
                           for i in range(len(path_edges))]
        }

    # ==================== MÓDULO 3: Análisis de Cuellos de Botella ====================
    def find_route_with_capacity_check(self, source: str, target: str, batch_size: float,
                                     shipment_weight: float, criterion: str = "COSTO") -> Dict[str, Any]:
        """
        Encuentra ruta verificando capacidades de nodos intermedios.
        """
        # Primero encontrar ruta sin considerar capacidades
        route_result = self.find_optimal_route(source, target, shipment_weight, criterion)
        
        if not route_result.get("success", False):
            return route_result

        # Verificar capacidades de nodos intermedios
        path_nodes = route_result["path"]
        capacity_violations = []
        
        for i, node_name in enumerate(path_nodes):
            if i == 0:  # Fábrica origen
                continue
            if i == len(path_nodes) - 1:  # Cliente destino
                continue
            
            node = self.nodes.get(node_name)
            if node and node.type == NodeType.HUB:
                if node.capacity < batch_size:
                    capacity_violations.append({
                        "node": node_name,
                        "capacity": node.capacity,
                        "required": batch_size,
                        "excess": batch_size - node.capacity
                    })

        # Actualizar resultado con información de capacidad
        route_result["batch_size"] = batch_size
        route_result["capacity_violations"] = capacity_violations
        
        if capacity_violations:
            route_result["feasible"] = False
            route_result["message"] = "Ruta inviable por saturación de infraestructura"
            
            # Intentar encontrar ruta alternativa
            alternative_result = self.find_alternative_route_bypassing_bottlenecks(
                source, target, shipment_weight, batch_size, criterion, capacity_violations
            )
            if alternative_result:
                route_result["alternative_route"] = alternative_result
        else:
            route_result["feasible"] = True
            route_result["message"] = "Ruta válida con capacidad suficiente"

        return route_result

    def find_alternative_route_bypassing_bottlenecks(self, source: str, target: str, 
                                                   shipment_weight: float, batch_size: float,
                                                   criterion: str, bottlenecks: List[Dict]) -> Optional[Dict]:
        """
        Busca ruta alternativa evitando los nodos con capacidad insuficiente.
        """
        # Crear conjunto de nodos problemáticos para excluir
        problematic_nodes = {b["node"] for b in bottlenecks}
        
        # Excluir estos nodos temporalmente
        original_graph = self.graph.copy()
        
        try:
            # Eliminar conexiones a nodos problemáticos
            self.graph = defaultdict(list)
            for source_node, edges in original_graph.items():
                if source_node in problematic_nodes:
                    continue
                for edge in edges:
                    if edge.target not in problematic_nodes:
                        self.graph[source_node].append(edge)
            
            # Buscar nueva ruta
            alternative = self.find_optimal_route(source, target, shipment_weight, criterion)
            
            if alternative.get("success", False):
                # Verificar capacidad de la nueva ruta
                for node in alternative["path"][1:-1]:
                    if node in problematic_nodes:
                        return None  # Si aún usa nodos problemáticos, descartar
                return alternative
            return None
            
        finally:
            # Restaurar el grafo original
            self.graph = original_graph

# ==================== FUNCIONES DE PRUEBA Y DEMOSTRACIÓN ====================

def run_logistics_solver():
    """Ejecuta el solver completo con casos de prueba."""
    # Crear la red logística
    network = SupplyChainNetwork()

    # Nodos
    network.add_node("Fabrica_Alpha", NodeType.FACTORY)
    network.add_node("Fabrica_Beta", NodeType.FACTORY)

    network.add_node("CEDIS_Norte", NodeType.HUB, capacity=500.0)
    network.add_node("CEDIS_Sur", NodeType.HUB, capacity=200.0)

    network.add_node("Cliente_1", NodeType.CLIENT)
    network.add_node("Cliente_2", NodeType.CLIENT)
    network.add_node("Cliente_3", NodeType.CLIENT)

    # Rutas
    network.add_route("Fabrica_Alpha", "CEDIS_Norte", cost=150, time=4, max_weight=40, reliability=0.98)
    network.add_route("Fabrica_Alpha", "CEDIS_Sur", cost=300, time=8, max_weight=50, reliability=0.95)
    network.add_route("Fabrica_Beta", "CEDIS_Sur", cost=100, time=3, max_weight=20, reliability=0.99)
    network.add_route("CEDIS_Norte", "CEDIS_Sur", cost=50, time=2, max_weight=30, reliability=0.95)
    network.add_route("CEDIS_Norte", "Cliente_1", cost=200, time=5, max_weight=15, reliability=0.90)
    network.add_route("CEDIS_Norte", "Cliente_2", cost=400, time=10, max_weight=40, reliability=0.92)
    network.add_route("CEDIS_Sur", "Cliente_2", cost=150, time=4, max_weight=25, reliability=0.97)
    network.add_route("CEDIS_Sur", "Cliente_3", cost=500, time=12, max_weight=45, reliability=0.85)

    print("=" * 60)
    print("SISTEMA DE OPTIMIZACIÓN LOGÍSTICA - PROYECTO INTEGRADOR")
    print("=" * 60)

    # ========== MÓDULO 1: Auditoría de Resiliencia ==========
    print("\n1. AUDITORÍA DE RESILIENCIA")
    print("-" * 40)
    
    print("\n--- Caso 1: Red completa (sin fallos) ---")
    report = network.audit_resilience()
    print(f"Resiliente: {report['is_resilient']}")
    print(f"Clientes aislados: {report['isolated_clients']}")
    
    print("\n--- Caso 2: Fallo en CEDIS_Norte ---")
    report_failure = network.audit_resilience(failed_nodes={"CEDIS_Norte"})
    print(f"Resiliente: {report_failure['is_resilient']}")
    print(f"Clientes aislados: {report_failure['isolated_clients']}")
    
    print("\n--- Caso 3: Fallo en CEDIS_Sur ---")
    report_failure2 = network.audit_resilience(failed_nodes={"CEDIS_Sur"})
    print(f"Resiliente: {report_failure2['is_resilient']}")
    print(f"Clientes aislados: {report_failure2['isolated_clients']}")

    # ========== MÓDULO 2: Motor de Ruteo Multi-Objetivo ==========
    print("\n2. MOTOR DE RUTEO MULTI-OBJETIVO")
    print("-" * 40)
    
    test_cases = [
        ("Fabrica_Alpha", "Cliente_2", 20, "COSTO"),
        ("Fabrica_Alpha", "Cliente_2", 20, "TIEMPO"),
        ("Fabrica_Alpha", "Cliente_2", 20, "CONFIABILIDAD"),
    ]
    
    for source, target, weight, criterion in test_cases:
        print(f"\n--- Ruta desde {source} hasta {target} (peso: {weight} tons, criterio: {criterion}) ---")
        result = network.find_optimal_route(source, target, weight, criterion)
        if result.get("success"):
            print(f"Ruta: {' -> '.join(result['path'])}")
            print(f"Costo total: ${result['total_cost']}")
            print(f"Tiempo total: {result['total_time']} hrs")
            print(f"Confiabilidad: {result['total_reliability']:.2%}")
        else:
            print(f"Error: {result.get('message', 'No se encontró ruta')}")

    # Prueba de filtrado por peso
    print("\n--- Prueba de filtrado por peso (envío de 35 tons) ---")
    result_weight_filter = network.find_optimal_route("Fabrica_Alpha", "Cliente_2", 35, "COSTO")
    if result_weight_filter.get("success"):
        print(f"Ruta: {' -> '.join(result_weight_filter['path'])}")
        print(f"Detalles: {result_weight_filter['path_details']}")
    else:
        print(f"Error: {result_weight_filter.get('message')}")

    # ========== MÓDULO 3: Análisis de Cuellos de Botella ==========
    print("\n3. ANÁLISIS DE CUELLOS DE BOTELLA")
    print("-" * 40)
    
    capacity_test_cases = [
        ("Fabrica_Alpha", "Cliente_2", 100, 20, "COSTO"),  # Lote 100 ≤ capacidad
        ("Fabrica_Alpha", "Cliente_2", 250, 20, "COSTO"),  # Lote 250 > capacidad de CEDIS_Sur
        ("Fabrica_Beta", "Cliente_2", 300, 15, "TIEMPO"),  # Lote 300 > capacidad de CEDIS_Sur
    ]
    
    for source, target, batch, weight, criterion in capacity_test_cases:
        print(f"\n--- Envío de {batch} tons (peso: {weight} tons) desde {source} hasta {target} ---")
        result = network.find_route_with_capacity_check(source, target, batch, weight, criterion)
        
        if result.get("success"):
            print(f"Ruta: {' -> '.join(result['path'])}")
            print(f"Factible: {result.get('feasible', False)}")
            print(f"Mensaje: {result.get('message', 'OK')}")
            
            if result.get("capacity_violations"):
                print("Violaciones de capacidad:")
                for violation in result["capacity_violations"]:
                    print(f"  - {violation['node']}: capacidad {violation['capacity']} < requerida {violation['required']}")
            
            if result.get("alternative_route"):
                alt = result["alternative_route"]
                print(f"Ruta alternativa: {' -> '.join(alt['path'])}")
                print(f"Costo alternativo: ${alt['total_cost']}")
        else:
            print(f"Error: {result.get('message', 'No se encontró solución')}")

    print("\n" + "=" * 60)
    print("SOLVER COMPLETADO EXITOSAMENTE")

if __name__ == "__main__":
    run_logistics_solver()
