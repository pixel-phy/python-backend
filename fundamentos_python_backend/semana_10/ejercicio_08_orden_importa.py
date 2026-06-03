"""Parámetros posicionales
El orden importa: """

def conectar_bd(host, puerto, usuario):
    return f"Conectando a {host}: {puerto} como {usuario}"

# Los argumentos van en el mismo orden
conectar_bd("localhost", 5432, "admin") # Correcto
conectar_bd(5432, "localhost", "admin") # Incorrecto

""" Argumentos nombrados (keywords) 
Se especifica qué parámetro recibe cada valor"""

# Mismo resultados, pero más claro
conectar_bd(usuario="admin", host="localhost", puerto=5432)

# Ventaja: El orden ya no importa
# Muy usado en Backend: Configuraciones opcionales

# Valores por defecto (default parameters)
def conectar_bd(host="localhost", puerto=5432, usuario="root"):
    return f"Conectando a {host}: {puerto} como {usuario}"

# Se puede llamar de múltiples maneras
conectar_bd() # Usa todos los defaults
conectar_bd("192.168.1.1") # Solo cambia host
conectar_bd(puerto=3306) # Solo cambia el puerto (nombrado)
conectar_bd("10.0.0.1", 27017, "mongo") # Todos posicionales

# Relación con Backend (muy importante)
# Escenario real: Conexión a base de datos

def obtener_conexion_bd(host="localhost", puerto=5432, bd="mi_app", timeout=30):
    """ En producción, estos valores vienen de variables de entorno.
    En desarrollo, usas los defaults. """

    print(f"Conectando a PostgreSQL en {host}:{puerto}/{bd} (timeout = {timeout}s)")
    # Simular conexión exitosa
    return {"Conectada": True, "host": host}

# Formas de uso típicas
obtener_conexion_bd() #Desarrollo local
obtener_conexion_bd(host="prod.db.com") # Solo cambiar host
obtener_conexion_bd("prod.db.com", 5432, "produccion") # Todos específicos
obtener_conexion_bd(timeout=60, bd="testing") # Args nombrados

""" Escenario real: Endpoint de API paginado"""

def listar_usuarios(limite=10, offset=0, orden="id", ascendente=True):
    """Simula un endpoint GET /usuarios con parámetros opcionales."""
    print(f"Consultando usuarios: limite={limite}, offset={offset}, orden={orden}")
    # Simular resultados paginados
    return [f"Usuario {i}" for i in range(offset, offset + limite)]

# Diferentes llamados desde el cliente
listar_usuarios() # Primeros 10 usuarios
listar_usuarios(20) # Primeros 20 usuarios
listar_usuarios(limite=5, offset=10) # Página 3 (11-15)
listar_usuarios(orden="nombre", ascendente=False) # Orden descendente por nombre
