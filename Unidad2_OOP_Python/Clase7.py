#Importar todo del módulo
#from Module1_OOP import *
#import Module1_OOP

#Importar solo la clase DataLoader del módulo
from Module1_OOP import DataLoader

def Main():
    loader1 = DataLoader("dataset1.csv")
    #Mostrar atributo de instancia, que es exclusivo del objeto
    print(f"El loader 1 carga del archivo {loader1.fileName}")

    loader2 = DataLoader("dataset2.json")
    print(f"El loader 2 carga del archivo {loader2.fileName}")

    #Imprimir cuántas cargas se han realizado hasta el momento:
    print(f"Total de cargas:{DataLoader.loads}")

if __name__ == "__main__":
    Main()
