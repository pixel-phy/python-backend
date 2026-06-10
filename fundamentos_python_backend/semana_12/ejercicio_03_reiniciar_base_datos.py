"""El reiniciador de Base de Datos (Modo w)
Tenemos un archivo llamado temporal.txt que contiene texto viejo. Escribe un script que, al ejecutarse,
limpie por completo ese archivo y solo deje escrita la palabra [VACIADO]. """

# 1. Se crea el modo del archivo
temporal = open("temporal.txt", mode="w", encoding='utf-8')

# 2. Se sobreescribe 
temporal.write("[VACIADO]")

# 3. Cerramos el archivo (siempre)
temporal.close()

print("Archivo vaciado exitosamente.")
