"""Promedio de calificaciones
Un programa que pide calificaciones hasta que el usuario decida terminar. Luego muestra promedio.

Requisitos:
1. Usar While True para pedir calificaciones.
2. Validar que las calificaciones estén entre 0 y 100.
3. Preguntar después de cada calificación: ¿Otra calificación? (s/n).
4. Si la respuesta es "n", salir del bucle.
5. Calcular:
- Promedio.
- Calificación más alta.
- Calificación más baja.
- Cantidad de calificaciones ingresadas.
6. Mostrar todos los resultados al final. """
print("\n=== PROMEDIO DE CALIFICACIONES ===\n")

# Inicializamos variables
total = 0
cantidad = 0
mas_alta = -1
mas_baja = 101
contador = 1
# Bucle principal
while True:
    entrada = input(f"Calificación {contador}: ")
    try:
        nota = float(entrada)
        if nota < 0 or nota > 100:
            print("La nota debe estar entre 0 y 100")
        else:
            print(f"Nota válida: {nota}")
            total += nota
            cantidad += 1
            contador += 1
            if nota > mas_alta:
                mas_alta = nota

            if nota < mas_baja:
                mas_baja = nota
            
            # Continuar
            respuesta = input("¿Otra calificación? (s/n): ").strip().lower()
            if respuesta != 's':
                break
    except ValueError:
        print("Debes ingresar un número.")

print("\n --- RESULTADOS --- \n")
print(f"Calificaciones ingresadas: {cantidad}")
print(f"Promedio: {total / cantidad:.2f}")
print(f"Más alta: {mas_alta}")
print(f"Más baja: {mas_baja}")


        
    


  