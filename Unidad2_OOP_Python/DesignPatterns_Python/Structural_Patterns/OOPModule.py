#IMPLEMENTATION OF THE ADAPTER PATTERN

# class adapterXML(XMLInterface):
#     def getData(self):
#         return "<XML>data</XML>"
    
# class adapterJSON(JSONInterface):
#     def getData(self):
#         return "{data1: 'value'}"
    
# class adapterTXT(TXTInterface):
#     def getData(self):
#         return "plain text data"


# class JSONInterface:
#     def getData(self):
#         pass
#     def setData(self):
#         pass

# class TXTInterface:
#     def getData(self):
#         pass
#     def setData(self):
#         pass

class XMLInterface:
    def getData(self):
        pass    
    def setData(self):
        pass

#clase adaptada
class Source(XMLInterface):
    def getData(self):
        return "<XML>data</XML>"

#interfaz destino:
class TxtInterface():
    def getData(self):
        pass
    def setData(self):
        pass

class Adapter(TxtInterface):
    __source = None

    def __init__(self, source):
        self.__source = source

    def getData(self):
        return "plain text data"
    
class Client_TXT:

    _sourceType = None

    def __init__(self, sourceType):
        self._sourceType = sourceType

    def getClientData(self):
        if self._sourceType.getData() == "plain text data":
            print("Datos correctos")
        else:
            print("datos incorrectos")


fuenteXML = Source()
adaptador = Adapter(fuenteXML)
miCliente = Client_TXT(adaptador)

miCliente.getClientData()









#La clase session es una clase SINGLETON
#solo admite una instancia a la vez
class Session:
    #atributo de clase para almacenar la instancia creada:
    __instance = None
    #"constructor"
    def getInstance():
        if Session.__instance == None:
            Session()
        return Session.__instance

    def __init__(self):
        if Session.__instance != None:
            raise Exception("Ya se ha creado una instancia de esta clase")
        else:
            Session.__instance = self










class Person:
    #atributos de clase:
    maxCourses = 100
    campus = "Pampalinda"
    #atributos de instancia:
    def __init__(self, name, document):
        self.name = name
        self.document = document

    #sobrecarga de la funcion print del objeto
    def __str__(self):
        return f"nombre:{self.name},documento:{self.document},campus:{self.campus}"      

    def printInfo(self):
        print(self.maxCourses)
        print(self.campus)
        print(self.name)
        print(self.document)

#sub-clases de persona:
class Student(Person):
    pass

class OperativeEmployee(Person):
    pass

class ManagementEmployee(Person):
    pass





