"""Smart-WMS (Sistema Automatizado de Asignación de Balanceo de Carga Logística)

Imagina un almacén vertical Automatizado donde los Racks de almacenamiento están organizados jerárquicamente
siguiendo la estructura de un árbol binario de búsqueda (BST) para garantizar accesos ultra rápidos de tipo
O(logN). Cada nodo del árbol representa una bahía de almacenamiento que guarda un SKU (lote de producto)
específico.

Para que el robot montacargas no gaste batería de forma innecesaria moviéndose desproporcionadamente hacia
un solo lado del almacén, el árbol debe monitorear su balanceo. Además, el sistema debe ser capaz de despachar 
pedidor urgentes basándose en prioridades numéricas y generar reportes operativos en tiempo real. 

Requerimientos del Sistema (Estructura de Clases)

Deberás implementar un programa consolidado en Python estructurado bajo el paradigma de 
Programación Orientada a Objetos (POO) que contenga, como mínimo, las siguientes especificaciones:

1. Clase NodoSKU:
Cada nodo del almacén debe contener:
- id_sku (entero, clave única de indexación).
- descripción (string, nombre del producto).
- peso_lote (flotante, peso en kilogramos del lote almacenado).
- prioridad (entero, de 1 a 10, donde 1 es prioridad crítica).
- izquierdo y derecho (punteros subárboles).

2. Clase principal SmartWMS
Esta clase controlará el almacén y deberá implementar los siguientes 4 módulos opoerativos:

Módulo A: Gestión Avanzada de Inventario
- registrar_sku(id_sku, descripcion, peso_lote, prioridad): Inserta un nuevo lote en el lugar correcto
del BST.
- cargar_lote_masivo(lista_skus): Permite poblar el almacén rápidamente recibiendo una lista de tuplas.

Módulo B: Auditoría de Infraesctructura y reportes
- calcular_peso_total(): Utiliza un recorrido Post-order para calcular de forma acumulada el peso total (kg)
que están soportando las estructuras del almacén.
- generar_manifiesto_inorden(): Despliega en pantalla el inventario completo ordenado de menor a mayor por
su id_sku.
- obtener_alertas_desbalanceo(): Calcula la altura del subárbol izquierdo y derecho de la raiz principal.
Si la diferencia de alturas (factor de balance) es mayor a 1 o menor a -1, debe imprimir un mensaje de advertencia:
[ALERTA] requiere rotación de racks por desbalanceo de carga.

Módulo C: Algoritmo de Despacho Dinámico (Cola de prioridad Inversa)
- despachar_sku_critico(): Los clientes VIP o líneas de producción detenidas requieren extraer inmediatamente el 
lote que tenga la máxima prioridad (en este sistema, el ID de SKU más bajo representa el muelle de acceso
inmediato/urgente). La función debe:
1. Localizar el SKU con el menor ID de todo el almacén.
2. Imprimir sus datos confirmando la salida de la ruta.
3. Eliminarlo físicamente del árbol reestructurado el BST de forma correcta.

Módulo D: Trazabilidad y Purga por Obsolescencia
- purgar_rango_obsoletos(limite_inf, limite_sup): Si una sere de SKUs entra en cuarentena o caducidad, el sistema 
debe eliminarlos todos en bloque utilizando el algoritmo de purga por rango (Bottom-Up/Post-order).

Datos de entrega para la prueba de estrés (__main__):
Para validar que el sistema funciona bajo condiciones reales, el bloque principal de ejecución deberá 
automatizar las siguientes fases:
1. Fase de Carga: Registra masivamente al menos 7 u 8 SKUs.
2. Fase auditoría: Imprimir el manifiesto ordenado, calcular el peso acumulado en los racks y verificar
el estado de balanceo del layout.
3. Fase de Operación: Despachar las 2 órdenes más urgentes consecutivamente y mostrar cómo se reestructura el almacén.
4. Fase de Purga: Eliminar un rango intermedio de SKUs defectuosos (por ejemplo, del ID 35 al 65)
y demosttrar que el inventario restante sigue perfectamente conectado."""

class NodoSKU:
    def __init__(self, id_sku, descripcion, peso_lote, prioridad):
        self.id_sku = id_sku
        self.descripcion = descripcion
        self.peso_lote = peso_lote
        self.prioridad = prioridad
        self.izquierdo = None
        self.derecho = None
    
    def __str__(self):
        return f"ID: {self.id_sku}, Descripción: {self.descripcion}, Peso: {self.peso_lote}kg, Prioridad: {self.prioridad}"


