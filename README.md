# Scheduling Lab

## Descripción
Este proyecto demuestra cómo el sistema operativo gestiona la prioridad de procesos.

## Tecnologías
- Python
- macOS (nice command)

## Ejecución

Alta prioridad:
sudo nice -n -20 python3 heavy_task.py

Baja prioridad:
nice -n 19 python3 heavy_task.py

## Resultado
El proceso con mayor prioridad termina primero.
