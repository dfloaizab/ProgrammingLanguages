
#Una función pura en python (no modifica el parámetro de entrada, 
# crea una nueva variable)
#entrada: una lista de enteros
#salida: una COPIA de la lista de entrada, con sus valores ^2
def unaFuncionPura(listaDeEntrada):
    #una lista vacía en python:
    listaSalida = []
    #iterando en una lista:
    for x in listaDeEntrada:
        #agregando un elemento a una lista:
        listaSalida.append(x**2)

    return listaSalida

def convertirAMayusculas(listaEntrada):
    listaNueva = []
    for nombre in listaEntrada:
        listaNueva.append(str(nombre).upper())
    return listaNueva

def convertirAMinusculas(listaEntrada):
    listaNueva = []
    for nombre in listaEntrada:
        listaNueva.append(str(nombre).lower())
    return listaNueva






    

