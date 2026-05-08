# SINCRONIZACIÓN EN CONCURRENCIA MULTI-HILO
import threading
import time
import random

#Recurso compartido, saldo de una cuenta, variable float:
saldo = 0.0

#Candado: objeto que controla o restringe el acceso de los hilos al recurso compartido
lock = threading.Lock()

#Función que representa la tarea que ejecutarán los hilos de forma concurrente:
def depositar(nombreHilo, valor):
    pass

def retirar(nombreHilo, valor):
    pass
    
# Creación de los hilos: "pool" de hilos:
hilos = []

#Crear 2 hilos e iniciar:
#Cada Hilo va a hacer varios retiros y depositos de forma concurrente
#Procurar sincronizar con el candado y validar la consistencia del saldo:
for i in range(2):
    # tarea = depositar 
    # tarea = retirar
    t = threading.Thread(target=tarea, args=(f"Hilo+{i}",))
    hilos.append(t)
    t.start()

# "Unir" (join) hilos al hilo principal:
for t in hilos:
    t.join()

#Imprimir valor final del contador:
print(f"Valor final del saldo:{saldo}")