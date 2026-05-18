"""Tuplas anidadas y desempaquetado
Una empresa tiene empleados. Cada empleado tiene: nombre, edad y un tuple con direcciones (calle, ciudad, código_postal)

empleados = [
    ("Ana", 28, ("Calle 123", "Madrid", 28001)),
    ("Luis", 35, ("Avenida 456", "Barcelona", 08001)),
    ("Carlos", 42, ("Plaza 789", "Valencia", 46001))
]

Requisitos: 
1. Recorrer la lista de empleados y mostrar cada uno con formato:
Empleado - edad años
  Dirección: Calle..., Ciudad, código postal
2. Buscar un empleado por nombre y mostrar toda su información.
3. Cambiar la ciudad del empleado "Luis" a "Barcelona" (¿es Posible?) ¿Por qué?
4. Agregar un nuevo empleado a la lista: ("Sofia", 31, ("Calle 456", "Sevilla", 41001))
5. Mostrar la lista actualizada."""

empleados = [
    ("Ana", 28, ("Calle 123", "Madrid", 28001)),
    ("Luis", 35, ("Avenida 456", "Barcelona", 8001)),
    ("Carlos", 42, ("Plaza 789", "Valencia", 46001))
]

# Recorremos la lista y mostramos información
print("\n --- EMPLEADOS ---")
for empleado in empleados:
    print(f"{empleado[0]} - {empleado[1]} años\n"
          f"  Dirección: {empleado[2][0]}, {empleado[2][1]}, {empleado[2][2]}")

print("\n--- BUSCAR ---")
buscar = input("Buscar nombre: ").strip().capitalize()
for empleado in empleados:
    if buscar == empleado[0]:
        print(f"{empleado[0]} - {empleado[1]} años\n"
              f"  Dirección: {empleado[2][0]}, {empleado[2][1]}, {empleado[2][2]}")
        break
else:
    print(f"No fue posible encontrar al empleado '{buscar}'")

# Intentamos modificar dirección
print("\nModificando información...")
try:
    empleado1, empleado2, empleado3 = empleados
    empleado2[2][1] = "Madrid"
except (ValueError, TypeError):
    print("\nNo es posible modificar la información en una tupla")

nuevo_empleado = ("Sofia", 31, ("Calle 456", "Sevilla", 41001))
empleados.append(nuevo_empleado)

print("\n --- ACTUALIZADA ---")
for nombre, edad, (calle, ciudad, cp) in empleados:
    print(f"{nombre} - {edad} años")
    print(f"  Dirección: {calle}, {ciudad}, {cp}")