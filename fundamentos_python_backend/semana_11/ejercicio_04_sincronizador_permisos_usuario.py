"""El sincronizador de permisos de usuario:
Estás diseñando el sistema de seguridad de una plataforma. Cuando un administrador edita un rol,
puede asignarle múltiples permisos de golpe (ej: "leer", "escribir", "borrar").
  - Requerimientos: Crea una función verificar_superusuario. Debe recibir el nombre
    del rol obligatorio (rol:str). Luego, recibirá un listado variable de permisos.
  - Lógica: Si el rol es "admin" Y entre los permisos viene "root", la función debe retornar
    True. En cualquier caso, debe retornar False.
  - Pruebas esperadas:
    print(verificar_superusuario("admin", "leer", "root"))
    print(verificar_superusuario("editor", "leer", "root")) """

def verificar_superusuario(rol: str, *args):
  if rol == "admin" and "root" in args:
    return True
  return False

print(verificar_superusuario("admin", "leer", "root"))
print(verificar_superusuario("editor", "leer", "root"))
