"""Matriz de temperaturas
Registro de temperaturas en 4 ciudades durante 5 días.
1. Mostrar la matriz.
2. Posición de cada temperatura.
3. Suma total de temperaturas.
4. Promedio de temperatura por ciudad.
5. Promedio de temperatura por día.
6. Temperatura máxima y en qué ciudad/día."""

temperaturas = [
    [22, 24, 23, 25, 24],
    [28, 19, 20, 21, 20],
    [30, 31, 29, 32, 31],
    [25, 16, 14, 15, 16]
]

# Mostrar la matriz
print("\nMatriz:")
for i in range(len(temperaturas)):
    print(temperaturas[i])

# Posición de cada temperatura registrada
print("\nPosiciones temperaturas registradas:")
for i in range(len(temperaturas)):
    for j in range(len(temperaturas[i])):
        print(f"fila {i+1}, columna {j+1}: temp {temperaturas[i][j]}°C")

# Suma total
suma_total = 0 
for i in range(len(temperaturas)):
    for j in range(len(temperaturas[i])):
        suma_total += temperaturas[i][j]
print(f"\nLas temperaturas suman: {suma_total}°C")

# Promedio de temperaturas por ciudad
print("\nPromedio de temperaturas por ciudad:\n")
ciudades = len(temperaturas)
dias = len(temperaturas[0])
acumulador = [0] * ciudades
for i in range(len(temperaturas)):
    suma_temp_ciudades = 0
    for j in range(len(temperaturas[i])):
        suma_temp_ciudades += temperaturas[i][j]
        promedio_temp = suma_temp_ciudades / dias
    print(f"Promedio de temperaturas ciudad {i+1}: {promedio_temp:.2f}°C")

# Promedio de temperaturas por día
print("\nPromedio de temperaturas por día:\n")

for i in range(ciudades):
    for j in range(ciudades):
        acumulador[j] += temperaturas[i][j]
for j in range(ciudades):
    promedio = acumulador[j]/ciudades
    print(f"Promedio de ciudad {j+1}: {promedio:.2f}°C")

# Temperatura máxima registrada
max_temp = temperaturas[0][0]
max_ciudad = 0
max_dia = 0
for i in range(len(temperaturas)):
    for j in range(len(temperaturas[i])):
        if temperaturas[i][j] > max_temp:
            max_temp = temperaturas[i][j]
            max_ciudad = i
            max_dia = j
print(f"\nLa temperatura máxima registrada fue {max_temp}°C en la ciudad {max_ciudad+1} el día {max_dia+1}")