"""Métodos: replace() y find().
Dada la variable: frase = "El sol brilla en el cielo" 
1. Reemplazar "sol" por "luna".
2. Encontrar la posición (índice) de la palabra "brilla".
3. Encontrar la posición de la palabra "cielo".
4. Verificar si la palabra "estrellas" existe en la frase.
5. Contar cuantas veces aparece la letra "e"."""
frase = "El sol brilla en el cielo"
sol_por_luna = frase.replace("sol", "luna")
posicion_brilla = frase.find("brilla")
posicion_cielo = frase.find("cielo")
estrellas = "estrellas" in frase
letra_e = frase.count("e")

print("\n--- RESULTADOS ---\n")
print(f"Sol por luna: {sol_por_luna}")
print(f"Brilla está en el índice: {posicion_brilla}")
print(f"Cielo está en la posición: {posicion_cielo}")
print(f"Está la palabra 'estrellas': {estrellas} ")
print(f"La letra 'e' está: {letra_e} veces")