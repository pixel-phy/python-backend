"""
Crear una función es_mayor_de_edad(edad) que retorne True si edad >= 18, False en caso contrario
"""
def es_mayor_de_edad(edad):
    return edad >= 18

try:
    edad = int(input("Edad: "))
    if edad <= 0:
        print("Ingrese una edad válida")
    else:
       resultado = es_mayor_de_edad(edad)
       print(resultado)
except ValueError as e:
    print(f"Error: {e}")

""" Aplicación Backend real
En una API, normalmente no se utiliza input(). En su lugar, la edad llegaría como parte de una solicitud HTTP: """

# Simulando un endpoint de API
def verificar_mayoria_de_edad(datos_usuario):
    """ Función que se llamaría desde un endpoint POST /verificar-edad """
    edad = datos_usuario.get("edad")

    if not edad:
        return {"error": "Edad no proporcionadad", "status": 400}
    if edad <= 0:
        return {"error": "Edad inválida", "status": 400}
    return {
            "es_mayor": edad >= 18,
            "status": 200
            }

# Simular llamada
print(verificar_mayoria_de_edad({"edad": 20}))
print(verificar_mayoria_de_edad({"edad": 14}))

