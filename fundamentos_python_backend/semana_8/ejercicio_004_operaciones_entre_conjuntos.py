"""Operaciones entre conjuntos (Unión, intersección, diferencia)
Estas operaciones son muy útiles en Backend para combinar listas de usuarios, permisos, etiquetas, etc."""

# Dos conjutos
conjunto_A = {1, 2, 3, 4}
conjunto_B = {3, 4, 5, 6}

#1. Unión: elementos A o en B (o en ambos)
union = conjunto_A | conjunto_B
print(f"Unión: {union}")

#2. Intersección: elementos en A y en B
interseccion = conjunto_A & conjunto_B
print(f"Intersección: {interseccion}")

#3. Diferencia: elementos en A pero no en B
diferencia = conjunto_A - conjunto_B
print(f"Diferencia: {diferencia}")

#4. Diferencia simétrica: elementos en A o en B, pero no en ambos
dif_simetrica = conjunto_A ^ conjunto_B
print(f"Diferencia simétrica: {dif_simetrica}")