class SmartWMS:
    def __init__(self):
        self.raiz = None
        self.total_nodos = 0
    
    # Módulo A: Gestión Avanzada de Inventario
    def registrar_sku(self, id_sku, descripcion, peso_lote, prioridad):
        if self.buscar_nodo(id_sku):
            print(f"[ERROR] El SKU {id_sku} ya existe en el inventario")
            return False
        
        nuevo_nodo = NodoSKU(id_sku, descripcion, peso_lote, prioridad)
        
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._insertar_recursivo(self.raiz, nuevo_nodo)
        
        self.total_nodos += 1
        print(f"[OK] SKU {id_sku} registrado exitosamente")
        return True
    
    def _insertar_recursivo(self, nodo_actual, nuevo_nodo):
        if nuevo_nodo.id_sku < nodo_actual.id_sku:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = nuevo_nodo
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, nuevo_nodo)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = nuevo_nodo
            else:
                self._insertar_recursivo(nodo_actual.derecho, nuevo_nodo)
    
    def buscar_nodo(self, id_sku):
        return self._buscar_recursivo(self.raiz, id_sku)
    
    def _buscar_recursivo(self, nodo_actual, id_sku):
        if nodo_actual is None:
            return None
        if nodo_actual.id_sku == id_sku:
            return nodo_actual
        elif id_sku < nodo_actual.id_sku:
            return self._buscar_recursivo(nodo_actual.izquierdo, id_sku)
        else:
            return self._buscar_recursivo(nodo_actual.derecho, id_sku)
    
    def cargar_lote_masivo(self, lista_skus):
        if not lista_skus:
            print("[INFO] Lista vacía, no se cargaron SKUs")
            return
        
        exitos = 0
        fallos = 0
        
        for sku_data in lista_skus:
            if len(sku_data) == 4:
                id_sku, descripcion, peso_lote, prioridad = sku_data
                if self.registrar_sku(id_sku, descripcion, peso_lote, prioridad):
                    exitos += 1
                else:
                    fallos += 1
            else:
                print(f"[ERROR] Datos inválidos para SKU: {sku_data}")
                fallos += 1
        
        print(f"\n[RESUMEN CARGA] SKUs cargados: {exitos}, Fallos: {fallos}")
    
    # Módulo B: Auditoría de Infraestructura y Reportes
    def calcular_peso_total(self):
        if self.raiz is None:
            return 0.0
        
        peso_total = self._calcular_peso_postorden(self.raiz)
        print(f"[PESO TOTAL] El peso acumulado en el almacén es: {peso_total:.2f} kg")
        return peso_total
    
    def _calcular_peso_postorden(self, nodo):
        if nodo is None:
            return 0.0
        
        peso_izq = self._calcular_peso_postorden(nodo.izquierdo)
        peso_der = self._calcular_peso_postorden(nodo.derecho)
        
        return peso_izq + peso_der + nodo.peso_lote
    
    def generar_manifiesto_inorden(self):
        if self.raiz is None:
            print("[MANIFIESTO] El almacén está vacío")
            return
        
        print("\n---Manifiesto de Inventario (Ordenado por ID) ---")
        print("ID     | Descripción              | Peso(kg) | Prioridad")
        self._recorrido_inorden(self.raiz)
    
    def _recorrido_inorden(self, nodo):
        if nodo is not None:
            self._recorrido_inorden(nodo.izquierdo)
            print(f"{nodo.id_sku:6d} | {nodo.descripcion:24s} | {nodo.peso_lote:8.2f} | {nodo.prioridad:8d}")
            self._recorrido_inorden(nodo.derecho)
    
    def obtener_alertas_desbalanceo(self):
        if self.raiz is None:
            print("[ALERTA] El almacén está vacío")
            return
        
        altura_izq = self._calcular_altura(self.raiz.izquierdo)
        altura_der = self._calcular_altura(self.raiz.derecho)
        factor_balance = altura_izq - altura_der
        
        print(f"\n[ANÁLISIS DE BALANCE] Altura izquierda: {altura_izq}, Altura derecha: {altura_der}")
        print(f"Factor de balance: {factor_balance}")
        
        if abs(factor_balance) > 1:
            print("[ALERTA] Requiere rotación de racks por desbalanceo de carga")
            if factor_balance > 1:
                print("-> El lado izquierdo está más pesado (sobrecarga en zona A)")
            else:
                print("-> El lado derecho está más pesado (sobrecarga en zona B)")
        else:
            print("[OK] El almacén está balanceado correctamente")
        
        return factor_balance
    
    def _calcular_altura(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self._calcular_altura(nodo.izquierdo), self._calcular_altura(nodo.derecho))
    
    # Módulo C: Algoritmo de Despacho Dinámico
    def despachar_sku_critico(self):
        if self.raiz is None:
            print("[ERROR] No hay SKUs para despachar")
            return None
        
        nodo_actual = self.raiz
        padre = None
        while nodo_actual.izquierdo is not None:
            padre = nodo_actual
            nodo_actual = nodo_actual.izquierdo
        
        sku_despachado = nodo_actual
        
        if nodo_actual.derecho is not None:
            if padre is None:
                self.raiz = nodo_actual.derecho
            else:
                padre.izquierdo = nodo_actual.derecho
        else:
            if padre is None:
                self.raiz = None
            else:
                padre.izquierdo = nodo_actual.izquierdo
        
        nodo_actual.izquierdo = None
        nodo_actual.derecho = None
        
        self.total_nodos -= 1
        
        print(f"\n[DESPACHO URGENTE] SKU {sku_despachado.id_sku} despachado a ruta")
        print(f"-> {sku_despachado}")
        print(f"-> Prioridad: {sku_despachado.prioridad} (crítica)")
        
        return sku_despachado
    
    # Módulo D: Trazabilidad y Purga por Obsolescencia
    def purgar_rango_obsoletos(self, limite_inf, limite_sup):
        if self.raiz is None:
            print("[ERROR] El almacén está vacío")
            return
        
        nodos_a_eliminar = []
        self._recopilar_nodos_rango(self.raiz, limite_inf, limite_sup, nodos_a_eliminar)
        
        if not nodos_a_eliminar:
            print(f"[INFO] No se encontraron SKUs en el rango [{limite_inf}, {limite_sup}]")
            return
        
        print(f"\n[PURGA] Eliminando {len(nodos_a_eliminar)} SKUs obsoletos...")
        
        for nodo in nodos_a_eliminar:
            self._eliminar_nodo(nodo.id_sku)
            print(f"-> SKU {nodo.id_sku} eliminado (purga por obsolescencia)")
        
        print(f"[PURGA COMPLETA] {len(nodos_a_eliminar)} SKUs eliminados del rango [{limite_inf}, {limite_sup}]")
    
    def _recopilar_nodos_rango(self, nodo, limite_inf, limite_sup, lista_nodos):
        if nodo is None:
            return
        
        self._recopilar_nodos_rango(nodo.izquierdo, limite_inf, limite_sup, lista_nodos)
        self._recopilar_nodos_rango(nodo.derecho, limite_inf, limite_sup, lista_nodos)
        
        if limite_inf <= nodo.id_sku <= limite_sup:
            lista_nodos.append(nodo)
    
    def _eliminar_nodo(self, id_sku):
        self.raiz = self._eliminar_recursivo(self.raiz, id_sku)
        self.total_nodos -= 1
    
    def _eliminar_recursivo(self, nodo, id_sku):
        if nodo is None:
            return None
        
        if id_sku < nodo.id_sku:
            nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, id_sku)
        elif id_sku > nodo.id_sku:
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, id_sku)
        else:
            if nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo
            else:
                sucesor = self._encontrar_minimo(nodo.derecho)
                nodo.id_sku = sucesor.id_sku
                nodo.descripcion = sucesor.descripcion
                nodo.peso_lote = sucesor.peso_lote
                nodo.prioridad = sucesor.prioridad
                nodo.derecho = self._eliminar_recursivo(nodo.derecho, sucesor.id_sku)
        
        return nodo
    
    def _encontrar_minimo(self, nodo):
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual


