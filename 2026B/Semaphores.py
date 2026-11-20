from threading import Thread, Semaphore, current_thread
import time
'''
Semáforos: "candados" con conteo que limita el número de accesos a un recurso
            (un "mutex", mutual exclusion lock, puede ser visto como un candado de 2 estados, abierto
            o cerrado y limita el acceso a un hilo a la vez)
'''

#Ejemplo: hay una sala de lectura para 4 personas, y de esa forma se permite
#         el acceso solo a esa cantidad, a leer los libros que quieran:

#         (Se encapsula el recurso, la función con el área crítica y el semáforo en una sola clase)
class Library:
    def __init__(self, capacity)->None:
        #Parámetro del semáforo:número de hilos a los cuales dará acceso
        self.librarian = Semaphore(value=capacity)

    def requestToRead(self, book, read_time):
        person_name = current_thread().name
        self.librarian.acquire()
        try:
            print(f"{person_name} empezó a leer {book} por {read_time} segundos.")
            time.sleep(read_time)
            print(f"{person_name} terminó de leer.")
        except:
            print("Error de ejecución de hilos.")
        finally:
            self.librarian.release()

#Se crea un objeto Library (con su función concurrente, su función crítica y su mecanismo de sincronización - Semáforo)
MyLibrary = Library(capacity=4)

#Se crean los lectores como una lista de hilos:
readers = [
    Thread(name="Diego", target=MyLibrary.requestToRead, args=("Stoner, de John Williams",10)),
    Thread(name="Diana", target=MyLibrary.requestToRead, args=("Dune, de Frank Herbert",10)),
    Thread(name="Juan", target=MyLibrary.requestToRead, args=("Pálido Fuego, de Vladimir Nabokov",10)),
    Thread(name="Paula", target=MyLibrary.requestToRead, args=("Trainspotting, de Irving Welsh",10)),
    Thread(name="Clara", target=MyLibrary.requestToRead, args=("Cartas a Clara, de Juan Rulfo",10)),
    Thread(name="Carolina", target=MyLibrary.requestToRead, args=("Los Detectives Salvajes, Roberto Bolaño",10)),
    Thread(name="Isabel", target=MyLibrary.requestToRead, args=("La Carretera, de Cormack McCarthy",10)),
    Thread(name="María Fernanda", target=MyLibrary.requestToRead, args=("Klara y el Sol, de Kazuo Ishiguro",10))
]

print(f"Biblioteca con capacidad de : {MyLibrary.librarian._value}")
print(f"N° de Lectores: {len(readers)}")

# Enter all reader at same time
for _r in readers:
    _r.start()

# wait to finish all threads.
for _r in readers:
    _r.join()

print("Todos terminaron de leer y quedaron contentos.")
