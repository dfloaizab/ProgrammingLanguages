from abc import ABC, abstractmethod

class Strategy(ABC):

   @abstractmethod
   def method1(self):
      pass
   
   @abstractmethod
   def method2(self):
      pass
   

class ConcreteStrategy1(Strategy):
   def method1(self):
      #implementación del método que corresponde a la estrategia 1
      pass
   

class ConcreteStrategy2(Strategy):
   def method1(self):
      pass
   

class Context():
   
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = Strategy

    #GET: devuelve referencia al objeto que representa la estrategia usada
    @property
    def strategy(self) -> Strategy:
       return self._strategy
    
    #SET
    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
       self._strategy = strategy

    #El contexto delega a la estrategia el método a utilizar.
    def entryPoint(self) ->None:
       
       self.strategy.method1()


#método principal del módulo:
if __name__ == "__main__":
   
    estrategia = input("Elija la estrategia a usar (1, 2)")

    if estrategia == "1":
        context = Context(ConcreteStrategy1())
    else:
       context = Context(ConcreteStrategy2())

    context.entryPoint()


   


