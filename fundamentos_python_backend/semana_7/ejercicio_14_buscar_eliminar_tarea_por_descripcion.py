"""Buscar y eliminar tarea por descripción:
La misma lista de tareas del ejercicio anterior. Ahora el usuario puede buscar una tarea por su descripción y eliminarla.
Requisitos:
1. Crear una lista de tareas (las 4 en ese orden).
2. Recorrer y mostras las tareas actuales.
3. Buscar una tarea por su descripción.
4. Eliminarla de la lista enlazada.
5. Recorrer y mostrar las tareas después de eliminar.
6. Intentar eliminar una tarea que no existe y mostrar mensaje."""

class NodoTareas:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False
        self.siguiente = None

nodo1 = NodoTareas("Estudiar Python")
nodo2 = NodoTareas("Hacer ejercicio")
nodo3 = NodoTareas("Leer un libro")

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

nodo2.completada = True

actual = nodo1
total_tareas = 0
print("\nLista de tares enlazadas:")
while actual:
    if actual.completada:
        print(f"✅ {actual.descripcion}")
        actual = actual.siguiente
        total_tareas += 1
    else:
        print(f"❌ {actual.descripcion}")
        actual = actual.siguiente

print(f"\nTotal tareas completadas: {total_tareas}")

nueva = NodoTareas("Practicar código")

nueva.siguiente = nodo1

nodo1 = nueva
actual = nodo1
total_tareas = 0
print("\nLista de tareas enlazadas:")
while actual:
    if actual.completada:
        print(f"✅ {actual.descripcion}")
        actual = actual.siguiente
        total_tareas += 1
    else:
        print(f"❌ {actual.descripcion}")
        actual = actual.siguiente

print(f"\nTotal tareas completadas: {total_tareas}")

# Creamos una lista de tareas con el orden de la lista enlazada

lista_tareas = []
actual = nodo1
print("\nMostramos lista de tareas desde la lista generada: ")
while actual:
    lista_tareas.append(actual.descripcion)
    actual = actual.siguiente

for i, tarea in enumerate(lista_tareas, 1):
    print(f"{i}. {tarea}")

# Buscamos tarea que se desee eliminar

eliminar = input("\nDescripción de tarea a eliminar: ").strip()

# Eliminamos del primer nodo
if nodo1.descripcion == eliminar:
    nodo1 = nodo1.siguiente
    print(f"Tarea '{eliminar}' eliminada exitosamente. Estaba en la primera posición.")
else:
    # Buscamos el nodo anterior a la tarea que se desea eliminar
    actual = nodo1
    while actual.siguiente is not None and actual.siguiente.descripcion != eliminar:
        actual = actual.siguiente
    
    if actual.siguiente is not None:
        # Eliminamos el nodo saltándolo
        actual.siguiente = actual.siguiente.siguiente
        print(f"Tarea '{eliminar}' eliminada con éxito.")
    else:
        print(f"Tarea '{eliminar}' no encontrada.")

# Mostramos lista después de eliminar
print("\nLista después de eliminar:")
actual = nodo1
total_tareas = 0
while actual:
    if actual.completada:
        print(f"✅ {actual.descripcion}")
        actual = actual.siguiente
        total_tareas += 1
    else:
        print(f"❌ {actual.descripcion}")
        actual = actual.siguiente

print(f"Total tareas completadas: {total_tareas}")