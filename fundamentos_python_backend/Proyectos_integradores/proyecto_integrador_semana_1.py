"""Proyecto integrador Semana 1
Un sistema de registro simple que solicita datos personales y los muestra formateados.
Requisitos:
1. Pedir nombre, edad, altura, peso.
2. Calcular el IMC (peso/altura²)
 IMC	            Clasificación	            Recomendación
< 18.5	            Bajo peso	         "Consulta a un nutricionista"
18.5 - 24.9	        Normal	             "Mantén tus hábitos saludables"
25 - 29.9	        Sobrepeso	          "Considera hacer ejercicio regularmente"
≥ 30	            Obesidad	         "Riesgo alto, consulta a un médico"

Reglas adicionales
1. Si la persona tiene sobrepeso Y es mayor de 50 años → mostrar "ALTO RIESGO: combina sobrepeso con edad avanzada"
2. Si la persona tiene obesidad Y es mayor de 40 años → mostrar "CRÍTICO: obesidad + edad > 40, requiere atención inmediata"
3. Si el IMC es Normal pero la persona tiene menos de 18 años → mostrar "Seguimiento pediátrico recomendado"

3. Mostrar todos los datos en un resumen bonito.
4. Validar que la edad sea un número entero positivo.
5. Validar que la altura y peso sean números positivos.
6. Calcular la edad que tendrá en 10 años."""

#Datos de entrada
print("\n=== REGISTRO DE USUARIO ===")

nombre = input("Nombre: ").strip().title()
if not nombre:
    print("El nombre no debe ir vacío.")

entrada_edad = input("Edad (años): ")
try:
    edad = int(entrada_edad)
    if edad < 0 or edad > 120:
        print("La edad debe estar entre 0 y 120 años.")
except ValueError:
    print(f"{entrada_edad} no es un número válido.")

entrada_altura = input("Altura (m): ")
try:
    altura = float(entrada_altura)
    if altura < 0 or altura > 2.30:
        print("La altura debe estar entre 0 y 2.30 metros")
except ValueError:
    print("Ingrese una altura válida.")

entrada_peso = input("Peso (kg): ")
try:
    peso = int(entrada_peso)
    if peso < 0:
        print("El peso debe ser un número positivo.")
except ValueError:
    print(f"{entrada_peso} no es un peso válido")

# Calculo de IMC
imc = peso / (altura ** 2)

if imc < 18.5:
    clasificacion = "Bajo peso"
    recomendacion = "Consulta a un nutricionista"

elif 24.9 > imc >= 18.5:
    clasificacion = "Normal"
    recomendacion = "Mantén tus hábitos saludables"

elif 25 < imc <= 29.9:
    clasificacion = "Sobrepeso"
    recomendacion = "Considera hacer ejercicio regularmente"

else: 
    clasificacion = "Obesidad"
    recomendacion = "Riesgo alto, consulta a un médico"

# Se muestran resultados
print("\n--- RESUMEN ---")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años (En 10 años tendrás {edad + 10})")
print(f"Altura: {altura:.2f}")
print(f"Pesos: {peso}")
print(f"IMC: {imc:.2f} ({clasificacion})")

# Consideraciones adicionales

if clasificacion.lower() == "sobrepeso" and edad > 50:
    print("ALTO RIESGO: combina sobrepeso con edad avanzada") 

elif clasificacion.lower() == "obesidad" and edad > 40:
    print("CRÍTICO: obesidad + edad > 40, requiere atención inmediata")

elif clasificacion.lower() == "normal" and edad < 18:
    print("Seguimiento pediátrico recomendado")




