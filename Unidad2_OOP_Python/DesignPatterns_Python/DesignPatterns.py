
### Septiembre 28, 2023
#### Patrón Estructural Adapter
#clase *adaptada con interfaz no compatible con el *cliente a través de un *adaptador
class Adaptee:
    def __init__(self):
        pass

    def request_trans(self):
        return "Petición adaptada a la interfaz del cliente"

#clase cliente
class Client:
    def __init__(self):
        pass

    def request(self):
        return "Petición del cliente (no compatible con la clase adaptada)"

#clase adaptadora
class Adapter(Client):
    def __init__(self, adaptee:Adaptee):
        self.adaptee = adaptee

    def request(self):
        return self.adaptee.request_trans()
    
#Ejemplo de implementación del adapter:
Pdf_reader = Client()
Word_reader = Adaptee()

print(Adapter(Word_reader).request)

######## Strategy
#clase que define una estrategia en general
class Strategy:
    def execute():
        pass

#estrategias concretas:
class ConcreteStrategyA(Strategy):
    def execute(self):
        print ("Ejecutando estrategia concreta A")

class ConcreteStrategyB(Strategy):
    def execute(self):
        print("Ejecutando estrategia concreta B")

#la clase Context es la que le permite al cliente ejecutar la estrategia correspondiente:
class Context:
    def __init__(self,strategy:Strategy):
        self.strategy = strategy

    def execute_strategy(self):
        self.strategy.execute()

#ejemplo de uso del patrón strategy (general):
#usando la estrategia A
strategyA = ConcreteStrategyA()
contexto_str1 = Context(strategyA)
result_str1 = contexto_str1.execute_strategy()

#usando la estrategia B
strategyB = ConcreteStrategyB()
contexto_str2 = Context(strategyB)
result_str2 = contexto_str2.execute_strategy()
