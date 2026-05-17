"""Gestor de lista de contactos
Una agenda telefónica simple usando lista enlazada. Cada contacto tiene:
- Nombre
- Teléfono
Hacer secuencialmente:
1. Crear la lista enlazada con los 3 contactos iniciales.
2. Mostrar todos los contactos.
3. Buscar un contacto por nombre y mostrar su teléfono.
4. Modificar el teléfono de "Luis" a "999999999".
5. Eliminar el contacto "Carlos" de la lista.
6. Agregar un nuevo contacto "Sofía" con teléfono "777777777" al final de la lista.
7. Mostrar nuevamente todos los contactos para verificar los cambios. """

class AgendaTelefonica:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.siguiente = None

contacto1 = AgendaTelefonica("Ana", 123456789)
contacto2 = AgendaTelefonica("Luis", 987654321)
contacto3 = AgendaTelefonica("Carlos", 555555555)

contacto1.siguiente = contacto2
contacto2.siguiente = contacto3
# Mostramos contactos
actual = contacto1
print("\n---CONTACTOS INICIALES ---")
while actual:
    print(f"{actual.nombre} - {actual.telefono}")
    actual = actual.siguiente

# Buscamos contacto
buscar = input("\nNombre a buscar: ").strip().capitalize()

actual = contacto1
nombre_encontrado = False
while actual:
    if actual.nombre == buscar:
        nombre_encontrado = True
        nombre_buscado = actual.nombre
        telefono_buscado = actual.telefono
    actual = actual.siguiente

print(f"--- BUSCAR {nombre_buscado.upper()} ---")
if nombre_encontrado:
    print(f"Teléfono de {nombre_buscado.capitalize()} - {telefono_buscado}")

else:
    print(f"Nombre '{nombre_buscado.capitalize()}' no encontrado")

# Modificamos el teléfono del contacto buscado
actual = contacto1
while actual:
    if nombre_encontrado:
        if actual.nombre == buscar:
            try: 
                nuevo_telefono = int(input("Teléfono nuevo: "))
                actual.telefono = nuevo_telefono
                print(f"Teléfono de {nombre_buscado} modificado {nuevo_telefono} ✅")
                break
            except ValueError:
                print("Número ingresado inválido")
                exit()
        actual = actual.siguiente

# Eliminamos el contacto 'Carlos' de la lista
eliminar = "Carlos"
print(f"\n--- ELIMINAR A {eliminar.upper()} ---")
if contacto1.nombre == eliminar:
    contacto1 = contacto1.siguiente
    print(f"'{eliminar}' fue eliminado correctamente.")
else:
    # Buscamos el nodo anterior al contacto carlos
    actual = contacto1
    while actual.siguiente is not None and actual.siguiente.nombre != eliminar:
        actual = actual.siguiente
    
    if actual.siguiente is not None:
        # Se elimina el nodo saltándolo
        actual.siguiente = actual.siguiente.siguiente
        print(f"'{eliminar}' eliminado correctamente")
    else:
        print(f"No se encontró a {eliminar} en los contactos")

# Agregamos a Sofía
print("\n --- AGREGAR A SOFIA ---")
contacto_nuevo = AgendaTelefonica("Sofia", 777777777)
ultimo = contacto1
while ultimo.siguiente is not None:
    ultimo = ultimo.siguiente
ultimo.siguiente = contacto_nuevo

print("✅ Contacto Sofía agregado al final")

print("\n--- CONTACTOS FINALES ---")
actual = contacto1
while actual:
    print(f"{actual.nombre} - {actual.telefono}")
    actual = actual.siguiente