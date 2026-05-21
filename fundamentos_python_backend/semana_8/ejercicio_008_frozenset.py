"""Frozenset (Conjutno inmutable)
A veces se necesita un conjutno que no se pueda modificar (por ejemplo, para usarlo como clave de diccionario)"""

# Set normal (mutable)
normal = {1, 2, 3}
normal.add(4)
print(normal)

# Frozenset (inmutable)
inmutable = frozenset([1, 2, 3])
# inmutable.add(4) - (muestra error)
print(inmutable)

# Se utiliza como clave de diccionario:
diccionario = {
    frozenset([1, 2]): "A",
    frozenset([3, 4]): "B"
}
print(diccionario[frozenset([1, 2])])

# También para conjuntos de conjuntos (los sets normales no pueden contener otros sets)
conjunto_de_conjuntos = {frozenset([1, 2]), frozenset([3, 4])}
print(conjunto_de_conjuntos)
