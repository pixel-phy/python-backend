"""Ejercicio 2: El procesador de filtros de búsqueda (kwargs):
    En las tiendas online, los usuarios pueden buscar productos filtrando por lo que quieran: unos buscan por precio_max, 
    otros por marca, otros por talla, o todos a la vez.
    - Requerimiento: Crea una función llamda construir_query_busqueda que reciba un parámetro obligatorio
    llamado categoria_principal (str). Además, debe recibir cualquier filtro extra usando kwargs.
    - Lógica: La función debe revisar si dentro de los filtros dinámicos viene la llave "precio_max".
    Si viene, debe imprimir: "Alerta: Filtrando por presupuesto limitado". Al final, la función debe retornar 
    el diccionario completo de kwargs.
    - Prueba esperada:
    print(construir_query_busqueda("tecnologia", marca="Sony", precio_max=500)) """

def construir_query_busqueda(categoria_principal: str, **kwargs):
    if "precio_max" in kwargs:
        print("Alerta: Filtrando por presupuesto limitado")
    return kwargs

print(construir_query_busqueda("tecnologia", marca="Sony", precio_max=500))
