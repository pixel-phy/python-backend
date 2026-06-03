"""Variable global """

mensaje = "Hola"
def mi_funcion():
    print(mensaje) # Puede leer la variable global

mi_funcion()
print(mensaje)

# Es posible modificar una variable global dentro de una función

contador = 0
def incrementar():
    global contador
    contador += 1

incrementar()
print(contador)
