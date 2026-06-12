"""El buscador de palabras Clave
Crea un Script que lea un archivo de texto línea por línea. Si la línea contiene la palabra 
"Error", debe imprimirla en la consola. Si no la contiene, debe ignorarla. """
#Abrimos el archivo 
archivo_log = open("datos.txt", mode="r", encoding="utf-8")

# Revisamos archivo 
for linea in archivo_log.lower():
    if "error" in linea:
        print(linea.strip())

# Cerramos archivo
archivo_log.close()
