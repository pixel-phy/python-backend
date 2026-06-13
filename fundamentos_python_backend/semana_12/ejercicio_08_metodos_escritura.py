""""Escritura y persistencia de datos
Cómo Python escribe datos en el disco duro y en un concepto de bajo nivel: el búfer de escritura.

    Métodos de escritura:
    1.  archivo.write(string)
    Toma un único string y lo escribe en el archivo.
    2. archivo.writelinie(lista_de_strings)
    Toma un iterable (como una lista de strings) y los escribe todos seguidos en el archivo.

    Búfer y el método flush()
    Cuando se ejecuta archivo.write(), python guarda el texto en una memoria interna muy rápida
    llamada Búfer.
    Cuando el Búfer se llena, o cuando finalmente llamas a archivo.close(), todo ese bloque de texto acumulado
    se "vuelca" (persiste) en el disco duro de un solo golpe.

    archivo.flush()
    Es un método que le dice a Python: "No te esperes a que el búfer se llene ni a que cierre el archivo, escribe
    lo que tienes en memoria en el disco duro ahora mismo!".
    ¿Por qué es importante?
    Si se está escribien algún archivo y hay un apagón repentinoo el proceso se cae antes de llamar a .close(), 
    todo lo que estaba atrapado en el búfer de memoria se perderá. Usar flush() intermitentemente asegura
    que los datos críticos se guarden en el disco duro real de inmediato. """

# Ejemplo:

archivo_salida = open("reporte_ventas.txt", mode="w", encoding="utf-8")

# Usando writelines
lineas_reporte = [
    "--- REPORTE DE VENTAS ---\n",
    "Producto A: $150 USD\n",
    "Producto B: $220 USD\n"
]
archivo_salida.writelines(lineas_reporte)

# Forzamos la escritura al disco inmediatamente sin cerrar el archivo todavía
archivo_salida.flush()

# El archivo sigue abierto, podemos seguir operando en el backend...
archivo_salida.write("Total Ventas: $370 USD\n")

# Cerramos finalmente
archivo_salida.close()