def main():
    print("--- Prueba de estrés ---\n")
    
    wms = SmartWMS()
    
    # Fase 1: Carga de datos
    print("Fase 1: Carga de Inventario")
    skus_iniciales = [
        (50, "Componentes Electrónicos", 150.5, 3),
        (30, "Piezas Mecánicas", 200.0, 5),
        (70, "Materiales Plásticos", 75.3, 7),
        (20, "Productos Químicos", 320.8, 2),
        (40, "Elementos de Fijación", 45.6, 6),
        (60, "Herramientas Manuales", 180.2, 4),
        (80, "Embalajes y Envases", 95.7, 8),
        (25, "Componentes Eléctricos", 210.4, 1)
    ]
    
    wms.cargar_lote_masivo(skus_iniciales)
    
    # Fase 2: Auditoría
    print("\nFase 2: Auditoría de Infraestructura")
    wms.generar_manifiesto_inorden()
    wms.calcular_peso_total()
    wms.obtener_alertas_desbalanceo()
    
    # Fase 3: Operación de despacho
    print("\nFase 3: Despacho Urgente")
    print("Despachando SKU más crítico (menor ID)...")
    sku_critico = wms.despachar_sku_critico()
    
    print("\nDespachando siguiente SKU crítico...")
    siguiente_critico = wms.despachar_sku_critico()
    
    print("\nEstado del almacén después de despachos:")
    wms.generar_manifiesto_inorden()
    wms.calcular_peso_total()
    
    # Fase 4: Purga por obsolescencia
    print("\nFase 4: Purga por obsolencia")
    print("Eliminando SKUs en rango [35, 65]...")
    wms.purgar_rango_obsoletos(35, 65)
    
    print("\nInventario después de la purga:")
    wms.generar_manifiesto_inorden()
    wms.calcular_peso_total()
    wms.obtener_alertas_desbalanceo()
    
    print(f"Total de SKUs en almacén: {wms.total_nodos}")

if __name__ == "__main__":
    main()
