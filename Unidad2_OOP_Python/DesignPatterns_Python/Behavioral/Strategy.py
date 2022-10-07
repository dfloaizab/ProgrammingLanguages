#from abc import abstractmethod
from abc  import *

class IAdapter(ABC):
    @abstractmethod
    def abstract_method1():
        pass
    
    @abstractmethod
    def abstract_method2():
        pass




class Context:
    def __init__(self, strategy):
        self._strategy = strategy


"""Clase Power: Define los atrtibutos de los ataques (El nombre y el daño que causa)"""

class Power:
    
    def __init__(self, name, damage, strategy = None):
        self.name = name
        self.damage = damage
        self.strategy = strategy

    def __str__(self):        
        return f"\nCon el poder {self.name} le has restado a tu enemigo {self.damage} de vida\n"

		

class Strategy():    
    @abstractmethod
    def Viajes(self):
        pass


class StrategyA(Strategy, Power):    
    def __init__(self) -> None:
        self.name = "ESPADA DE LA VERDAD"
        self.damage = 25000


class StrategyB(Strategy, Power):
    def __init__(self) -> None:
        self.name = "PATADA DE TARZÁN"
        self.damage = 56000

  
class StrategyC(Strategy, Power):
    def __init__(self) -> None:
        self.name = "BOLA DE FUEGO"
        self.damage = 78000



if __name__ == "__main__":
    
    poder1 = StrategyA()
    poder2 = StrategyB()
    poder3 = StrategyC()

    opc = int(input("ESCOGE UN PODER DE ATAQUE \nEspada de la verdad: (1)  \nPatada de tarzán: (2)  \nMazo de fuego: (3)"))

    if (opc == 1):
        print(Power(poder1.name, poder1.damage, strategy=StrategyA))

    elif (opc == 2):
        print(Power(poder2.name, poder2.damage, strategy=StrategyA))

    elif (opc == 3):
        print(Power(poder3.name, poder3.damage, strategy=StrategyA))

    else: 
        print("\nOPCIÓN INCORRECTA")




    


   
 
   
