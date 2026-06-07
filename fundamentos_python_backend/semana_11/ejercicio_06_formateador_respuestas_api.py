"""El formateador de Respuestas API:
A veces el frontend nos pide datos de un usuario, pero no siempre quiere los mismos campos.
Queremos una función que limpie la información y arme un perfil bonito.

  - Requerimiento: Crea una función formatear_perfil_api. Debe recibir un parámetro obligatorio
    llamado id_usuario (int). El resto de los datos del perfil vendrán en kwargs.
  - Lógica: La función debe crear un diccionario limpio. Adentro debe llevar la llave "id" con
    el valor de id_usuario. Luego, debe fusionar o meter los campos "nombre" y "pais" solo si 
    viene dentro de kwargs. Si vienen otros campos (como password o token), debe ignorarlos por 
    seguridad. Al final, retorna el diccionario limpio.

  - Prueba esperada:
    print(formatear_perfil_api(105, nombre="Miguel", pais="Colombia", password="secreto123"))"""

def formatear_perfil_api(id_usuario: int, **kwargs):
  diccionario = {}
  diccionario["id"] = id_usuario
  if "nombre" in kwargs:
    diccionario["nombre"] = kwargs["nombre"]
  if "pais" in kwargs:
    diccionario["pais"] = kwargs["pais"]
  return diccionario
print(formatear_perfil_api(105, nombre="Miguel", pais="Colombia", password="secreto123"))

