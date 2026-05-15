"""Mezclar dos colas (intercalar)
Tienes dos colas y quieres combinarlas intercalando elementos ej: [1, 3, 5] y [2, 4, 6] : [1, 2, 3, 4, 5, 6]"""

from collections import deque

pares = [2, 4, 6]
impares = [1, 3, 5, 7, 9, 11]
cola1 = deque(pares)
cola2 = deque(impares)
mezcla = []

while cola1 and cola2:
    mezcla.append(cola2.popleft())
    mezcla.append(cola1.popleft())

if not cola1:
    while cola2:
        mezcla.append(cola2.popleft())

if not cola2:
    while cola1:
        mezcla.append(cola1.popleft())

print(f"Mezcla: {mezcla}")
