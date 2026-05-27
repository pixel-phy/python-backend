#¿Qué son diccionarios anidados?
#Son diccionarios que contienen otros diccionarios como valores.

# Ejemplo:
empresa = {
        "empleado1": {"nombre": "Ana", "edad": 25, "puesto": "ingeniera"},
        "empleado2": {"nombre": "Luis", "edad": 30, "puesto": "Analista"},
        "empleado3": {"nombre": "Carlos", "edad": 28, "puesto": "Gerente"},
        }

# Acceder a valores anidados
print(empresa["empleado1"]["nombre"])
print(empresa["empleado2"]["puesto"])

# Modificar valores anidados
empresa["empleado1"]["edad"] = 26
print(empresa["empleado1"]["edad"])

# Agregar nuevo empleado
empresa["empleado4"] = {"nombre": "Sofía", "edad": 35, "puesto": "Directora"}
print(empresa["empleado4"]["nombre"])

# Recorrer diccionario anidado
print("\n=== LISTA DE EMPLEADOS ===")
for clave, empleado in empresa.items():
    print(f"{clave}: {empleado['nombre']} - {empleado['puesto']} ({empleado['edad']} años)")

""" 1. crea tu propio diccionario anidado estudiantes donde cada clave sea un número de estudiantes (1, 2, 3) y cada valor sea 
        un diccionario con "nombre", "edad", "curso".
    2. Muestra el nombre del estudiante 2.
    3. Cambia la edad del estudiante 1 a un valor diferente.
    4. Agrega un nuevo estudiante 4.
    5. Recorre el diccionario y muestra la información de cada estudiante."""

estudiantes = {
        "estudiante1": {"nombre": "Miguel", "edad": 13, "curso": "Matemáticas"},
        "estudiante2": {"nombre": "Daniela", "edad": 13, "curso": "Ciencia"},
        "estudiante3": {"nombre": "Felipe", "edad": 14, "curso": "Aviación"},
        }

print(estudiantes["estudiante2"]["nombre"])
estudiantes["estudiante1"]["edad"] = 14
estudiantes["estudiante4"] = {"nombre": "Juan Camilo", "edad": 16, "curso": "logística"}
print("\n=== LISTA DE ESTUDIANTES ===")
for clave, estudiante in estudiantes.items():
    print(f"{clave}: {estudiante['nombre']} - {estudiante['curso']} ({estudiante['edad']} años)")
    

