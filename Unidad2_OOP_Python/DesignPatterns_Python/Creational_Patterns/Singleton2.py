#Singleton - beneficios:
#1. evitar acceso concurrente a recurso compartido
#2. tener un punto de acceso global a un recurso

#formas de implementación

#Ejemplo de singleton "clásico"

class ClassicSingleton:

    _instance_ = None

    def __init__(this):
        raise RuntimeError("invocar la función create_instance para crear objeto")
    
    #métodos de instancia
    def enqueueDocument(this, fileName, format):
        pass

    def dispatchDocument(this, fileName):
        pass

    def deleteDocument(this, fileName):
        pass
    
    #un "classmethod es un método estático"
    @classmethod
    def createInstance(this):
        if this._instance_ is None:
            #lo hace solo una vez, cuando no se ha instanciado ningún objeto
            this._instance_ = this.__new__(this) 
            #__new__ lo usa internamente __init__ para crear una nueva instancia de clase
        
        return this._instance_
    
######### fin de implementación del singleton

#tratamos de crear con el método init:
#printerPool1 = ClassicSingleton()
#printerPool2 = ClassicSingleton()

#Ejemplo de uso del singleton clásico:

printerPool1 = ClassicSingleton.createInstance() #lo llamo como método estático, no
                                                 #método de objeto
printerPool2 = ClassicSingleton.createInstance()

print(printerPool1)
print(printerPool2)

print(printerPool1 == printerPool2)


