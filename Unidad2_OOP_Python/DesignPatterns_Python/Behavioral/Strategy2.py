
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
