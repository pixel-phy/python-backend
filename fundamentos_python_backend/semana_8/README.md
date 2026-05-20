# 📚 Semana 8: Conjuntos (Sets)

## 🎯 Objetivo de la semana

Aprender a utilizar **conjuntos (sets)** en Python, una estructura de datos que:
- Almacena **elementos únicos** (sin duplicados)
- Es **desordenada** (no mantiene el orden de inserción)
- Es **mutable** (se pueden agregar y eliminar elementos)
- Es **muy eficiente** para operaciones de pertenencia y eliminación de duplicados

Los conjuntos son ideales para:
- Eliminar duplicados de una lista
- Verificar pertenencia rápida (`x in conjunto`)
- Operaciones matemáticas de conjuntos (unión, intersección, diferencia)

---

## 📂 Estructura de la carpeta
semana_8_conjuntos/
├── README.md
├── S1_creacion_basica.py
├── S2_metodos_basicos.py
├── S3_eliminar_duplicados.py
├── S4_operaciones_conjuntos.py
├── S5_verificar_pertenencia.py
├── S6_subconjuntos_superconjuntos.py
├── S7_conjuntos_inmutables.py
├── S8_ejercicios_practicos.py
├── S9_repaso.py
└── proyecto_integrador.py

---

## 📋 Contenido de la semana

| Día | Ejercicio | Tema | Concepto clave |
|-----|-----------|------|----------------|
| Lunes | S1 | Creación de conjuntos | `set()`, `{}` |
| Lunes | S2 | Métodos básicos | `add()`, `remove()`, `discard()`, `clear()` |
| Martes | S3 | Eliminar duplicados | De listas a conjuntos |
| Martes | S4 | Operaciones de conjuntos | Unión (`\|`), intersección (`&`), diferencia (`-`), diferencia simétrica (`^`) |
| Miércoles | S5 | Verificar pertenencia | `in`, `not in` |
| Miércoles | S6 | Subconjuntos y superconjuntos | `issubset()`, `issuperset()`, `isdisjoint()` |
| Jueves | S7 | Conjuntos inmutables | `frozenset()` |
| Jueves | S8 | Ejercicios prácticos | Aplicaciones reales |
| Viernes | S9 | Repaso | Ejercicios variados |
| Sábado | - | Descanso / repaso | - |
| Domingo | Proyecto | Sistema de gestión de usuarios | Conjuntos para roles y permisos |

---

## 🔍 ¿Qué es un Conjunto (Set)?

**Principio:** Colección desordenada de elementos únicos.

```python
# Crear conjuntos
frutas = {"manzana", "pera", "uva"}
numeros = set([1, 2, 3, 2, 1])  # {1, 2, 3} (duplicados eliminados)
vacio = set()  # {} es diccionario vacío, no conjunto

# Agregar elementos
frutas.add("naranja")

# Eliminar elementos
frutas.remove("pera")  # si no existe, da error
frutas.discard("pera")  # si no existe, no da error

# Verificar existencia
if "manzana" in frutas:
    print("Hay manzana")

# Recorrer (sin orden garantizado)
for fruta in frutas:
    print(fruta)
```
🔍 Operaciones entre conjuntos

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Unión: elementos en A o B (o ambos)
union = A | B  # {1, 2, 3, 4, 5, 6}

# Intersección: elementos en A y B
interseccion = A & B  # {3, 4}

# Diferencia: elementos en A pero no en B
diferencia = A - B  # {1, 2}

# Diferencia simétrica: elementos en A o B pero no en ambos
dif_simetrica = A ^ B  # {1, 2, 5, 6}
🔍 Métodos importantes
Método	Qué hace	Ejemplo
add(x)	Agrega x al conjunto	s.add(5)
remove(x)	Elimina x (error si no existe)	s.remove(5)
discard(x)	Elimina x (no error si no existe)	s.discard(5)
clear()	Elimina todos los elementos	s.clear()
copy()	Crea una copia superficial	s2 = s.copy()
issubset()	¿Todos los elementos están en otro?	A.issubset(B)
issuperset()	¿Contiene todos los elementos de otro?	A.issuperset(B)
isdisjoint()	¿No tienen elementos en común?	A.isdisjoint(B)
```

🔍 Frozenset (conjunto inmutable)
```python
# Frozenset: versión inmutable del set
inmutable = frozenset([1, 2, 3])
# inmutable.add(4)  # ❌ AttributeError

# Útil para usarlo como clave de diccionario
diccionario = {frozenset([1, 2]): "valor"}
```