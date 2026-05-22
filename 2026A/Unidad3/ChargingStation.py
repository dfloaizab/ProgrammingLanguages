from threading import Thread, Semaphore, current_thread
import time
import random

'''
Lenguajes de Programación 2026 A
Concurrencia en Python:
Ejercicio:
Simulación de una estación de carga para vehículos eléctricos.

La estación posee solamente 3 cargadores disponibles.
'''

class ChargingStation:

    def __init__(self, capacity):

        # TODO:
        # Crear un semáforo que controle
        # la cantidad de cargadores disponibles.
        pass

    def charge_vehicle(self, vehicle_name, charge_time):

        driver = current_thread().name

        print(f"{driver} llegó con el vehículo {vehicle_name}")

        # TODO:
        # Solicitar acceso a un cargador.
        

        try:

            print(f"{vehicle_name} comenzó a cargarse.")
            print(f"Tiempo estimado: {charge_time} segundos")

            # Simulación del tiempo de carga
            time.sleep(charge_time)

            print(f"{vehicle_name} terminó de cargarse.")

        except:
            print("Error durante el proceso de carga.")

        finally:

            # TODO:
            # Liberar el cargador.
            

            print(f"{vehicle_name} abandonó la estación.\n")


# Crear estación con capacidad para 3 vehículos simultáneos
station = ChargingStation(capacity=3)

# Lista de vehículos
vehicles = [

    Thread(
        name="Conductor 1",
        target=station.charge_vehicle,
        args=("Tesla Model 3", random.randint(2,6))
    ),

    Thread(
        name="Conductor 2",
        target=station.charge_vehicle,
        args=("BYD Dolphin", random.randint(2,6))
    ),

    Thread(
        name="Conductor 3",
        target=station.charge_vehicle,
        args=("Nissan Leaf", random.randint(2,6))
    ),

    Thread(
        name="Conductor 4",
        target=station.charge_vehicle,
        args=("Kia EV6", random.randint(2,6))
    ),

    Thread(
        name="Conductor 5",
        target=station.charge_vehicle,
        args=("Hyundai Ioniq 5", random.randint(2,6))
    ),

    Thread(
        name="Conductor 6",
        target=station.charge_vehicle,
        args=("Renault Kwid E-Tech", random.randint(2,6))
    )
]

print("Estación de carga iniciada.\n")

# TODO:
# Iniciar todos los hilos.


# TODO:
# Esperar a que todos los hilos finalicen.


print("Todos los vehículos fueron cargados.")

#MODIFICACIONES:

# 1. Los vehículos manejan prioridades: "first responders", ambulancias y vehículos de bomberos, tienen prioridad 3.
#                                        vehículos de transporte de pasajeros y carga, prioridad 2.
#                                        vehículos particulares, prioridad 1
#                                        expropiar cargador a vehículos con menor prioridad cuando llegue uno
#                                        con mayor prioridad
# 2. Manejar límite de tiempo máximo de permanencia en el cargador
