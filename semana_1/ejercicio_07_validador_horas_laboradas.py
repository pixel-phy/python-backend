"""Estás desarrollando un sistema de cálculo de horas extras para una empresa. El programa debe validar el horario de entrada 
y salida del empleado, calcular si hizo horas extras y determinar el pago según las reglas de la empresa.

Reglas de la empresa
Jornada normal: 9:00 a 18:00 (9 a 18)

Situación	                                             Regla
Entrada después de las 9:00	             Se descuenta como "minutos tarde"
Salida antes de las 18:00	                "Jornada reducida" (sin penalización, solo aviso)
Salida después de las 18:00	                Horas extras (se pagan según tarifa especial)

1. Cálculo de horas extras 
Horas extras por día	                        Multiplicador
Hasta 2 horas extras	                    1.5x (tiempo y medio)
Más de 2 horas extras	                    2x (doble)

Reglas especiales (fines de semana)
Sábado (5) y Domingo (6) → Todo el tiempo trabajado se paga como hora extra al doble (2x), sin importar el horario.

En fines de semana no aplican los conceptos "tarde" o "jornada reducida".

Validaciones:
1. Horas deben estar entre 0 y 23
2. Hora de salida debe ser mayor o igual a hora de entrada.
3. Día debe estar entre 0 (lunes) y 6 (domingo)

Requisitos del programa
Solicitar:
1. Día de la semana (0=lunes, 1=martes, 2=miércoles, 3=jueves, 4=viernes, 5=sábado, 6=domingo)
2. Hora de entrada (0-23)
3. Hora de salida (0-23)

Validar todas las entradas

Calcular:
1. Horas totales trabajadas
2. Horas extra (si aplica)
3. Pago equivalente en "horas normales"

Mostrar:
1. Horas trabajadas
2. Si es fin de semana
3. Si llegó tarde (entre semana)
4. Si salió antes (jornada reducida)

Horas extra y su desglose (si aplica)

Total equivalente en horas normales. """

print("\n=== Calculadora de horas laborales ===\n")

# Días de la semana
dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

# 1. Día
dia = input("Ingresa el día de la semana: ").strip().lower()
if dia not in dias_semana:
    print("Día no válido")
    exit()

fin_semana = dia in ["sabado", "domingo"]

# 2. Hora de entrada
try:
    entrada = int(input("Hora de entrada (0-23): ").strip())
    if entrada < 0 or entrada > 23:
        raise ValueError("La hora debe estar entre 0 y 23")
except ValueError as e:
    print(f" Error: {e}")
    exit()

# 3. Hora de salida
try:
    salida = int(input("Hora de salida (0-23): ").strip())
    if salida < 0 or salida > 23:
        raise ValueError("La hora debe estar entre 0 y 23")
    if salida < entrada:
        raise ValueError("La salida no puede ser menor a la entrada")
except ValueError as e:
    print(f"Error: {e}")
    exit()

# 4. Horas trabajadas
horas_trabajadas = salida - entrada

# 5. Resultados
print(f"\n--- Resultados ---")
print(f"Día: {dia.capitalize()}")

if fin_semana:
    print("FIN DE SEMANA - Todo al doble")
    print(f"Horas trabajadas: {horas_trabajadas}")
    print(f"Equivalente en horas normales: {horas_trabajadas * 2}h")
else:
    print("Día laborable")
    print(f"Horario normal: 9:00 a 18:00")
    print(f"Horas trabajadas: {horas_trabajadas}")
    
    # Llegó tarde
    if entrada > 9:
        print(f"Llegó tarde: {entrada - 9} hora(s)")
    else:
        print("Llegó tarde: No")
    
    # Salió antes
    if salida < 18:
        print(f"Salió antes: {18 - salida} hora(s) antes")
    else:
        print("Salió antes: No")
    
    # Horas extra
    if salida > 18:
        extra = salida - 18
        print(f"\nHoras extra: {extra} hora(s)")
        if extra <= 2:
            equivalente = 8 + (extra * 1.5)
            print(f"  {extra}h x 1.5 = {extra * 1.5}h equivalentes")
        else:
            equivalente = 8 + 3 + ((extra - 2) * 2)
            print(f"  Primeras 2h: 2h x 1.5 = 3h equivalentes")
            print(f"  Resto {extra - 2}h: x 2 = {(extra - 2) * 2}h equivalentes")
        print(f"\nTotal equivalente: {equivalente}h")
    else:
        print(f"\nTotal equivalente: {horas_trabajadas}h")