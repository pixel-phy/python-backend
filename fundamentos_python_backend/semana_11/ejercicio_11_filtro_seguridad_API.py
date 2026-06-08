"""El filtro de seguridad de API 
Cuando un frontend solicita un listado de usuarios a nuestro Backend, por seguridad nunca
debemos enviar usuarios que hayan sido suspendidos o estén inactivos. 
    Imagina que se recibe esta lista de tu base de datos:

    usuarios = [
    {"username": "miguel01", "activo": True},
    {"username": "ana77", "activo": False},
    {"username": "carlos99", "activo": True}
]

    Requerimiento: Utiliza la función nativa filter() junto con una función lambda para crear
    una nueva lista llamada usuarios_activos que contenga únicamente los diccionarios de los 
    usuarios donde "activo" sea True. """

usuarios = [
    {"username": "migue01", "activo": True},
    {"username": "ana77", "activo": False},
    {"username": "carlos99", "activo": True}
]
usuarios_activos = list(filter(lambda x : x["activo"] == True, usuarios))

print(usuarios_activos)
