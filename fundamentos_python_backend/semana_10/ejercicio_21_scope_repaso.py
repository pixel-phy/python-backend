""" Ambito de variables (Scope) - Local vs Global

- Ámbito global son variables que se definen fuera de una fución. Configurar URL de base de datos, credenciales (no secretas),
configuraciones generales del servidor.

- Ámbito local son variables que se definen dentro de una función. Una vez la función retorna el resultado, se eliminan las variables 
locales de la memoria."""

# Variable global
VERSION_API = "v1.0"

def registrar_usuario(nombre):
    # Varibale local
    mensaje_bienvenida = f"Hola {nombre}"
    print(mensaje_bienvenida)
    print(VERSION_API)

registrar_usuario("Miguel")
