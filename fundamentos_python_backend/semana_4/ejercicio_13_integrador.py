"""Ejercicio integrador:
Dadas las listas: 
nombres = ["Ana", "Luis", "Maria", "Carlos"]
notas = [85, 92, 78, 88]
1. Mostrar lista enumerada "1. Nombre --> nota
2. Calcular promedio del curso.
3. Mostrar estudiante con nota más alta."""
nombres = ["Ana", "Luis", "María", "Carlos"]
notas = [85, 92, 78, 88]

# Mostrar la lista enumerada:
for i in range(len(nombres)):
    print(f"{i+1}. {nombres[i]} --> {notas[i]} puntos")

# Promedio del curso:
suma = 0
nota_alta = -1
estudiante = ""

for i in range(len(nombres)):
    suma += notas[i]
    if notas[i] > nota_alta:
        nota_alta = notas[i]
        estudiante = nombres[i]

promedio = suma/ len(notas)

print(f"\n--- RESULTADOS ---\n")
print(f"Promedio del curso: {promedio:.2f}")
print(f"Estudiante con nota más alta: {estudiante} con {nota_alta} puntos.")