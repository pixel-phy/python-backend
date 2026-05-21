"""Primer acercamiento a los SETS """
# Se pueden definir con llaves:
frutas = {"manzana", "pera", "uva", "manzana"} # El duplicado se elimina
print(frutas)

# O con set() a partir de una lista
numeros = set([1, 2, 2, 3, 3, 4, 5, 6, 6])
print(numeros)

# Vacío no se usa {}
vacio = set()
print(type(vacio))

# Métodos básicos
# Agregar elementos
frutas.add("durazno")
print(frutas)

# Eliminar elementos
frutas.remove("manzana") # Si no existe da error
print(frutas)
frutas.discard("naranja") # Si no existe no da error

# Verificar existencia
if "pera" in frutas:
    print("Hay pera en lista")
else:
    print("No hay pera en lista")

# Longitud
print(len(frutas))

# Recorrer (orden no garantizado)
for fruta in frutas:
    print(fruta)