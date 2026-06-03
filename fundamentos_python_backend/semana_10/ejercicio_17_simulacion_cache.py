""" Simulación Caché
Crear una función crear_cache() que retorne dos funciones: guardar(clave, valor) y obtener(clave). El caché
debe ser una variable local de crear_cache(). """

def crear_cache():
    memoria_cache = {}

    def guardar(clave, valor):
        memoria_cache[clave] = valor
        print(f"Guardado: '{clave}' con el valor '{valor}'")

    def obtener(clave):
        # El método .get() evita que el programa falle si la clave no existe
        return memoria_cache.get(clave, "Clave no encontrada")

    return guardar, obtener

mi_guardar, mi_obtener = crear_cache()

mi_guardar("usuario_1", "Ana Gómez")
mi_guardar("token_sesion", "ABC123XYZ")

print(mi_obtener("usuario_1"))
print(mi_obtener("token_sesion"))

print(mi_obtener("edad"))
