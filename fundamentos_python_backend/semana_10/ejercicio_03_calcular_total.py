""" Calcular total de carrito
Lógica de negocio """

def calcular_total(precios):
    """ Recibe lista de precios y retorna el total."""
    return sum(precios)

carrito = [15000, 23000, 8900]
total = calcular_total(carrito)
print(f"Total a pagar: ${total}")

