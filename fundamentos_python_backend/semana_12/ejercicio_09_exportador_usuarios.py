"""El exportador de usuarios:
    Tienes la siguiente lista de nombres obtenidos de una base de datos ficticia:

    usuarios = ["Carlos", "Ana", "Sofía", "Mauricio"]

    Escribe un script que cree un archivo llamado usuarios.txt usando writelines(). Tu misión es asegurarte
    de que en el archivo final cada usuario quede en su propia lína (uno debajo del otro). """

archivo_usuarios = open("usuarios.txt", mode="w", encoding="utf-8")

usuarios = ["Carlos", "Ana", "Sofía", "Mauricio"]

# Añadimos los saltos de línea dinámicamente:
usuarios_con_salto = [f"{usuario}\n" for usuario in usuarios]

archivo_usuarios.writelines(usuarios_con_salto)

archivo_usuarios.flush()

archivo_usuarios.close()
