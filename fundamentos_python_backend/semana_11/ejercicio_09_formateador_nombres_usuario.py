"""El formateador de nombres de usaurio
Cuando un usuario se registra, a veces escribe su nombre con espacios extra o en minúsculas.
Queremos limpiar el string rápido.
  - Requerimiento: Crea una función lambda llamada limpiar_username. Debe recibir un string,
    quitarle los espacios en blanco de los extremos.
  - Prueba esperada: print(limpiar_username("     MigueEL01      "))"""

limpiar_username = lambda string: string.strip().lower()

print(limpiar_username("        MiguEL01        ")      )
