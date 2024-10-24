from Model import *
from View  import *
from Controller import *

def main():
    #instanciar objetos de MVC:
    myModel = ProductModel()
    myView = ProductView()
    myController = ProductCatalogController(myModel, myView)

    #imprimir menú de opciones:
    print("Menu\n")
    print("1. Adicionar Producto")
    print("2. Mostrar Catálogo")
    print("3. Salir")

    #manejar opciones:
    sel = int(input("seleccione una opción"))
    if sel == 1:
        myController.addNewProduct()
    elif sel == 2:
        myController.showProducts()
    elif sel == 3:
        pass
    else:
        print("opcion no válida")


if __name__== "__main__":
    main()