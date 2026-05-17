"""Lista enlazada de tareas:
Una aplicación de tareas pendientes necesita almacenar tareas en orden de creación. 
Cada tarea tiene:
- Descripción.
- Completada (True, False).
Requisitos:
1. Crear manualmente 3 nodos con las tareas:
- Estudiar Python.
- Hacer ejercicio.
- Leer un libro.
2. Enlazarlos en el orden de creación.
3. Marcar como completada la segunda tarea (cambiar completada a True)
4. Recorrer la lista y mostrar cada tarea con su estado:
- Si está completada: ✅ Estudiar Python
- Si no: ❌ Hacer ejercicio
5. Contar cuántas tareas están completadas
6. Insertar una nueva tarea ("Practicar código) al inicio de la lista.
7. Recorrer nuevamente para verificar que la nueva tarea está al inicio."""

# Se crea nodo principal
class NodoTareas:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False
        self.siguiente = None

# Se asignan descripciones de las tareas
nodo1 = NodoTareas("Estudiar Python")
nodo2 = NodoTareas("Hacer ejercicio")
nodo3 = NodoTareas("Leer un libro")

# Se enlazan en orden de creación
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

# Marcar como completada la segunda tarea
nodo2.completada = True

# Recorremos la lista para mostrar el estado de cada tarea
actual = nodo1
tareas_completadas = 0

print("\nLista de tareas:")
while actual:
    if actual.completada:
        print(f"✅ {actual.descripcion}")
        actual = actual.siguiente
        tareas_completadas += 1
    else:
        print(f"❌ {actual.descripcion}")
        actual = actual.siguiente

print(f"Tareas completadas: {tareas_completadas}")

# Insertar nueva tarea
nueva = NodoTareas("Practicar código")
nueva.siguiente = nodo1
nodo1 = nueva
# Recorremos nuevamente la lista para verificar

actual = nodo1
tareas_completadas = 0
print("\nLista de tareas actualizada: ")
while actual:
    if actual.completada:
        print(f"✅ {actual.descripcion}")
        actual = actual.siguiente
        tareas_completadas += 1
    else:
        print(f"❌ {actual.descripcion}")
        actual = actual.siguiente

print(f"Tareas completadas: {tareas_completadas}")