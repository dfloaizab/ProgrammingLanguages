from events import      Events
#Clase Publisher que se encarga de actualizar o notificar a los 
#subscriptores
class Publisher:
    #Inicializar lista de observadores
    def __init__(this):
        this._observers = []

    def addSubscriber(this, newSubscriber):
        this._observers.append(newSubscriber)

    def removeSubscriber(this, subscriber):
        this._observers.remove(subscriber)

    def notifySubscribers(this,message):
        #enviar message a todos los subscribers en la lista:
        for subscriber in this._observers :
            subscriber.update(message)

class Subscriber:

    def Update(this, message):
        pass

class SubscriberType1(Subscriber):

    def Update(this, message):
        #return super().Update(message)
        print(f"Subscriber 1 recibió mensaje {message}")

class SubscriberType2(Subscriber):

    def Update(this, message):
        print(f"")

#Método principal:
if __name__ == "__main__":

    #crear publisher:
    publisher1 = Publisher()

    #crear subscriptores u "observers"
    observer1 = SubscriberType1()
    observer2 = SubscriberType2()

    #agregar subscriptores:
    publisher1.addSubscriber(observer1)
    publisher1.addSubscriber(observer2)

    #notificar subscriptores:
    publisher1.notifySubscribers("checking my subscribers...")
