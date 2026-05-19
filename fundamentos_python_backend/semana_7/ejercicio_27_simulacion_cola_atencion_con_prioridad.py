"""Simulación de cola de atención con prioridad (hospital)
Un hospital atiende pacientes en una sala de emergencias. Cada paciente tiene:
- Nombre
- Edad
- Nivel de urgencia (1 = Muy urgente, 2 = Urgente, 3 = Normal)
Reglas de atención:
- Primero se atienden los de urgencia 1 (más urgente)
- Luego los de urgencia 2
- Luego los de urgencia 3
- Dentro del mismo nivel de urgencia, se respeta el orden de llegada.
Lista inicial: 
("Ana", 25, 2)
("Luis", 30, 1)
("Carlos", 40, 3)
("Sofia", 22, 2)
("Juan", 35, 1)
Requisitos:
1. Crear la lista enlazada con los 5 pacientes en el orden de llegada.
2. Mostrar la lista original (con el orden de llegada)
3. Reordenar la lista por prioridad (urgencia 1 - 2 - 3), manteniendo el orden de llegada dentro de cada nivel.
4. Mostrar la lista ordenada por prioridad
5. Atender al primer paciente (eliminar de la lista)
6. Mostrar la lista después de atender."""

class Paciente:
    def __init__(self, datos):
        self.datos = datos
        self.siguiente = None

# Datos de los pacientes
paciente1 = Paciente(("Ana", 25, 2))
paciente2 = Paciente(("Luis", 30, 1))
paciente3 = Paciente(("Carlos", 40, 3))
paciente4 = Paciente(("Sofía", 22, 2))
paciente5 = Paciente(("Juan", 35, 1))

# Enlazamos
paciente1.siguiente = paciente2
paciente2.siguiente = paciente3
paciente3.siguiente = paciente4
paciente4.siguiente = paciente5
paciente5.siguiente = None

# Mostramos la lista en el orden de llegada
print("\n--- LISTA ORIGINAL ---")
actual = paciente1
contador = 0
while actual:
    contador += 1
    tipo = "Muy urgente" if actual.datos[2] == 1 else "Urgente" if actual.datos[2] == 2 else "Normal"
    print(f"{contador}. {actual.datos[0]} - {actual.datos[1]} ({tipo})")
    actual = actual.siguiente

# Separamos datos por nivel de urgencia
muy_urgentes = []
urgentes = []
normal = []
actual = paciente1
while actual:
    if actual.datos[2] == 1:
        muy_urgentes.append(actual.datos)
    elif actual.datos[2] == 2:
        urgentes.append(actual.datos)
    else:
        normal.append(actual.datos)
    actual = actual.siguiente

# Reconstruimos la lista respetando prioridad de urgencia
todas = muy_urgentes + urgentes + normal

if not todas:
    paciente1 = None
else:
    paciente1 = Paciente(todas[0])
    actual = paciente1
    for paciente in todas[1:]:
        actual.siguiente = Paciente(paciente)
        actual = actual.siguiente

print("\n--- LISTA ORDENADA CON PRIORIDAD ---")
actual = paciente1
contador = 0
while actual:
    contador += 1
    tipo = "Muy urgente" if actual.datos[2] == 1 else "Urgente" if actual.datos[2] == 2 else "Normal"
    print(f"{contador}. {actual.datos[0]} - {actual.datos[1]} ({tipo})")
    actual = actual.siguiente

# Atender primer paciente
print("\n--- ATENDIENDO PRIMER PACIENTE ---")
if paciente1:
    atendido = paciente1
    paciente1 = paciente1.siguiente
    tipo = "Muy urgente" if atendido.datos[2] == 1 else "Urgente" if atendido.datos[2] == 2 else "Normal"
    print(f"✅ Atendido: {atendido.datos[0]} - ({tipo})")

# Mostramos la lista después de atender
print("\n--- PACIENTES EN COLA ---")
actual = paciente1
contador = 0
while actual:
    contador += 1
    tipo = "Muy urgente" if actual.datos[2] == 1 else "Urgente" if actual.datos[2] == 2 else "Normal"
    print(f"{contador}. {actual.datos[0]} - {actual.datos[1]} ({tipo})")
    actual = actual.siguiente