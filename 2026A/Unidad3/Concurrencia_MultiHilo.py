import threading
import time

# Esta función es la tarea que va a ejecutar cada hilo:
def tarea(nombre):
    print(f"Iniciando tarea {nombre}")
    time.sleep(5)
    print(f"Finalizando tarea {nombre}")


# Creamos un conjunto de hilos:
hilos = []
for i in range(10):
    t = threading.Thread(target=tarea, args=f"Hilo+{i}")
    hilos.append(t)
    t.start()

# Someter los hilos al control del hilo principal
# El hilo principal espera a que los otros hilos terminen:
for t in hilos:
    t.join()

