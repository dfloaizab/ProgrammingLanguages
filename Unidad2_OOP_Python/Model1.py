class DataLoader:

    #atributo de clase, compartido entre todas las instancias
    #de la clase
    loads = 0

    #método de inicialización, invocado al crear un objeto
    def __init__(self, pFileName):
        
        #loads es un atributo de clase:
        DataLoader.loads += 1

        #fileName es una atributo de instancia
        self.fileName = pFileName

    def loadCSV():
        pass

    def loadJSON():
        pass

    def loadXML():
        pass
    
    
    class Entity1:
        pass
    
    class Entity2:

    
