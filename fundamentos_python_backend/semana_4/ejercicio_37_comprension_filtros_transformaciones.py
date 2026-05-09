"""List comprehension (filtros y transformaciones)
Dada la lista numeros = [15, 22, 8, 31, 42, 13, 9, 27, 35, 18], usa list comprehension para crear:
1. mayores_20 --> números mayores a 20.
2. pares --> numeros pares.
3. cuadrados --> cuadrados de todos los números.
4. divisibles_5 --> números divisibles por 5.
5. pares_y_grandes --> números pares y mayores a 25."""

numeros = [15, 22, 8, 31, 42, 13, 9, 27, 35, 18]
mayores_20 = [n for n in numeros if n > 20]
pares = [n for n in numeros if n % 2 == 0]
cuadrados = [n ** 2 for n in numeros]
divisibles_5 = [n for n in numeros if n % 5 == 0]
pares_y_grandes = [n for n in numeros if n % 2 == 0 and n > 25]
print(f"\nnumeros: {numeros}")
print(f"mayores_20: {mayores_20}")
print(f"pares: {pares}")
print(f"cuadrados: {cuadrados}")
print(f"divisibles_5: {divisibles_5}")
print(f"pares_y_grandes: {pares_y_grandes}")