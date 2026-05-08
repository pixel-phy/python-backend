"""enumerate():
Cuando se recorre una lista con for, a veces se necesita saber en qué posición estamos. enumerate() nos dá el índice automátciamente.
Dada la lista tareas = ["estudiar python", "hacer ejercicio", "leer"]
1. Usa enumerate() para mostrar cada tarea con su número empezando desde 1.
2. Mostrar el formato "1. estudiar Python"."""

tareas = ["estudiar python", "hacer ejercicio", "leer"]

for i, tarea in enumerate(tareas, start = 1):
    print(f"{i}. {tarea}")