import threading
import time
import random

#Recurso compartido:
contador = 0

#Candado: objeto que controla o restringe el acceso de los hilos al recurso compartido
lock = threading.Lock()

#Función que representa la tarea que ejecutarán los hilos de forma concurrente:
def tarea(nombreHilo):
    global contador

    print(f"Iniciando hilo...{nombreHilo}")

    # INICIO Sección crítica: fragmento de código que accede al recurso compartido
    # AÚN NO HAY SINCRONIZACIÓN:

    #El candado bloquea el recurso para el hilo con acquire
    lock.acquire()
    contador = contador + 1
    #...lo libera con release
    lock.release()
   
    #Sleep aleatorio:
    time.sleep(int(random.random())*100)
    # FIN DE SECCIÓN CRÍTICA

    print(f"Finalizando...{nombreHilo}")


# Creación de los hilos: "pool" de hilos:
hilos = []

#Crear 10 hilos e iniciar:
for i in range(10):
    t = threading.Thread(target=tarea, args=(f"Hilo+{i}",))
    hilos.append(t)
    t.start()

# "Unir" (join) hilos al hilo principal:
for t in hilos:
    t.join()

#Imprimir valor final del contador:
print(f"Valor final del contador:{contador}")