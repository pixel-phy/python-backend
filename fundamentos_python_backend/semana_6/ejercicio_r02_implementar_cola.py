"""Implementar cola desde cero"""

from collections import deque

cola = deque()
cola.append(10)
cola.append(20)
cola.append(30)
print(cola.popleft())
print(cola.popleft())
print(cola.popleft())