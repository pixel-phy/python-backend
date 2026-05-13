"""Evaluar expresión matemática con pilas:
Escribir un programa que evalúe expresiones matemáticas simples con + y -, respetando el orden de izquierda a derecha, usando dos pilas (una para números,
otra para operadores)."""

expresion = input("Expresión: ")

numeros_entrada = []
signos = []


for caracter in expresion:
    if caracter == "+" or caracter == "-":
        signos.append(caracter)
    if caracter.isdigit():
        numeros_entrada.append(int(caracter))

resultado = numeros_entrada[0]

for i in range(len(signos)):
    if signos[i] == "+":
        resultado = resultado + numeros_entrada[i + 1]
    elif signos[i] == "-":
        resultado = resultado - numeros_entrada[i + 1]

print(f"Resultado: {resultado}")