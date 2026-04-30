"""Sistema de calificación de estudiantes
Una escuela necesita un sistema que califique a los estudiantes según su nota y asistencia.

Reglas
Nota                            Asistencia                          Calificación final
>= 90                               >= 80 %                            "Excelente"
≥ 90	                            < 80%	                        "Buena, pero mejorable"
70-89	                            ≥ 80%	                            "Aprobado"
70-89	                            < 80%   	                        "En riesgo"
< 70	                            cualquier	                        "Reprobado"

Además: 
1. Si el estudiante tiene nota >= 90 y asistencia >= 90 %: Matrícula de honor
2. Si asistencia es <50%: Reprobado por inasistencia (Independiente de la nota)

Datos que pide:
1. Nombre del estudiante.
2. Nota (0-100)
3. Porcentaje de asistencia (0-100)

Validaciones
- Nombre no vacío
- Nota entre 0 y 100
- Si aplica mención especial

"""
print("\n--- SISTEMA DE CALIFICACIÓN DE ESTUDIANTES ---\n")

# 1. ENTRADAS Y VALIDACIONES
nombre_estudiante = input("Nombre del estudiante: ").strip()

if nombre_estudiante == "":
    print("❌ Error: El nombre no puede estar vacío")
    exit()

# Verificar solo letras (quitando espacios)
nombre_sin_espacios = nombre_estudiante.replace(" ", "")
if not nombre_sin_espacios.isalpha():
    print("❌ Error: El nombre solo debe contener letras y espacios")
    exit()

entrada_nota = input("Nota (0 - 100): ").strip()
try:
    nota = int(entrada_nota)
    if nota < 0 or nota > 100:
        raise ValueError("La nota debe estar entre 0 y 100.")
except ValueError as e:
    print(f"❌ Error: {e}")
    exit()

entrada_asistencia = input("Porcentaje de asistencia (0 - 100): ").strip()
try:
    asistencia = int(entrada_asistencia)
    if asistencia < 0 or asistencia > 100:
        raise ValueError("La asistencia debe estar entre 0 y 100.")
except ValueError as e:
    print(f"❌ Error: {e}")
    exit()

# 2. INICIALIZAR VARIABLES
calificacion = ""
mencion_especial = False

# 3. REGLAS DE NEGOCIO (versión corregida)
if asistencia < 50:
    calificacion = "Reprobado por inasistencia"
elif nota < 70:
    calificacion = "Reprobado"
elif nota >= 90 and asistencia >= 90:
    calificacion = "Excelente"
    mencion_especial = True
elif nota >= 90:
    calificacion = "Excelente"
    if asistencia < 80:
        calificacion = "Buena, pero mejorable"
elif nota >= 70 and asistencia >= 80:
    calificacion = "Aprobado"
elif nota >= 70 and asistencia < 80:
    calificacion = "En riesgo"
else:
    calificacion = "Reprobado"

# 4. MOSTRAR RESULTADOS
print("\n--- RESULTADOS ---")
print(f"Nombre: {nombre_estudiante}")
print(f"Nota: {nota}/100")
print(f"Asistencia: {asistencia}%")
print(f"Calificación: {calificacion}")

if mencion_especial:
    print("✨ Mención especial: Matrícula de honor")