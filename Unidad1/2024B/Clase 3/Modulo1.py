#Modulo para implementar un CRUD pequeñito
#para una plataforma de streaming de videojuegos

#cada colección está implementada como una lista de
#diccionarios:

publishers = []
videogames = []
users = []
reviews = []

def addPublisher(id, name, country, total_sales):
    newPublisher = {"id":id,"name":name,"country":country}
    publishers.append(newPublisher)

def filterPublisherByTotalSales_iter(totalSales):
    filteredList = []
    for rec in publishers:
        if rec["total_sales"] == totalSales:
            filteredList.append(rec)    
    return filteredList


#usando la función de orden superior "filter" y una función lambda de filtrado:
def filterPublisherByTotalSales_FilterLambda(totalSales):

    #funcion de filtrado:
    #se aplica sobre cada elemento de la lista, que es un diccionario
    #de cada elemento, miro si la llave total_sales corresponde al parámetro
    filterFunction2 = lambda x: x["total_sales"] == totalSales
    filteredList = list (  filter (filterFunction2  , publishers))
    return filteredList



