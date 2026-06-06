"""El bug del carrito acumulador
La idea es que cuando un usuario añade productos a su carrito, se cree un carrito nuevo si no tiene uno, o se añadan a su lista existente.
El problema es que en producción los usuarios están reportando que ven los productos de otros clientes en sus carritos.  """

"""
# Código con bug

def agregar_al_carrito(producto:str, carrito_actual=[]):
    carrito_actual.append(producto)
    return f"Productos en tu carrito: {carrito_actual}"

"""

# Solución
def agregar_al_carrito(producto: str, carrito_actual: list=None):
    
    if carrito_actual is None:
        carrito_actual = []

    carrito_actual.append(producto)
    return carrito_actual

carrito_usuario = None

carrito_usuario = agregar_al_carrito("Camisa", carrito_usuario)
print("Paso 1:", carrito_usuario)

carrito_usuario = agregar_al_carrito("Zapatos", carrito_usuario)
print("Paso 2:", carrito_usuario)
