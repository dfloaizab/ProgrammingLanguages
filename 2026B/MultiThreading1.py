import random
import threading
import time

# Lista de 10 vehículos: (Nombre, Tiempo de carga en segundos)
vehiculos = [
    ("Tesla Model 3", 3),
    ("Nissan Leaf", 2),
    ("BYD Dolphin", 4),
    ("Chevrolet Bolt", 2),
    ("Hyundai Ioniq 5", 3),
    ("Kia EV6", 2),
    ("Renault Zoe", 4),
    ("Ford Mustang Mach-E", 3),
    ("Volvo XC40", 2),
    ("BMW i4", 3),
]

estaciones_en_uso = 0


def cargar_sin_control(nombre, tiempo):
    global estaciones_en_uso

    # ¡PROBLEMA! No hay límite, todos entran de golpe
    estaciones_en_uso += 1
    print(
        f"[INICIO] {nombre} conectando... (Estaciones activas:"
        f" {estaciones_en_uso})"
    )

    time.sleep(tiempo)  # Simula el tiempo de carga

    estaciones_en_uso -= 1
    print(
        f"[FIN] {nombre} terminó en {tiempo}s. (Estaciones activas:"
        f" {estaciones_en_uso})"
    )


# Ejecución
hilos = []
inicio = time.time()

for nombre, tiempo in vehiculos:
    hilo = threading.Thread(target=cargar_sin_control, args=(nombre, tiempo))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print(f"\nTiempo total: {time.time() - inicio:.2f}s")
# Resultado erróneo: Verás que "Estaciones activas" llega hasta 10.
