from Modulo1 import *

#método "main" del módulo:
if __name__ == "__main__":

    print("1. agregar publisher\n")
    print("2. filtrar\n")
    print("3. salir\n")

    op = input("ingrese opción deseada:")

    #crear publishers:
    while op != 3:
        if op == 1:
            id = input("ingrese el id\n")
            nombre = input("ingrese el nombre\n")
            pais = input("ingrese el pais\n")
            tot_ventas = input("ingrese el total de ventas\n")
            addPublisher(id,nombre, pais, tot_ventas)            
        elif op == 2:
            tot_ventas = input("ingrese el total de ventas\n")
            filterPublisherByTotalSales_FilterLambda(tot_ventas)

        op = input("ingrese opción deseada:")



    