# 📚 Semana 7: Tuplas y Listas enlazadas

## 🎯 Objetivo de la semana

Aprender dos estructuras de datos fundamentales:
- **Tuplas:** Inmutables, rápidas y seguras
- **Listas enlazadas:** Secuencias dinámicas donde cada elemento apunta al siguiente

Estas estructuras son la base de sistemas que manejan datos inmutables (tuplas) y estructuras dinámicas (listas enlazadas).

---

## 📂 Estructura de la carpeta

semana_7_tuplas_listas_enlazadas/
├── README.md
├── T1_tuplas_creacion.py
├── T2_tuplas_desempaquetado.py
├── T3_tuplas_vs_listas.py
├── T4_metodos_tuplas.py
├── T5_ejercicios_tuplas.py
├── L1_nodos.py
├── L2_lista_enlazada_basica.py
├── L3_recorrer_lista.py
├── L4_buscar_en_lista.py
├── L5_insertar_nodos.py
├── L6_eliminar_nodos.py
├── T6_repaso.py
└── proyecto_integrador.py

---

## 📋 Contenido de la semana

| Día | Ejercicio | Tema | Concepto clave |
|-----|-----------|------|----------------|
| Sábado | T1 | Tuplas: creación y acceso | `()`, `[0]`, `[-1]` |
| Sábado | T2 | Tuplas: desempaquetado | `a, b, c = tupla` |
| Sábado | T3 | Tuplas vs listas | Inmutabilidad vs mutabilidad |
| Sábado | T4 | Métodos de tuplas | `.count()`, `.index()` |
| Sábado | L1 | Nodos | `class Nodo: valor, siguiente` |
| Sábado | L2 | Lista enlazada básica | Crear y enlazar nodos |
| Sábado | L3 | Recorrer lista enlazada | `while actual:` |
| Sábado | L4 | Insertar nodos | Inicio |
| Sábado | L5 | Insertar nodos | Final |
| Sábado | L6 | Insertar nodos | Medio |
| Sábado | L7 | Buscar en lista enlazada | Encontrar un valor |
| Sábado | L8 | Eliminar nodos | Reajustar punteros |
| Sábado | T6 | Repaso de tuplas | Ejercicios variados |
| Sábado | L7 | Repaso de listas enlazadas | Ejercicios variados |
| Domingo | Proyecto | Lista de tareas | Lista enlazada de tareas |

---

## 🔍 ¿Qué es una Tupla?

**Principio:** Inmutabilidad (no se puede modificar después de creada).

```python
# Crear tuplas
dias = ("lunes", "martes", "miércoles")
punto = (10, 20)
solo_un_elemento = (5,)  # ¡la coma es importante!

# Acceder a elementos
print(dias[0])   # lunes
print(dias[-1])  # miércoles

# Desempaquetado
a, b, c = dias
print(a, b, c)   # lunes martes miércoles

# Las tuplas son inmutables
dias[0] = "domingo"  # ❌ TypeError

## 🔍 ¿Qué es una cola enlazada?

**Principio:** Estructura de datos lineal que almacena elementos en orden secuencial. (Sigue el principio FIFO).

```python
# Crear listas enlazadas
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Asignamos valores a cada nodo
nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)

# Generamos conexiones entre nodos
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

# Recorremos toda la lista para mostrar valores
actual = nodo1
while actual is not None:
    print(actual.valor)
    actual = actual.siguiente