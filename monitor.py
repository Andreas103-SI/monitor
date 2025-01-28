import psutil  # Biblioteca para obtener información sobre el uso de recursos del sistema
import time # Biblioteca para manejar tiempos de espera
from datetime import datetime # Para trabajar con fechas y horas


# Función para mostrar el uso de CPU, memoria y disco
def mostrar_estadisticas():
    print("\n--- Estadísticas del Sistema ---")
    # Uso de CPU
    uso_cpu = psutil.cpu_percent(interval=1) # Obtiene el uso de CPU en un intervalo de 1 segundo
    print(f"Uso de CPU: {uso_cpu}%")

    # Uso de memoria
    memoria = psutil.virtual_memory() # Obtiene información sobre la memoria
    print(f"Uso de Memoria: {memoria.percent}% (Usado: {memoria.used / (1024**3):.2f} GB / Total: {memoria.total / (1024**3):.2f} GB)")

    # Uso de disco
    disco = psutil.disk_usage('/')  # Obtiene información sobre el disco principal
    print(f"Uso de Disco: {disco.percent}% (Usado: {disco.used / (1024**3):.2f} GB / Total: {disco.total / (1024**3):.2f} GB)")

# Función principal para actualizar y registrar las métricas
def monitorizar_sistema(duracion=30, intervalo=1):#Intervalo unificado
    """
    Monitorea el uso de recursos del sistema durante un periodo determinado.
    
    Args:
        duracion (int): Duración total del monitoreo en segundos (por defecto, 30 segundos).
        intervalo (int): Intervalo de actualización en segundos (por defecto, 1 segundo).
    """
    print("Iniciando monitorización del sistema...")
    inicio = datetime.now() # Guarda la hora de inicio de la monitorización
    
    try:
         # Bucle que ejecuta el monitoreo hasta que se alcance la duración indicada
        while (datetime.now() - inicio).seconds < duracion:
            mostrar_estadisticas() # Muestra las métricas actuales
            time.sleep(intervalo)  # Espera el tiempo definido antes de la siguiente iteración
    except KeyboardInterrupt:
        # Captura la interrupción manual del usuario (Ctrl + C)
        print("\nMonitorización detenida por el usuario.")
    finally:
        print("\nFinalizó la monitorización del sistema.")

# Punto de entrada principal del programa
if __name__ == "__main__":
    """
    Este bloque se ejecuta solo si el archivo es ejecutado directamente (no importado como módulo).
    Inicia la monitorización del sistema con una duración de 60 segundos y actualizaciones cada 2 segundos.
    """
    monitorizar_sistema(duracion=60, intervalo=2) #Duracion e intervalo ajustable





