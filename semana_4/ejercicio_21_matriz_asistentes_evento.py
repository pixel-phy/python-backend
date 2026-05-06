"""Matriz de asistentes a eventos:
Una empresa organizó 3 eventos y registró la cantidad de asistentes por día durante 4 días.
1. Mostrar la matriz como tabla.
2. Calcular total de asistentes por evento.
3. Calcular total de asistentes por día.
4. Mostrar qué evento tuvo más asistentes en total."""

# Se define la matriz
asistentes = [
    [120, 90, 110, 80],
    [95, 85, 105, 100],
    [130, 110, 95, 115]
]

# Mostramos la matriz como tabla:
print("\nAsistentes por evento y día:")
for i in range(len(asistentes)):
    print(f"Evento {i+1}: {asistentes[i]}")

# Total de asistentes por evento
print("\nTotal por evento:")
for i in range(len(asistentes)):
    total_evento = 0
    for j in range(len(asistentes[i])):
        total_evento += asistentes[i][j]
    print(f"Evento {i+1}: {total_evento} asistentes.")

# Total de asistentes por día:
print("\nTotal de asistentes por día:")
dias = len(asistentes[0])

for j in range(dias):
    total_dia = 0
    for i in range(len(asistentes)):
        total_dia += asistentes[i][j]
    print(f"Día {j+1}: {total_dia} Asistentes")

# Evento que tuvo más asistente
max_asistentes = -1
max_evento = -1
print("\n--- Evento que más asistentes tuvo ---")
for i in range(len(asistentes)):
    total_evento = 0
    for j in range(len(asistentes[i])):
        total_evento += asistentes[i][j]
    if total_evento > max_asistentes:
        max_asistentes = total_evento
        max_evento = i + 1

print(f"Evento {max_evento} con {max_asistentes} asistentes.")
