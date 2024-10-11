#1. CREATIONAL PATTERNS: se centran en cómo son creados los objetos en un módulo 
#                        de software
#1.a Singleton: Solo se admite una instancia de 1 objeto en un módulo de software

# class NotSingleton():

#     def __init__(self,user, pwd):
#         self.user = user
#         self.pwd = pwd

# notSingleton1 = NotSingleton("Diego","abcd1234")
# notSingleton2 = NotSingleton("Diana", "efgh5678")
# #notSingleton1 y notSingleton2
# print(notSingleton1 is notSingleton2)


# class Singleton():
#     #atributo de clase para la instancia de clase
#     #(inicialmente es None, o Null)
#     _instance = None

#     #método de instanciación de clase:
#     def __new__(this):
#         #valida que no se haya creado una instancia antes:
#         if this._instance is None:
#             #crea una instancia como objeto genérico de python
#             this._instance = super(Singleton, this).__new__(this)
#             #atributo de instancia, de ejempl
#             this._instance.config = {}
#         return this._instance
    
# objeto1 = Singleton()
# objeto2 = Singleton()

# print("Funciona el uso del singleton?:")
# print(objeto1)
# print(objeto2)

# print(objeto1 is objeto2)

#Ejemplo de aplicación:
#Un objeto de conexión a base de datos que se comporta como un singleton
#solo se admite una instancia de la clase DatabaseConnection en el módulo
#USO: Administración de recursos compartidos: configuraciones globales, recursos
#limitados, etc
# class DatabaseConnection(Singleton):

#     def __init__(this):
#         if  "connection_string" not in this.config:
#             this.config["connection_string"] = this.connectToDatabase()

#     def connectToDatabase(this):
#         return "sample connection string"
    
# connection1 = DatabaseConnection()
# connection2 = DatabaseConnection()
# print(f"son la misma conexión?{connection1 is connection2}")

    
# 2. BEHAVIORAL PATTERNS

# OBSERVER: permite que objetos se suscriban a los cambios o eventos generados por
#           otro objeto
#emisora de los eventos o de los mensajes, a los que se suscriben los observadores:
# class Subject:

#     def __init__(this):
#         this._observers = []

#     def attach(this, observer):
#         this._observers.append(observer)

#     def detach(this, observer):
#         this._observers.remove(observer)

#     def notify(this, message):
#         for observer in this._observers:
#             observer.update(message)

# #observador genérico
# class Observer():
#     def update(this, message):
#         #implementar manejo del mensaje en el observador concreto
#         pass

# #observador concreto:
# class ConcreteObserver(Observer):
#     def update(this, message):
#         print(f"El obvservador recibió el {message}")


# #emisor:
# subject = Subject()

# #subscriptores:
# obs1 = ConcreteObserver()
# obs2 = ConcreteObserver()

# #suscribir:
# subject.attach(obs1)
# subject.attach(obs2)

# subject.notify(">>Mensaje a todos los suscriptores<<")

#STRATEGY: define un conjunto de comportamientos en funciones que 
#           pueden ser usadas de forma intercambiable


class Strategy:

    def execute_strategy(this):
        pass

class ConcreteStrategy1(Strategy):
    def execute_strategy(this):
        return "ejecución de estrategia1"
    
class ConcreteStrategy2(Strategy):
    def execute_strategy(this):
        return "ejecución de estrategia2"
    
class Context:

    def __init__(this, strategy: Strategy):
        this._strategy = strategy

    def setNewStrategy(this,strategy:Strategy):
        this._strategy = strategy

    def execute_strategy(this):
        return this._strategy.execute_strategy()
    

contexto_uso = Context(ConcreteStrategy1())
print(f"Se está usando la estrategia 1:{contexto_uso.execute_strategy()}")

contexto_uso.setNewStrategy(ConcreteStrategy2())
print(f"Se está usando la estrategia 1:{contexto_uso.execute_strategy()}")


# 3. STRUCTURAL PATTERNS
# ADAPTER: "adapta" la interfaz de un objeto a la que pueda entender otro objeto. 
#            permite que objetos con interfaces incompatibles puedan colaborar

#interfaz destino:
class Target:
    def request(this):
        return "\ncomportamiento por defecto del target..."

#interfaz que no es compatible
class Adaptee:
    def specific_request(this):
        return "\ncontenido incompatible"

#clase adaptadora:
class Adapter(Target):
    
    def __init__(this, adaptee: Adaptee):
        this._adaptee = adaptee

    def request(this):
        #return this._adaptee.specific_request()
        return f"\ncontenido adaptado a lo que el cliente requiere:{this._adaptee.specific_request()}"



def client(target: Target):
    print(target.request())

# trabaja con el target:
new_target = Target()
client(new_target)

#creamos instancia de la clase con interfaz incompatible:
clase_adaptada = Adaptee()
print(f"\nLlamado a método no compatible {clase_adaptada.specific_request()}")

#se llama el request específico a través del adaptador:
nuevo_adapter = Adapter(clase_adaptada)
client(nuevo_adapter)

#
