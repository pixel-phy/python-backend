# Algoritmos de validación de Datos con Python

## 📌 Descripción general

Esta semana estará dedicada al estudio y aplicación de **algoritmos de validación** fundamentales en sistemas de información. El enfoque principal será comprender cómo se generan y verifican los digitos de control en diferentes contextos, desde números de tarjetas hasta códigos de barras, utilizando **Python** como herramienta de implementación.

El objetivo es desarrollar un conjunto de habilidades que permitan:
- Implementar verificaciones de integridad de datos.
- Comprender la lógica matemática detrás de los digitos de control.
- Aplicar estos conceptos en un proyecto integrador funcional.

--- 

## Temario semanal 


### 1. Algoritmo de Luhn
- **Descripción**: El algoritmo de Luhn (o módulo 10) es un método de suma de verificación utilizado para validar números de identificación, como tarjetas de crédito y números de IMEI.
- **Actividades**:
  - Implementación del algoritmo en Python.
  - Validación de números de tarjeta de crédito ficticios.
  - Generación del dígito de control.

### 2. Checksum Básico
- **Descripción**: Introducción a los checksums como método simple de detección de errores. Se abordarán sumas de verificación básicas (ej. checksum de 8 bits).
- **Actividades**:
  - Cálculo de checksum para cadenas de texto.
  - Comparación entre diferentes métodos (suma simple, XOR, etc.).
  - Implementación de una función genérica de checksum.

### 3. Códigos de Barras
- **Descripción**: Estudio de los sistemas de codificación más comunes (EAN-13, UPC-A, Code 128) y sus mecanismos de validación.
- **Actividades**:
  - Decodificación y validación de códigos EAN-13.
  - Cálculo del dígito verificador para códigos de barras.
  - Simulación de lectura de códigos desde una entrada estándar.

### 4. Validación de restricciones (Constraint Validation)
- **Descripción**: Permite validar datos no solo por su formato, sino también por **reglas lógicas y relaciones entre campos**. Se basa en definir restricciones (condiciones que deben cumplirse) y verificar su satisfacción.
- **Actividades**:
  - Definición de un sistema de reglas en Python (diccionarios, clases o librerías coo `constraint`)
  - Validación de formularios complejos con múltiples campos relacionados.
  - Implementación de un motor de validación por restricciones.
  - Comparativa con validación por digitos verificadores (enfoques complementarios).

### 5. Dígitos Verificadores
- **Descripción**: Análisis de otros sistemas de dígitos de control (módulo 11, ISBN, RUT chileno, etc.).
- **Actividades**:
  - Implementación de validadores para distintos formatos.
  - Comparativa de algoritmos (módulo 10 vs módulo 11).
  - Manejo de excepciones y casos borde.

### 6. Ejercicios Integradores
- **Descripción**: Combinación de todos los conceptos anteriores en ejercicios que requieren múltiples validaciones.
- **Actividades**:
  - Validación de un formulario que incluya tarjeta, código de barras y RUT.
  - Detección de errores en lotes de datos.
  - Optimización de funciones para validación masiva.

### 7. Proyecto Integrador (Cierre de Semana)
- **Descripción**: Aplicación final que consolida todos los aprendizajes en un sistema completo.
- **Propuesta**: Desarrollar una **herramienta de validación de datos** que permita:
  - Ingresar diferentes tipos de identificadores.
  - Validar su integridad mediante el algoritmo correspondiente.
  - Mostrar resultados claros (válido/no válido y causa de error).
  - Generar un reporte de validación.
- **Entregables**: Código fuente documentado, pruebas unitarias y este README actualizado.

---
