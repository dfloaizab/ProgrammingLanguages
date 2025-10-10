from abc import ABC, abstractmethod

# Define como contratos las operaciones de CRUD
class IMovieRepository(ABC):

    @abstractmethod
    def getAll(this):
        pass

# Principio "I": Interface Seggregation Principle, se separan comportamientos generales distintos 
# en varias interfaces, en vez de empacarlas en una sola interfaz.
# Las subclases implementan solo lo que vayan a usar
class IReadableRepository(ABC):

    @abstractmethod
    def read_all(this):
        pass

class WritableRepository(ABC):

    @abstractmethod
    def save_item(this, item):
        pass

