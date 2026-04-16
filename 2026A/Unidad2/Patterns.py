from abc import ABC, abstractmethod
import math

###### PATRONES DE DISEÑO

# PATRONES CREACIONALES: Determina cómo se instancian las clases en un módulo

# 1. Singleton: Solo se puede tener una instancia de una clase

# Cómo se implementa: 

class Singleton:

    #instancia de clase:
    _instance = None

    def __new__(cls):
        #crea la instancia solo si no existe.
        #no permite crear más instancias de la misma clase
        if cls._instance is None:
            print("Se crea nueva instancia...")
            cls._instance = super().__new__(cls)
        return cls._instance
    
    #Después agregamos más métodos o implementamos como clase abstracta...


instancia1 = Singleton()
instancia2 = Singleton()


# Cómo se usa:

