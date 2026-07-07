import math
import csv
import os
from typing import List, Dict, Tuple, Optional

# MÓDULO 1: GESTIÓN DE NODOS (UBICACIONES)

class Nodo:
    def __init__(self, id_nodo: str, nombre: str, x: float, y: float, demanda: float = 0.0, oferta: float = 0.0):
        self.__id = id_nodo
        self.__nombre = nombre
        self.x = x
        self.y = y
        self.demanda = demanda
        self.oferta = oferta

    # Properties con validaciones
    @property
    def id(self) -> str: return self.__id

    @property
    def nombre(self) -> str: return self.__nombre

    @property
    def x(self) -> float: return self.__x
    @x.setter
    def x(self, val: float): self.__x = float(val)

    @property
    def y(self) -> float: return self.__y
    @y.setter
    def y(self, val: float): self.__y = float(val)

    @property
    def demanda(self) -> float: return self.__demanda
    @demanda.setter
    def demanda(self, val: float):
        if float(val) < 0: raise ValueError("La demanda no puede ser negativa.")
        self.__demanda = float(val)

    @property
    def oferta(self) -> float: return self.__oferta
    @oferta.setter
    def oferta(self, val: float):
        if float(val) < 0: raise ValueError("La oferta no puede ser negativa.")
        self.__oferta = float(val)

    # Métodos
    def distancia_a(self, otro_nodo: 'Nodo') -> float:
        return math.sqrt((self.__x - otro_nodo.x)**2 + (self.__y - otro_nodo.y)**2)

    def es_oferente(self) -> bool: return self.__oferta > 0
    def es_demandante(self) -> bool: return self.__demanda > 0

    def __repr__(self) -> str:
        return f"Nodo('{self.__id}', '{self.__nombre}', {self.__x}, {self.__y}, {self.__demanda}, {self.__oferta})"

    def __str__(self) -> str:
        return f"[{self.__id}] {self.__nombre} (Ofert: {self.__oferta} | Dem: {self.__demanda})"

    @classmethod
    def desde_csv(cls, linea_csv: str) -> 'Nodo':
        # Formato esperado: id,nombre,x,y,demanda,oferta
        lector = csv.reader([linea_csv])
        datos = next(lector)
        return cls(datos[0], datos[1], float(datos[2]), float(datos[3]), float(datos[4]), float(datos[5]))


class GestorNodos:
    def __init__(self):
        self.__nodos: Dict[str, Nodo] = {}  # Composición

    # CRUD
    def crear(self, nodo: Nodo) -> bool:
        if nodo.id in self.__nodos: return False
        self.__nodos[nodo.id] = nodo
        return True

    def leer(self, id_nodo: str) -> Optional[Nodo]:
        return self.__nodos.get(id_nodo)

    def actualizar(self, id_nodo: str, **kwargs) -> bool:
        nodo = self.leer(id_nodo)
        if not nodo: return False
        for llave, valor in kwargs.items():
            if hasattr(nodo, llave): setattr(nodo, llave, valor)
        return True

    def eliminar(self, id_nodo: str) -> bool:
        if id_nodo in self.__nodos:
            del self.__nodos[id_nodo]
            return True
        return False

    # Búsquedas y listados
    def buscar_por_id(self, id_nodo: str) -> Optional[Nodo]:
        return self.leer(id_nodo)

    def buscar_por_nombre(self, nombre: str) -> Optional[Nodo]:
        for nodo in self.__nodos.values():
            if nodo.nombre.lower() == nombre.lower(): return nodo
        return None

    def obtener_todos(self) -> List[Nodo]:
        return list(self.__nodos.values())

    def listar_todos(self) -> str:
        lineas = [f"{'ID':<6} | {'Nombre':<15} | {'X':<5} | {'Y':<5} | {'Demanda':<8} | {'Oferta':<8}"]
        lineas.append("-" * 60)
        for n in self.__nodos.values():
            lineas.append(f"{n.id:<6} | {n.nombre:<15} | {n.x:<5.1f} | {n.y:<5.1f} | {n.demanda:<8.1f} | {n.oferta:<8.1f}")
        return "\n".join(lineas)

# MÓDULO 2: GESTIÓN DE RUTAS (ARISTAS)

class Ruta:
    def __init__(self, origen: str, destino: str, distancia: float, costo: float, capacidad: float):
        self.__origen = origen
        self.__destino = destino
        self.distancia = distancia
        self.costo = costo
        self.capacidad = capacity = capacidad
        self.__flujo = 0.0

    @property
    def origen(self) -> str: return self.__origen
    @property
    def destino(self) -> str: return self.__destino

    @property
    def distancia(self) -> float: return self.__distancia
    @distancia.setter
    def distancia(self, val: float): self.__distancia = float(val)

    @property
    def costo(self) -> float: return self.__costo
    @costo.setter
    def costo(self, val: float):
        if float(val) < 0: raise ValueError("El costo no puede ser negativo.")
        self.__costo = float(val)

    @property
    def capacidad(self) -> float: return self.__capacidad
    @capacidad.setter
    def capacidad(self, val: float):
        if float(val) < 0: raise ValueError("La capacidad no puede ser negativa.")
        self.__capacidad = float(val)

    @property
    def flujo(self) -> float: return self.__flujo
    @flujo.setter
    def flujo(self, val: float):
        if float(val) < 0: raise ValueError("El flujo no puede ser negativo.")
        if float(val) > self.__capacidad: raise ValueError("El flujo no puede exceder la capacidad.")
        self.__flujo = float(val)

    @property
    def flujo_disponible(self) -> float:
        return self.__capacidad - self.__flujo

    def enviar_flujo(self, cantidad: float) -> bool:
        if cantidad <= self.flujo_disponible:
            self.flujo += cantidad
            return True
        return False

    def costo_total(self) -> float:
        return self.__flujo * self.__costo

    def esta_saturada(self) -> bool:
        return self.__flujo >= self.__capacidad

    @staticmethod
    def calcular_costo_por_distancia(distancia: float, factor_costo: float) -> float:
        return distancia * factor_costo


class GestorRutas:
    def __init__(self, gestor_nodos: GestorNodos):
        self.__rutas: List[Ruta] = []  # Composición
        self.gestor_nodos = gestor_nodos  # Agregación

    def crear(self, ruta: Ruta) -> bool:
        if not self.gestor_nodos.buscar_por_id(ruta.origen) or not self.gestor_nodos.buscar_por_id(ruta.destino):
            return False  # Validación de existencia de nodos
        self.__rutas.append(ruta)
        return True

    def obtener_todas(self) -> List[Ruta]:
        return self.__rutas

    def eliminar(self, origen: str, destino: str) -> bool:
        for r in self.__rutas:
            if r.origen == origen and r.destino == destino:
                self.__rutas.remove(r)
                return True
        return False

    def buscar_ruta(self, origen: str, destino: str) -> Optional[Ruta]:
        for r in self.__rutas:
            if r.origen == origen and r.destino == destino: return r
        return None

    def rutas_desde(self, nodo_id: str) -> List[Ruta]:
        return [r for r in self.__rutas if r.origen == nodo_id]

    def rutas_hacia(self, nodo_id: str) -> List[Ruta]:
        return [r for r in self.__rutas if r.destino == nodo_id]

    def calcular_flujo_total(self) -> float:
        return sum(r.flujo for r in self.__rutas)

    def calcular_costo_total(self) -> float:
        return sum(r.costo_total() for r in self.__rutas)

# MÓDULO 3: SIMULACIÓN DE RED

class SimuladorRed:
    TIEMPO_SIMULACION = 100
    PASO_TIEMPO = 1

    def __init__(self, gestor_nodos: GestorNodos, gestor_rutas: GestorRutas):
        self.gestor_nodos = gestor_nodos  # Agregación
        self.gestor_rutas = gestor_rutas  # Agregación
        self.__historial_envios = []

    def simular_flujo(self, origen: str, destino: str, cantidad: float) -> bool:
        ruta = self.gestor_rutas.buscar_ruta(origen, destino)
        if ruta and ruta.enviar_flujo(cantidad):
            self.__historial_envios.append({"origen": origen, "destino": destino, "cantidad": cantidad, "exito": True})
            return True
        self.__historial_envios.append({"origen": origen, "destino": destino, "cantidad": cantidad, "exito": False})
        return False

    def simular_demanda(self):
        # Envía flujos simples directos basados en ofertas y demandas disponibles
        for n_origen in self.gestor_nodos.obtener_todos():
            if n_origen.es_oferente():
                for r in self.gestor_rutas.rutas_desde(n_origen.id):
                    n_destino = self.gestor_nodos.buscar_por_id(r.destino)
                    if n_destino and n_destino.es_demandante():
                        envio = min(n_origen.oferta, n_destino.demanda, r.flujo_disponible)
                        if envio > 0:
                            if self.simular_flujo(n_origen.id, n_destino.id, envio):
                                n_origen.oferta -= envio
                                n_destino.demanda -= envio

    def estadisticas_simulacion(self) -> dict:
        total_intentos = len(self.__historial_envios)
        exitosos = len([e for e in self.__historial_envios if e["exito"]])
        return {
            "total_intentos": total_intentos,
            "envios_exitosos": exitosos,
            "flujo_total": self.gestor_rutas.calcular_flujo_total(),
            "costo_total": self.gestor_rutas.calcular_costo_total()
        }

    def reporte_estado_actual(self) -> str:
        res = ["=== ESTADO ACTUAL DE LA RED ==="]
        for r in self.gestor_rutas.obtener_todas():
            sat = "[SATURADA]" if r.esta_saturada() else ""
            res.append(f"Ruta {r.origen} -> {r.destino} | Flujo: {r.flujo}/{r.capacidad} | Costo Acum: ${r.costo_total()} {sat}")
        return "\n".join(res)

    @staticmethod
    def validar_ruta_completa(nodos_ruta: List[str], gestor_rutas: GestorRutas) -> bool:
        for i in range(len(nodos_ruta) - 1):
            if not gestor_rutas.buscar_ruta(nodos_ruta[i], nodos_ruta[i+1]): return False
        return True

    @staticmethod
    def calcular_costo_ruta(nodos_ruta: List[str], gestor_rutas: GestorRutas) -> float:
        total = 0.0
        for i in range(len(nodos_ruta) - 1):
            r = gestor_rutas.buscar_ruta(nodos_ruta[i], nodos_ruta[i+1])
            if r: total += r.costo
        return total

    @staticmethod
    def formatear_resultado_simulacion(datos: dict) -> str:
        return (f"--- RESUMEN SIMULACIÓN ---\n"
                f"Envíos Procesados: {datos['total_intentos']} (Éxitos: {datos['envios_exitosos']})\n"
                f"Flujo Movilizado : {datos['flujo_total']} unidades\n"
                f"Costo de Red Total: ${datos['costo_total']:.2f}")

# MÓDULO 4: OPTIMIZACIÓN DE RUTAS

class OptimizadorRutas:
    ALGORITMO_DEFAULT = "dijkstra"
    MAX_ITERACIONES = 1000

    def __init__(self, gestor_rutas: GestorRutas):
        self.gestor_rutas = gestor_rutas  # Asociación / Agregación externa

    @classmethod
    def configurar(cls, algoritmo: str, max_iter: int):
        cls.ALGORITMO_DEFAULT = algoritmo
        cls.MAX_ITERACIONES = max_iter

    def __obtener_grafo(self, criterio: str) -> Tuple[set, dict]:
        nodos = set()
        adj = {}
        for r in self.gestor_rutas.obtener_todas():
            nodos.add(r.origen)
            nodos.add(r.destino)
            if r.origen not in adj: adj[r.origen] = []
            peso = r.distancia if criterio == "distancia" else r.costo
            adj[r.origen].append((r.destino, peso))
        return nodos, adj

    def __dijkstra_generico(self, origen: str, destino: str, criterio: str) -> List[str]:
        nodos, adj = self.__obtener_grafo(criterio)
        if origen not in nodos or destino not in nodos: return []
        
        distancias = {n: float('inf') for n in nodos}
        previos = {n: None for n in nodos}
        distancias[origen] = 0
        no_visitados = list(nodos)

        iteraciones = 0
        while no_visitados and iteraciones < self.MAX_ITERACIONES:
            iteraciones += 1
            u = min(no_visitados, key=lambda n: distancias[n])
            if distancias[u] == float('inf') or u == destino: break
            no_visitados.remove(u)

            for v, peso in adj.get(u, []):
                alt = distancias[u] + peso
                if alt < distancias[v]:
                    distancias[v] = alt
                    previos[v] = u

        ruta = []
        actual = destino
        while actual:
            ruta.insert(0, actual)
            actual = previos[actual]
        return ruta if ruta[0] == origen else []

    def ruta_mas_corta(self, origen: str, destino: str) -> List[str]:
        return self.__dijkstra_generico(origen, destino, "distancia")

    def ruta_menor_costo(self, origen: str, destino: str) -> List[str]:
        return self.__dijkstra_generico(origen, destino, "costo")

    def flujo_maximo(self, origen: str, destino: str) -> float:
        # Implementación de Ford-Fulkerson (Edmonds-Karp simplificado)
        rutas = self.gestor_rutas.obtener_todas()
        flujo_max = 0.0
        
        def bfs_camino_aumento():
            parent = {origen: None}
            queue = [origen]
            while queue:
                u = queue.pop(0)
                for r in rutas:
                    if r.origen == u and r.flujo_disponible > 0 and r.destino not in parent:
                        parent[r.destino] = r
                        if r.destino == destino: return parent
                        queue.append(r.destino)
            return None

        for _ in range(self.MAX_ITERACIONES):
            camino = bfs_camino_aumento()
            if not camino: break
            
            # Calcular cuello de botella
            curr = destino
            cuello_botella = float('inf')
            while curr != origen:
                r = camino[curr]
                cuello_botella = min(cuello_botella, r.flujo_disponible)
                curr = r.origen
            
            # Enviar flujo
            curr = destino
            while curr != origen:
                r = camino[curr]
                r.enviar_flujo(cuello_botella)
                curr = r.origen
            flujo_max += cuello_botella

        return flujo_max

    def arbol_expansion_minima(self) -> List[Tuple[str, str, float]]:
        # Algoritmo de Kruskal simplificado
        rutas = sorted(self.gestor_rutas.obtener_todas(), key=lambda x: x.distancia)
        parent = {}
        
        def find(i):
            if parent[i] == i: return i
            return find(parent[i])

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            parent[root_i] = root_j

        mst = []
        for r in rutas:
            if r.origen not in parent: parent[r.origen] = r.origen
            if r.destino not in parent: parent[r.destino] = r.destino
            
            if find(r.origen) != find(r.destino):
                union(r.origen, r.destino)
                mst.append((r.origen, r.destino, r.distancia))
        return mst

    @staticmethod
    def distancia_total(ruta_nodos: List[str], gestor_rutas: GestorRutas) -> float:
        total = 0.0
        for i in range(len(ruta_nodos) - 1):
            r = gestor_rutas.buscar_ruta(ruta_nodos[i], ruta_nodos[i+1])
            if r: total += r.distancia
        return total

# MÓDULO 5: REPORTES Y VISUALIZACIÓN

class ReporteadorRed:
    def __init__(self, gestor_nodos: GestorNodos, gestor_rutas: GestorRutas, optimizador: OptimizadorRutas):
        self.gn = gestor_nodos
        self.gr = gestor_rutas
        self.opt = optimizador

    def reporte_nodos(self) -> str:
        columnas = ["ID", "Nombre", "X", "Y", "Demanda", "Oferta"]
        datos = [[n.id, n.nombre, str(n.x), str(n.y), str(n.demanda), str(n.oferta)] for n in self.gn.obtener_todos()]
        return "--- REPORTE DE NODOS ---\n" + self.formatear_tabla(datos, columnas)

    def reporte_rutas(self) -> str:
        columnas = ["Origen", "Destino", "Distancia", "Costo", "Capacidad", "Flujo"]
        datos = [[r.origen, r.destino, str(r.distancia), f"${r.costo}", str(r.capacidad), str(r.flujo)] for r in self.gr.obtener_todas()]
        return "--- REPORTE DE RUTAS ---\n" + self.formatear_tabla(datos, columnas)

    def reporte_optimizacion(self) -> str:
        nodos = self.gn.obtener_todos()
        if len(nodos) < 2: return "No hay suficientes nodos para optimizar."
        orig, dest = nodos[0].id, nodos[-1].id
        rc = self.opt.ruta_mas_corta(orig, dest)
        rmc = self.opt.ruta_menor_costo(orig, dest)
        
        return (f"--- ANÁLISIS DE OPTIMIZACIÓN ({orig} -> {dest}) ---\n"
                f"Ruta Más Corta (Dijkstra Distancia): {' -> '.join(rc) if rc else 'No hay ruta'}\n"
                f"Ruta Menor Costo (Dijkstra Costo)  : {' -> '.join(rmc) if rmc else 'No hay ruta'}\n")

    def reporte_completo(self) -> str:
        return f"{self.reporte_nodos()}\n\n{self.reporte_rutas()}\n\n{self.reporte_optimizacion()}"

    def exportar_reporte_csv(self, nombre_archivo: str):
        with open(nombre_archivo, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["--- NODOS ---"])
            writer.writerow(["ID", "Nombre", "X", "Y", "Demanda", "Oferta"])
            for n in self.gn.obtener_todos(): writer.writerow([n.id, n.nombre, n.x, n.y, n.demanda, n.oferta])

    def exportar_reporte_txt(self, nombre_archivo: str):
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            f.write(self.reporte_completo())

    @classmethod
    def formatear_tabla(cls, datos: List[List[str]], columnas: List[str]) -> str:
        anchos = [len(c) for c in columnas]
        for fila in datos:
            for i, val in enumerate(fila): anchos[i] = max(anchos[i], len(val))
        
        formato = " | ".join([f"{{:<{a}}}" for a in anchos])
        lineas = [formato.format(*columnas), "-" * (sum(anchos) + 3 * (len(columnas) - 1))]
        for fila in datos: lineas.append(formato.format(*fila))
        return "\n".join(lineas)

    @classmethod
    def generar_resumen_estadistico(cls, datos: List[float]) -> str:
        if not datos: return "Sin datos."
        return f"Min: {min(datos)}, Max: {max(datos)}, Prom: {sum(datos)/len(datos):.2f}"

    @classmethod
    def colorear_estado(cls, valor: float, umbral: float) -> str:
        # Simulación de colores mediante texto decorado
        return f"⚠️ [{valor}]" if valor >= umbral else f"✅ [{valor}]"


