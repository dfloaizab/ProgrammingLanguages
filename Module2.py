def loadDataCSV(fileName):

    file = open(fileName,"r")
    namesList = []
    timesList = []
    pointsList = []
    DictList = []

    for line in file:
        #la función strip elimina los caracteres especiales al final de la línea:
        text = line.strip()
        #convertir linea a una lista de valores:
        
        valuesList = text.split(";") #valuesList = [ "Dflb1977", "1500", "700"]

        # namesList.append( valuesList[0] )
        # timesList.append( valuesList[1] )
        # pointsList.append( valuesList[2] )

        dict1 = {"nick": valuesList[0],
                 "time": valuesList[1],
                 "points": valuesList[2] }
        DictList.append(dict1)

    return DictList
        
        
    #print(DictList)
    # print(namesList)
    # print(timesList)
    # print(pointsList)


        



