""" Reto del día 2: El buscador de Productos con paginación

Imagina que estás construyendo el backend para una tienda online. Cuando el frontend te pide la lista de productos, no puedes mandarle
10000 productos de golpe porque tumbarías el servidor. Tienes que paginar (mostrar de 10 en 10 o de 20 en 20) y permitir filtros opcionales.

Tarea: Crear una función llamada obtener_productos:
    - 1. Debe recibir los siguientes parámetros
    - productos_db (un diccionario que simula la base de datos. Este parámetro no tiene valor por defeto, es obligatorio)
    - pagina (entero, opcional, por defecto debe ser 1)
    - por_pagina (entero, opcional, por defecto debe ser 2)
    - categoria_filtrar(opcional, una lista de strings para filtrar)
    - 2. La base de datos de prueba tiene esta estructura:
    base_datos = {
    1: {"nombre": "laptop", "categoria": "tecnologia"},
    2: {"nombre": "Teclado", "categoria": "tecnologia"},
    3: {"nombre": "Cafetera", "categoria": "hogar"}, 
    4: {"nombre": "Curso Python", "categoria": "educacion"},
    5: {"nombre": "Monitor", "categoria": "tecnologia"}
    }

    - 3. Lógica de la función:
    - Primero, si el usuario pasa categorias_filtrar debes filtrar los productos que pertenezcan a esas categorías. Si no pasa nada, usas todos los productos.
    - Segundo, debes aplicar la paginación a esos productos resultantes. 
    - Tercero, la función debe retornar una lista con los productos de esa página. """

base_datos = {
    1: {"nombre": "laptop", "categoria": "tecnologia"},
    2: {"nombre": "Teclado", "categoria": "tecnologia"},
    3: {"nombre": "Cafetera", "categoria": "hogar"}, 
    4: {"nombre": "Curso Python", "categoria": "educacion"},
    5: {"nombre": "Monitor", "categoria": "tecnologia"}
    }

def obtener_productos(productos_db:dict, pagina:int=1, por_pagina:int=2, categoria_filtrar=None):
    if categoria_filtrar is None:
        categoria_filtrar = []

    # Filtrar
    productos_filtrados = []
    for id_producto, info in productos_db.items():
        if len(categoria_filtrar) == 0 or info["categoria"] in categoria_filtrar:
            productos_filtrados.append(info)

    # Paginar
    inicio = (pagina - 1) * por_pagina
    fin = inicio + por_pagina

    return productos_filtrados[inicio:fin]

# Prueba sin filtros y por defecto
print(f"Página 1: {obtener_productos(base_datos)}")

# Prueba 2: pedimos la página 2
print(f"Página 2: {obtener_productos(base_datos, pagina=2)}")

# Prueba 3: Filtramos solo por "tecnología" y pedimos la página 1
print(f"Solo tecnología (pág 1) {obtener_productos(base_datos, pagina=1, categoria_filtrar=["tecnologia"])}")
