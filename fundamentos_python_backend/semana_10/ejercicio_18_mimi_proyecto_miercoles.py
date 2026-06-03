""" Mini proyecto del día 3

Sistema de configuración por sesión (sin globales)
Crear una función crear_configuracion() que retorne tres funciones:
    - set(clave, valor) - guardar configuración
    - get(clave) - obtiene configuración
    - reset() - limpia toda la configuración

Además debe validar que:
    - clave sea string (si no, lanzar error)
    - set no permita sobreescribir claves existentes a menos que se pase force = True """

def crear_configuracion():
    # Diccionario local y privado
    config = {}
    def set_config(clave, valor, force=False):
        # Validación de tipo de dato
        if not isinstance(clave, str):
            raise TypeError("La clave debe ser un string.")

        # Validación de sobreescritura
        if clave in config and not force:
            raise ValueError(f"La clave '{clave}' ya existe. Usa force=True para sobreescribir")

        # Si pasa validaciones, se guarda
        config[clave] = valor

    def get_config(clave):
        if not isinstance(clave, str):
            raise TypeError("La clave debe ser un string.")
        return config.get(clave, None)

    def reset_config():
        config.clear()
        print("Configuración reiniciada por completo.")

    return set_config, get_config, reset_config

asignar, obtener, reiniciar = crear_configuracion()

# Guardamos configuraciones
asignar("idioma", "español")
asignar("modo_oscuro", True)
print(obtener("idioma"))

# Intentar guardar una clave que No es string
try:
    asignar(123, "error")
except TypeError as e:
    print(f"Error esperado: {e}")

# Intentar sobreescribir una clave existente sin force=True
try:
    asignar("idioma", "inglés")
except ValueError as e:
    print(f"Error esperado: {e}")

# Sobreescribir forzadamente
asignar("idioma", "inglés", force=True)
print(obtener("idioma"))

# Reiniciar la configuración
reiniciar()
print(obtener("idioma"))




