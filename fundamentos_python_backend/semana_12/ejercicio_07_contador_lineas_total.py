"""Contador de líneas total
Escribe un programa que lea un archivo y te diga cuántas líneas tiene en total, pero sin usar
readlines() """
# Abrimos el archivo 
archivo_log = open("datos.txt", mode="r", encoding="utf-8")

contador = 0
for linea in archivo_log:
    contador += 1

archivo_log.close()

print(f"El archivo tiene en total {contador} líneas")
