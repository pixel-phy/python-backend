"""Un sistema escolar mantiene una lista de estudiantes. Cada estudiante tiene:
- Nombre
- Nota promedio (0 a 100)
1. Crear una lista enlazada con los 5 estudiantes en el orden dado.
2. Mostrar la lista original
3. Ordenar lal ista por los estudiantes cretios:
- primerio por promedio.
- luego por nombre.
4. Mostrar la lista ordenada."""

class Estudiante:
    def __init__(self, datos):
        self.datos = datos  # (nombre, promedio)
        self.siguiente = None

# Crear lista original
e1 = Estudiante(("Ana", 85))
e2 = Estudiante(("Luis", 92))
e3 = Estudiante(("Carlos", 78))
e4 = Estudiante(("Sofia", 92))
e5 = Estudiante(("Juan", 85))

e1.siguiente = e2
e2.siguiente = e3
e3.siguiente = e4
e4.siguiente = e5

inicio = e1

# Mostrar lista original
print("--- LISTA ORIGINAL ---")
actual = inicio
contador = 1
while actual:
    nombre, promedio = actual.datos
    print(f"{contador}. {nombre} - {promedio}")
    actual = actual.siguiente
    contador += 1

# Algoritmo de inserción ordenada (por promedio DESC, luego nombre ASC)
inicio_ordenado = None
actual = inicio

while actual:
    nombre, promedio = actual.datos
    nuevo = Estudiante((nombre, promedio))
    
    # Insertar al inicio
    if inicio_ordenado is None:
        nuevo.siguiente = inicio_ordenado
        inicio_ordenado = nuevo
    else:
        # Comparar con el primer nodo
        nom0, prom0 = inicio_ordenado.datos
        
        # Si debe ir antes que el primero
        if promedio > prom0 or (promedio == prom0 and nombre < nom0):
            nuevo.siguiente = inicio_ordenado
            inicio_ordenado = nuevo
        else:
            # Buscar posición correcta
            actual_ordenado = inicio_ordenado
            while actual_ordenado.siguiente is not None:
                nom_sig, prom_sig = actual_ordenado.siguiente.datos
                if promedio > prom_sig or (promedio == prom_sig and nombre < nom_sig):
                    break
                actual_ordenado = actual_ordenado.siguiente
            
            nuevo.siguiente = actual_ordenado.siguiente
            actual_ordenado.siguiente = nuevo
    
    actual = actual.siguiente

inicio = inicio_ordenado

# Mostrar lista ordenada
print("\n--- LISTA ORDENADA (por promedio DESC, luego nombre ASC) ---")
actual = inicio
contador = 1
while actual:
    nombre, promedio = actual.datos
    print(f"{contador}. {nombre} - {promedio}")
    actual = actual.siguiente
    contador += 1