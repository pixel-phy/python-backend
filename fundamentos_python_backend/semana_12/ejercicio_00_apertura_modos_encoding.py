"""Teoría del día 1:
Para que python pueda interactuar con un archivo del disco duro, primero debe pedirle permiso al 
Sistema Operativo para abrirlo. Esto se hace mediante la función nativa open().

Al Backend le importan tres cosas fundamentales al abrir un archivo: la ruta, el modo y la codificación.

mi_archivo = open("ruta_del_archivo.txt", mode="r", encoding="utf-8")

1. Los modos de apertura (mode):
El modo le dice a Python qué pretendes hacer con el archivo. Esto es crucial en Backend para proteger la integridad de los datos.

r: read(lectura): Solo lee el archivo. Es el modo por defecto.
w: write(escritura): Sobreescribe el archivo.
a: append(Anexar): Agrega datos al final del archivo.
x: exclusive(creación): Creación exclusiva de archivos.

2. encoding='utf-8'
Por defeto, Python abre los archivos usando la codificación nativa del sistema operativo (Windows usa una, Linux otra).
Regla de oro: Simepre, siempre especificar encoding='utf-8' al abrir archivos de texto. """

# Ejemplo:

# Estamos registrando las visitas de un usuario a nuestra API.

#1. Abrimos el archivo en modo 'a' para no borrar registros anteriores
# Si el archivo 'accesos.log' no existe, python lo creará automáticamente.

log_usuarios = open("acces.log", mode="a", encoding="utf-8")
# 2. Escribimos una nueva línea
log_usuarios.write("Usuario 'admin' inició sesión - 10:45 AM\n")

# 3. Siempre cerrar el archivo. Si no se cierra, se queda consumiendo memoria RAM.
log_usuarios.close()

print("¡Registro guardado con éxito!")
