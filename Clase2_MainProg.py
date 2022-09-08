
import Module2 as m2


def MyMain():
    
    #pass #Instrucción vacía (no hacer nada)
    #leer nombre del archivo:
    myFileName = input("Ingrese el nombre del archivo:")
    DataBase1 = m2.loadDataCSV(myFileName)
    print(type(DataBase1))
    print(type(DataBase1[0]))


#Definir punto de entrada del módulo a la función MyMain
if __name__ == "__main__":
    MyMain()
