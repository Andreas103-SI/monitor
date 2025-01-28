# Proyecto de Monitoreo de Recursos del Sistema

Este proyecto es una aplicación de monitoreo de recursos del sistema, desarrollada utilizando Python. Su propósito es rastrear y mostrar métricas clave del sistema como el uso de CPU, memoria y disco en tiempo real. Es una herramienta útil para entender el rendimiento del sistema y detectar posibles cuellos de botella.

## Características

- Monitoreo en tiempo real del uso de CPU, memoria y disco.
- Configuración personalizable de la duración total del monitoreo y el intervalo de actualización.
- Reporte detallado en consola de las métricas monitoreadas.

## Requisitos

- Python 3.x
- Biblioteca psutil** (para recopilar métricas del sistema)

## Instalación

1. Clona el repositorio en tu máquina local:
   ```bash
   git clone https://github.com/Andreas103-SI/monitor.git
## Uso

1. Ejecuta el programa desde tu terminal:
   ```bash
   python monitor.py
## Ejemplo
 --- Estadísticas del Sistema ---
Uso de CPU: 85%
⚠️ ALERTA: El uso de CPU ha excedido el umbral de 80% (Actual: 85%)
Uso de Memoria: 70% (Usado: 5.20 GB / Total: 8.00 GB)
Uso de Disco: 50% (Usado: 120.00 GB / Total: 500.00 GB)

