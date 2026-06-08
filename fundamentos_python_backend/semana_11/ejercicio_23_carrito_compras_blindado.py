"""El Carrito de compras blindado (Funciones anidadas + nonlocal)
Para evitar que hackers alteren el total a pagar desde el navegador web, el total del carrito de 
compras debe manejarse de forma 100% segura dentro del backend usando una función anidada.
    - Crear una función externa llamada crear_carrito(). Adentro, declara una variable total_pagar = 0.0
    - Función interna: Adentro, crear una función interna llamada agregar_producto(precio: float).
        - Debe usar nonlocal para poder modificar el total_pagar.
        - Debe sumar el precio al total_pagar y retornar el nuevo total acumulado.
- Lógica final externa: Debe retornar la función interna agregar_producto (sin ejecutar, como una fábrica). """

def crear_carrito():
    total_pagar = 0.0
    def agregar_producto(precio: float):
        nonlocal total_pagar
        total_pagar += precio
        return total_pagar
    return agregar_producto

mi_carrito = crear_carrito()
print(mi_carrito(50.0))
print(mi_carrito(150.0))

