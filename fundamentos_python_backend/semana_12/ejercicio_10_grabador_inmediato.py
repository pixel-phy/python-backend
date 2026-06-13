"""El grabador inmediato (Simulador de Emergencia)
    Escribe un script que abra un archvio llamado seguridad.log en modo a. El programa debe 
    escribir la frase "ALERTA: Intento de intrusión detectado\n". Imagina que después de esa línea
    código viene un proceso muy pesado o peligroso que podría congelar el sistema."""

archivo_seguridad = open("seguridad.log", mode="a", encoding="utf-8")

frase = "Alerta: Intento de intrusión detectado\n"

archivo_seguridad.write(frase)

archivo_seguridad.flush()

archivo_seguridad.close()
