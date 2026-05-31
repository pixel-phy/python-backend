# 📚 Semana 10 - Funciones (Parte 1)

## 📅 Cronograma: Fundamentos para Backend

| Día | Tema | Objetivo | Mini proyecto diario |
|-----|------|----------|---------------------|
| Día 1 | Definición y llamado básico | Crear funciones simples que reciban parámetros y retornen valores | Validador de formato de email |
| Día 2 | Parámetros posicionales, nombrados y valores por defecto | Controlar la flexibilidad de una función | Filtro de usuarios activos |
| Día 3 | Ámbito de variables (local vs global) | Evitar efectos colaterales en la lógica de negocio | Contador seguro de intentos fallidos |
| Día 4 | Retorno de valores (simple, múltiple, temprano) | Diseñar funciones que devuelvan datos estructurados | Procesador de precios (total, mayor, menor) |
| Día 5 | Docstrings y buenas prácticas | Escribir funciones auto-documentadas y mantenibles | Calculadora de impuestos documentada |
| Día 6 | Práctica con escenarios backend | Aplicar lo aprendido a casos reales (validaciones, transformaciones) | Validador de contraseñas + sanitizador de inputs |
| Día 7 | Proyecto integrador | Construir un mini gestor de tareas estilo API interna | Sistema de tareas con prioridades y resumen |

---

## 🧪 Proyecto integrador (Día 7)

**Nombre:** Task Manager Backend (versión funcional)

**Descripción:**  
Construir un conjunto de funciones que simulen la lógica interna de una API de gestión de tareas. Los datos se almacenan en una lista de diccionarios (simulando una base de datos en memoria).

**Funciones a implementar:**

| Función | Comportamiento |
|---------|----------------|
| `agregar_tarea(lista, nombre, prioridad)` | Agrega una tarea con estructura `{"nombre": str, "prioridad": "alta"/"media"/"baja", "completada": False}` |
| `completar_tarea(lista, nombre)` | Marca una tarea como `completada: True` |
| `mostrar_pendientes(lista)` | Retorna lista de tareas NO completadas, ordenadas por prioridad (alta → media → baja) |
| `guardar_resumen(lista)` | Retorna string: `"Total: X | Completadas: Y | Pendientes: Z"` |

---

## 📌 Buenas prácticas de backend aplicadas esta semana

- ✅ **Responsabilidad única:** Cada función hace una sola cosa.
- ✅ **Retornar, no imprimir:** Las funciones devuelven datos para que otra capa (API, vista, etc.) los use.
- ✅ **Nombres descriptivos:** `calcular_impuesto` en lugar de `calc`.
- ✅ **Docstrings obligatorios:** Toda función pública debe tener documentación.
- ✅ **Sin efectos secundarios:** No modificar variables globales innecesariamente.

---

## 📚 Recursos complementarios

- [Real Python - Defining Functions](https://realpython.com/defining-your-own-python-function/)
- [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
- [Python Scope & LEGB Rule](https://realpython.com/python-scope-legb-rule/)

---

**Próxima semana:** Funciones (Parte 2) → `*args`, `**kwargs`, funciones anidadas, lambda y `map/filter/reduce`