# =====================================================================
# MÓDULO 6: SISTEMA PRINCIPAL E INTERFAZ
# =====================================================================

class SistemaRed:
    def __init__(self):
        self.gestor_nodos = GestorNodos()
        self.gestor_rutas = GestorRutas(self.gestor_nodos)
        self.simulador = SimuladorRed(self.gestor_nodos, self.gestor_rutas)
        self.optimizador = OptimizadorRutas(self.gestor_rutas)
        self.reporteador = ReporteadorRed(self.gestor_nodos, self.gestor_rutas, self.optimizador)

    def cargar_datos_manual(self):
        # Carga de Nodos de Ejemplo
        nodos_ejemplo = [
            Nodo("N1", "Bogotá", 0, 0, 100, 0),
            Nodo("N2", "Medellín", 4, 3, 0, 150),
            Nodo("N3", "Cali", 6, 5, 80, 0),
            Nodo("N4", "Barranquilla", 8, 2, 0, 100),
            Nodo("N5", "Cartagena", 10, 4, 50, 0)
        ]
        for n in nodos_ejemplo: self.gestor_nodos.crear(n)

        # Carga de Rutas de Ejemplo
        rutas_ejemplo = [
            Ruta("N1", "N2", 5, 10, 200),
            Ruta("N1", "N3", 8, 16, 150),
            Ruta("N2", "N3", 3, 6, 100),
            Ruta("N2", "N4", 6, 12, 120),
            Ruta("N3", "N4", 4, 8, 80),
            Ruta("N4", "N5", 5, 10, 90),
            Ruta("N3", "N5", 7, 14, 60)
        ]
        for r in rutas_ejemplo: self.gestor_rutas.crear(r)

    def ejecutar_simulacion(self):
        print("\n>> Ejecutando Simulación de Demandas...")
        self.simulador.simular_demanda()
        stats = self.simulador.estadisticas_simulacion()
        print(SimuladorRed.formatear_resultado_simulacion(stats))

    def exportar_resultados(self, carpeta: str):
        if not os.path.exists(carpeta): os.makedirs(carpeta)
        self.reporteador.exportar_reporte_txt(os.path.join(carpeta, "reporte.txt"))
        self.reporteador.exportar_reporte_csv(os.path.join(carpeta, "reporte.csv"))
        print(f"\n[!] Reportes exportados exitosamente en la carpeta '{carpeta}/'")


if __name__ == "__main__":
    # 1. Crear instancia del Sistema Coordinador
    sistema = SistemaRed()
    
    # 2. Cargar datos de ejemplo
    sistema.cargar_datos_manual()
    
    # Mostrar estado inicial de Nodos y Rutas cargadas
    print(sistema.reporteador.reporte_nodos())
    print("\n" + sistema.reporteador.reporte_rutas())
    
    # 3. Ejecutar simulación de demanda
    sistema.ejecutar_simulacion()
    
    # 4. Calcular rutas óptimas entre N1 y N5
    print("\n" + sistema.reporteador.reporte_optimizacion())
    
    # Demostración del algoritmo de Flujo Máximo de Ford-Fulkerson en la red
    flujo_max = sistema.optimizador.flujo_maximo("N1", "N5")
    print(f"Flujo Máximo Adicional Calculado (N1 -> N5): {flujo_max} unidades.")
    
    # 5 & 6. Generar reportes completos y exportar resultados
    sistema.exportar_resultados("salida_reportes")
