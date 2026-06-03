""" Desafío Backend - Endpoint de búsqueda de productos
Crear una función:
    buscar_productos(termino, categoria="todos", precio_max=None, orden="nombre") que:
    1. Simule una búsqueda (solo imprime los criterios).
    2. Retorne un diccionario con los parámetros que se usaron en la búsqueda.
    3. Si precio_max es None, no aplicar filtro de precio. """

def buscar_productos(termino, categoria="todos", precio_max=None, orden="nombre"):
    return {
            "termino": termino,
            "categoria": categoria,
            "precio_max": precio_max,
            "orden": orden
                }

print(buscar_productos("laptop"))
print(buscar_productos("mouse", categoria="electronica", precio_max=50))
print(buscar_productos("monitor", orden= "precio", precio_max=300))
