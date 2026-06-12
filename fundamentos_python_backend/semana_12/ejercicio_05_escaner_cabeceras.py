"""El Escáner de cabeceras
Imagina que un sistema externo te envía un archivo gigante todos los días. Para comprobar que el archivo
no está corrupto, solo necesitamos verificar la primera línea. Escribe un script que abra un archivo 
en modo lectura y muestre en consola únicamente su primera línea."""

# Abrimos el archivo en modo lectura
archivo_log = open("datos.txt", mode="r", encoding="utf-8")
print("Iniciando lectura de la cabecera del archivo...")
# Utilizamos el método integrado para leer líneas en Python .readline()
print(archivo_log.readline())
# Cerramos el archivo
archivo_log.close()

