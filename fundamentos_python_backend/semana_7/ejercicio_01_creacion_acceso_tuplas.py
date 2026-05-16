"""Tuplas - Creación y acceso
1. Crear una tupla con los días de la semana.
2. Muestra el primer y último día.
3. Muestra los días hábiles. 
4. Muestra los días del fin de semana. 
5. Muestra todos los días en orden inverso. 
6. Intentar: dias[0] = "Domingo" """

dias = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")

print(f"Primer día: {dias[0]} | Último día: {dias[-1]}")
dias_habiles = dias[:5]
print(f"Días hábiles: {dias_habiles}")
dias_fin_semana = dias[-2:]
print(f"Días fin de semana: {dias_fin_semana}")
orden_inverso = dias[::-1]
print(f"Orden inverso: {orden_inverso}")
