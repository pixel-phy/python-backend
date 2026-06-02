"""Crear una función
Crear una función saludar_usuario(nombre) que reciba un nombre y retorne "Bienvenido al sistema, 'nombre' """

def saludar_usuario(nombre):
    return f"Bienvenido al sistema, {nombre}"

mensaje = saludar_usuario("Miguel")
print(mensaje)

