"""El ordenador de productos por precio (Uso avanzado)
Imagina que desde tu base de datos traes la siguiente lista de diccionarios (productos):

    productos = [
    {"nombre": "Teclado", "precio": 150},
    {"nombre": "Mouse", "precio": 80},
    {"nombre": "Monitor", "precio": 500}
    ]

Python utiliza la función nativa sorted() para ordenar listas. Si se hace sorted(productos), 
Python se rompe porque no sabe si quieres ordenar por nombre o por precio.
Para solucionarlo, sorted recibe un argumento llamada key donde le pasas
una función lambda que le dice exactamente qué campo mirar.

    - Requerimiento: Utilizar la función sorted() junto con una función lambda para ordenar 
    la lista productos de menor a mayor precio. """

productos = [
    {"nombre": "Teclado", "precio": 150},
    {"nombre": "Mouse", "precio": 80},
    {"nombre": "Monitor", "precio": 500}
]

productos_ordenados = sorted(productos, key=lambda x : x['precio'])
print(productos_ordenados)
