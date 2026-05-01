from multiprocessing import Process
import time

# UNA TAREA ES:
# Unidad funcional que vamos a ejecutar concurrentemente
# (En este caso es un proceso)
def tarea(nombre):
    print(f"Iniciando tarea {nombre}")
    time.sleep(5)
    print(f"Finalizando tarea {nombre}")

# Lista de procesos:
procesos = []
# Vamos a crear 10 procesos, donde cada uno va a ejecutar la tarea
# definida
for i in range(10):
    # Creamos el proceso:
    p = Process(target = tarea, args=(f"Proceso-{i}"))
    # Lo agregamos a la lista:
    procesos.append()
    # Lo iniciamos:
    p.start()

for p in procesos:
    p.join()
