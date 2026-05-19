"""Invertir lista enlazada por bloques de prioridad
Una empresa tiene tareas organizadas en una lista enlazada. Cada tarea tiene:
- Descripción
- Prioridad (1 = alta, 2 = media, 3 = baja)

Lista inicial (orgen original):
("Informe", 1)
("Correo", 2)
("Llamada", 1)
("Backup", 3)
("Reunión", 2)

Requisitos:
1. Crear la lista enlazada con las 5 tareas en el orden original.
2. Mostrar la lista original
3. Invertir la lista por bloqueda de prioridad:
- Dentro de cada prioridad (1, 2, 3), invertir el orde de las tareas
- El orden global de prioridades se mantiene (1 - 2 - 3)
4. Mostrar la lista transformada."""

class Tarea:
    def __init__(self, datos):
        self.datos = datos
        self.siguiente = None

tarea1 = Tarea(("Informe", 1))
tarea2 = Tarea(("Correo", 2))
tarea3 = Tarea(("Llamada", 1))
tarea4 = Tarea(("Backup", 3))
tarea5 = Tarea(("Reunión", 2))

tarea1.siguiente = tarea2
tarea2.siguiente = tarea3
tarea3.siguiente = tarea4
tarea4.siguiente = tarea5
tarea5.siguiente = None

actual = tarea1
contador = 0
print("\n--- Lista original ---")
while actual is not None:
    contador += 1
    prioridad = "Alta" if actual.datos[1] == 1 else "Media" if actual.datos[1] == 2 else "Baja"
    print(f"{contador}. {actual.datos[0]} ({prioridad})")
    actual = actual.siguiente

# Listamos tareas por prioridad
alta = []
media = []
baja = []
actual = tarea1
while actual is not None:
    if actual.datos[1] == 1:
        alta.append(actual.datos)
    elif actual.datos[1] == 2:
        media.append(actual.datos)
    else:
        baja.append(actual.datos)
    actual = actual.siguiente

# Invertimos el orden de las tareas
alta.reverse()
media.reverse()
baja.reverse()

# Unimos todas las tareas
todas = alta + media + baja

# Reordenamos lista enlazada
if not todas:
    tarea1 = None
else:
    tarea1 = Tarea(todas[0])
    actual = tarea1
    for tarea in todas[1:]:
        actual.siguiente = Tarea(tarea)
        actual = actual.siguiente

print("\n--- LISTA TRANSFORMADA ---")
actual = tarea1
contador = 0
while actual is not None:
    contador += 1
    prioridad = "Alta" if actual.datos[1] == 1 else "Media" if actual.datos[1] == 2 else "Baja"
    print(f"{contador}. {actual.datos[0]} ({prioridad})")
    actual = actual.siguiente