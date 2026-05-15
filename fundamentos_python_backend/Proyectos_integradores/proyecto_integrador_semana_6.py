"""Proyecto integrador de pilas y colas:
Una clínica necesita un sistema para gestionar la atención de pacientes. Hay dos tipos de atención:
- Urgencias (prioridad alta): Se atiende primero
- Colsulta general (prioridad baja): Se atiende después
Dentro de cada tipo, se respeta el orden de llegada.
Requisitos:
1. Agregar paciente: nombre, tipo: urgencia/general (Dos colas separadas).
2. Atender paciente (primero urgencias, luego generales)
3. Mostrar colas en espera
4. Estadísticas: Total atendidos, urgencias atendidas, generales atendidas.
5. Salir."""