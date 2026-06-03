"""Configuración de Servidor
Crear una función configurar_servidor(host, puerto=8080, ssl=False, timeout= 30) que retorne un diccionario con la configuración. """

def configurar_servidor(host, puerto=8080, ssl=False, timeout=30):
    return {"host": host, 
    "puerto": puerto, 
    "ssl": ssl, 
    "timeout": timeout
            }

print(configurar_servidor("localhost"))
print(configurar_servidor("api.miapp.com", puerto=443, ssl=True))
print(configurar_servidor("0.0.0.0", timeout=60))
