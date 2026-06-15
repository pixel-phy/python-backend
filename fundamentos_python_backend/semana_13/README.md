# Algoritmos Clásicos

Los **algoritmos clásicos** de búsqueda y ordenamiento son la base de la computación.Son herramientas poderosas en el mundo real. En logística, la eficiencia en el manejo de datos se traduce directamente en ahorro de tiempo, combustible y dinero.

### ¿Por qué son importantes en logística?

En el día a día logístico se manejan grandes volúmenes de información:
- Inventarios con miles de productos.
- Rutas de entrega.
- Pedidos de clientes.
- Vehículos en un centro de distribución.

Aplicar algoritmos eficientes permite:

| Necesidad logística | Algoritmo útil |
|---------------------|----------------|
| Encontrar rápido un paquete en un almacén desordenado | Búsqueda lineal |
| Localizar un pedido en un inventario ordenado por código | Búsqueda binaria |
| Organizar envíos por prioridad (más cercano → más lejano) | Ordenamiento burbuja / selección |
| Insertar una nueva orden en una lista de entregas ya ordenada | Ordenamiento por inserción |

---
## Temario semanal

### 📅 Día 1 – Búsqueda Lineal
- Recorrer elemento por elemento en contextos de entrada/salida (IO).
- Ideal para listas desordenadas o cuando no se tiene información previa.
- Complejidad: O(n).
- **En logística**: Útil cuando un camión llega con mercancía sin etiquetar y hay que revisar manualmente lote por lote.

### 📅 Día 2 – Búsqueda Binaria
- Búsqueda eficiente en listas **ordenadas**.
- Divide el rango de búsqueda a la mitad en cada paso.
- Complejidad: O(log n).
- **En logística**: Localizar un contenedor en un almacén ordenado por número de lote o código de barras.

### 📅 Día 3 – Ordenamiento Burbuja
- Intercambio de elementos adyacentes repetidamente.
- El elemento más grande "burbujea" hacia el final.
- Complejidad: O(n²) en el peor caso.
- **En logística**: Útil didácticamente, pero en la práctica se usa para listas muy pequeñas (ej: ordenar 10 rutas de entrega en una misma zona).

### 📅 Día 4 – Ordenamiento por Selección
- Selecciona repetidamente el **mínimo** (o máximo) y lo coloca en su posición correcta.
- Menos intercambios que burbuja, pero aún O(n²).
- **En logística**: Elegir el pedido más urgente o la ruta más corta de forma sistemática.

### 📅 Día 5 – Ordenamiento por Inserción
- Construye la lista ordenada insertando cada elemento en su lugar correcto.
- Muy eficiente para listas casi ordenadas (O(n) en el mejor caso).
- **En logística**: Insertar una nueva entrega urgente en una lista de rutas ya casi ordenadas por horario.

### 📅 Día 6 – Ejercicios Integradores
- Combinar búsqueda y ordenamiento:
  - Ordenar con inserción/selección y luego buscar con binaria.
  - Comparar tiempos con búsqueda lineal.
- **En logística**: 
  - Ordenar pedidos por código postal y buscar rápidamente los de una zona.
  - Simular un centro de distribución que recibe productos desordenados y necesita responder consultas rápido.

### 📅 Día 7 – Proyecto Integrador
- Aplicar todos los conceptos en un proyecto completo.
- **Propuesta logística**: 
  - Sistema de gestión de un pequeño almacén.
  - Funcionalidades: agregar productos (con código, nombre, ubicación), ordenar por código, buscar producto por código, mostrar inventario ordenado.
  - Implementar al menos un algoritmo de búsqueda (lineal o binaria) y uno de ordenamiento (selección, inserción o burbuja).

---
