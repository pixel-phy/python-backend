"""El historial de errores:

Imagina que nuestro servidor detectó un fallo. Escribe un Script que abra (o cree) un archivo
llamado errores.log. Debes añadir dos líneas de texto diferentes sin borrar lo que ya 
puediera existir en el archivo. """

registro_errores = open("errores.log", mode="a", encoding='utf-8')

registro_errores.write("Error 500: Fallo de conexión.\nVerifique conexión y vuelva a intentarlo.\n")

registro_errores.close()

print("Archivo editado correctamente.")
