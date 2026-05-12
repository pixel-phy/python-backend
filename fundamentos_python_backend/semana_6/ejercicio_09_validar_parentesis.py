"""Validar paréntesis (pila)
Un compilador o editor de código necesita verificar que los paréntesis, corchetes y llaves estén correctamente balanceados.
- El programa debe pedir una expresión al usuario.
- Usar una pila para verificar que los símbolos de apertura ([{coincidan con los de cierre}])
- Mostrar "✅ Balanceado" o "❌ No balanceado"."""

print("\n=== Validador de paréntesis ===")

expresion = input("Expresión: ")

pila = []
balanceado = True

for caracter in expresion:
    if caracter == '(' or caracter == '[' or caracter == '{':
        pila.append(caracter)
    
    elif caracter == ')':
        if not pila or pila[-1] != '(':
            balanceado = False
            break
        pila.pop()
    
    elif caracter == ']':
        if not pila or pila[-1] != '[':
            balanceado = False
            break
        pila.pop()
    
    elif caracter == '}':
        if not pila or pila[-1] != '{':
            balanceado = False
            break
        pila.pop()

# Si quedaron símbolos dentro de la pila, no está balanceado
if pila:
    balanceado = False

if balanceado:
    print("✅ Balanceada")
else:
    print("❌ No balanceada")