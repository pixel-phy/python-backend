"""Eliminar elementos en un diccionario
Tres formas de eliminar en Backend (cada uno con su uso específico) """

pedido = {
        "id": "ORD-001",
        "producto": "laptop",
        "estado": "pendiente",
        "descuento": 10,
        "notas": "urgente"
    }
print(f"{pedido}")
# 1. pop(): elimina y devuelve el valor (útil si el valor se necesita)
descuento = pedido.pop("descuento")
print(f"Descuento aplicado: {descuento}%")
print(pedido)

# 2. del: elimina sin devolver valor (más rápido si no se necesita el valor)
del pedido["notas"]
print(pedido)

# 3. popitem(): elimina y devuelve el último par (útil para pilas)
ultimo_par = pedido.popitem()
print(f"Último elemento eliminado: {ultimo_par}")
print(pedido)
