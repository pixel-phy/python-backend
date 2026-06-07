"""Argumentos dinámicos (*args, kwargs) y el Orden de Parámetros
1. *args (argumentos en forma de Tupla)
El asterisco le dice a Ppython: "Agrupa todos los argumentos posicionales extra que me envíen
y mételos en una tupla llamada args".
- Uso típico en Backend: Recibir una lista variable de etiquetas para un producto, o un listade IDs de usuarios
  que se van a eliminar en lote. """

def registrar_etiquetas(*args):
  print(args)
  for etiqueta in args:
    print(f"Guardando etiqueta: {etiqueta}")

registrar_etiquetas("python", "django", "api")

"""2. kwargs (key Arguments en forma de diccionario)
Los dos asteriscos le dicen a Python: "Agrupa todos los argumentos que vengan con nombre
y valor (llave=valor) y mételos en un diccionario llamado kwargs".
    - Uso típico en Backend: Procesar formularios dinámicos o payloads JSON variables 
    donde un usuario puede llenar unos campos y otros no (ej. Actualizar perfil)."""

def actualizar_perfil(**kwargs):
    print(kwargs)
    if "ciudad" in kwargs:
        print(f"Actualizando ciudad a: {kwargs['ciudad']}")

actualizar_perfil(ciudad="Bogotá", edad=28)

