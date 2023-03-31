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
