"""Responder:
1. Estudiantes que están en matemáticas o en física.
2. Estudiantes que están en ambas materias.
3. Estudiantes que están solo en matemáticas.
4. Estudiantes que están solo en una materia."""

estudiantes_mates = {"Ana", "Luis", "Carlos", "Sofía"}
estudiantes_fisica = {"Luis", "Sofía", "Juan", "Pedro"}

union = estudiantes_mates | estudiantes_fisica
interseccion = estudiantes_mates & estudiantes_fisica
diferencia = estudiantes_mates - estudiantes_fisica
dif_simetrica = estudiantes_mates ^ estudiantes_fisica

print(f"Unión: {union}")
print(f"Intersección: {interseccion}")
print(f"Diferencia: {diferencia}")
print(f"Diferencia simétrica: {dif_simetrica}")