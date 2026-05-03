"""Usando la variable texto = "Python Backend", extraer mediante slicing:
1. La palabra Python (primeros 6 caracteres).
2. La palabra Backend (desde la 7ma posición hasta el final).
3. El texto completo (todo).
4. El texto completo pero invertido."""
print("\n--- SLICING STRINGS ---\n")
# Declaramos variable
texto = "Python Backend"
python = texto[0:6]
backend = texto[7:]
completo = texto[:]
completo_invertido = texto[::-1]

print("\n--- RESULTADOS ---\n")
print(f"Python: {python}")
print(f"Backend: {backend}")
print(f"El texto completo: {completo}")
print(f"Completo invertido: {completo_invertido}")