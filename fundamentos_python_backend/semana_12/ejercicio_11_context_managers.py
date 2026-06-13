"""Context Managers: El bloque with open()
    El problema de utilizar archivo.close() al final de código es que si ocurre un error a mitad 
    del código, el script se detiene y el archivo se queda abierto en la memoria RAM, bloqueando 
    recursos del servidor. 

    Para solucionar esto de forma automatizada, Python utiliza Context Managers a través de la palabra
    with. """

with open("datos.txt", mode="r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    # Hacemos lo que queramos hacer... 

# Al salir de la identación del bloque with.
# Python cierra el archivo automáticamente. Incluso si el código falla por dentro. 

