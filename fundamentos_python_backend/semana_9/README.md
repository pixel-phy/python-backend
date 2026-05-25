# 📚 Semana 9: Diccionarios (Dict)

## 🎯 Objetivo de la semana

Aprender a utilizar **diccionarios** en Python, una de las estructuras de datos más importantes y utilizadas en backend.

Los diccionarios permiten:
- Almacenar datos en **pares clave-valor**
- Acceso rápido por clave (O(1))
- Representar objetos (usuarios, productos, configuraciones)
- Datos anidados (diccionarios dentro de diccionarios)

---

## 📂 Estructura de la carpeta
semana_9_diccionarios/
├── README.md
├── D1_creacion_basica.py
├── D2_acceso_elementos.py
├── D3_metodos_basicos.py
├── D4_recorrer_diccionarios.py
├── D5_metodos_avanzados.py
├── D6_diccionarios_anidados.py
├── D7_dict_comprehension.py
├── D8_ejercicios_practicos.py
├── D9_repaso.py
└── proyecto_integrador.py


---

## 📋 Contenido de la semana

| Día | Ejercicio | Tema | Concepto clave |
|-----|-----------|------|----------------|
| Lunes | D1 | Creación de diccionarios | `{}`, `dict()`, pares clave-valor |
| Lunes | D2 | Acceso a elementos | `dict["clave"]`, `.get()` |
| Martes | D3 | Métodos básicos | `.keys()`, `.values()`, `.items()` |
| Martes | D4 | Recorrer diccionarios | `for clave in dict`, `for valor in dict.values()` |
| Miércoles | D5 | Métodos avanzados | `.pop()`, `.update()`, `.setdefault()` |
| Miércoles | D6 | Diccionarios anidados | `{"usuario": {"nombre": "Ana", "edad": 25}}` |
| Jueves | D7 | Dict comprehension | `{x: x**2 for x in range(5)}` |
| Jueves | D8 | Ejercicios prácticos | Aplicaciones reales |
| Viernes | D9 | Repaso | Ejercicios variados |
| Sábado | - | Descanso / repaso | - |
| Domingo | Proyecto | Sistema de inventario con diccionarios | CRUD completo |

---

## 🔍 ¿Qué es un Diccionario?

**Principio:** Colección **desordenada** de pares **clave → valor**.

```python
# Crear diccionarios
usuario = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

# Acceder a valores
print(usuario["nombre"])  # Ana
print(usuario.get("edad"))  # 25

# Modificar valores
usuario["edad"] = 26

# Agregar nuevos pares
usuario["profesion"] = "Ingeniera"

# Eliminar pares
del usuario["ciudad"]
edad = usuario.pop("edad")  # elimina y devuelve el valor
```

## 🔍 Recorrer diccionarios

```python
usuario = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

# Recorrer claves
for clave in usuario:
    print(clave, usuario[clave])

# Recorrer valores
for valor in usuario.values():
    print(valor)

# Recorrer pares (clave, valor)
for clave, valor in usuario.items():
    print(f"{clave}: {valor}")
```
## 🔍 Dict comprehension
```python
# Crear diccionario de cuadrados
cuadrados = {x: x**2 for x in range(5)}
print(cuadrados)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Filtrar
pares_cuadrados = {x: x**2 for x in range(10) if x % 2 == 0}
print(pares_cuadrados)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

## 🔍 Diccionarios anidados
```python
# Diccionario dentro de diccionario
empresa = {
    "empleado1": {"nombre": "Ana", "edad": 25},
    "empleado2": {"nombre": "Luis", "edad": 30}
}

print(empresa["empleado1"]["nombre"])  # Ana
```