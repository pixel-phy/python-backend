# 📚 Semana 11: Funciones (parte 2)

## 🎯 Objetivo de la semana

Profundizar en el uso de funciones en Python, cubriendo conceptos avanzados que permiten escribir código más flexible, reutilizable y elegante.

---

## 📂 Estructura de la carpeta
semana_11_funciones_parte2/
├── README.md
├── F1_args_kwargs.py
├── F2_lambda.py
├── F3_funciones_anidadas.py
├── F4_recursion.py
├── F5_decoradores.py
├── F6_ejercicios_integradores.py
├── F7_repaso.py
└── proyecto_calculadora.py


---

## 📋 Contenido de la semana

| Día | Ejercicio | Tema | Concepto clave |
|-----|-----------|------|----------------|
| Lunes | F1 | `*args` | Argumentos variables posicionales |
| Lunes | F1 | `**kwargs` | Argumentos variables nombrados |
| Martes | F2 | Funciones lambda | Funciones anónimas de una línea |
| Miércoles | F3 | Funciones anidadas | Funciones dentro de funciones |
| Miércoles | F3 | `nonlocal` | Modificar variables de función externa |
| Jueves | F4 | Recursión básica | Funciones que se llaman a sí mismas |
| Viernes | F5 | Decoradores básicos | Funciones que modifican otras funciones |
| Sábado | F6 | Ejercicios integradores | Aplicar todo lo aprendido |
| Domingo | Proyecto | E-Commerce Core | Aplicación completa |

---

## 🔍 ¿Qué es `*args`?

Permite pasar un número variable de argumentos posicionales a una función. Los argumentos se reciben como una **tupla**.

```python
def sumar_todos(*args):
    return sum(args)

print(sumar_todos(1, 2, 3, 4))  # 10
print(sumar_todos(5, 10))       # 15

```
---

## 🔍 ¿Qué es `**kwargs`?

Permite pasar un número variable de argumentos nombrados (clave-valor) a una función. Los argumentos se reciben como un **diccionario**.

```python
def mostrar_datos(**kwargs):
    for clave, valor in kwargs.items():
    print(f"{clave}: {valor}")

  mostrar_datos(nombre="Ana", edad=15, ciudad="Madrid")
```

---

## 🔍 ¿Qué son las funciones lambda?

Funciones anónimas (sin nombre) de una sola línea. Útiles para operaciones simples y como argumentos de otras funciones.

``` Python
# Función normal
def cuadrado(x):
    return x ** 2

# Lambda equivalente
cuadrado = lambda x: x ** 2

# Uso común con sorted()
numeros = [1, 4, 2, 5, 3]
ordenados = sorted(numeros, key=lambda x: -x)  # orden descendente

```

---

## 🔍 ¿Qué son funciones anidadas?

Funciones definidas dentro de otras funciones. Útiles para encapsular lógica y crear closures.

``` python

def exterior(mensaje):
    def interior():
        print(mensaje)
    return interior

saludo = exterior("Hola")
saludo()  # Hola

```
---

## 🔍 ¿Qué es nonlocal?

Permite modificar variables definidas en fucniones externas (no globales).

```python
def contador():
    valor = 0
    def incrementar():
        nonlocal valor
        valor += 1
        return valor
    return incrementar

cuenta = contador()
print(cuenta())  # 1
print(cuenta())  # 2
```

---

## 🔍 ¿Qué es recursión?

Una función que se llama a sí misma. Debe tener un caso base (condición de parada) para evitar bucles infinitos.

``` python

def factorial(n):
    if n == 0:          # caso base
        return 1
    return n * factorial(n - 1)  # llamada recursiva

print(factorial(5))  # 120
```

---

## 🔍 ¿Qué son decoradores?

Funciones que reciben otra función como argumento, la "envuelven" y devuelven una función modificada.

```python

def mi_decorador(func):
    def wrapper():
        print("Antes de la función")
        func()
        print("Después de la función")
    return wrapper

@mi_decorador
def saludar():
    print("¡Hola!")

saludar()
```

---


