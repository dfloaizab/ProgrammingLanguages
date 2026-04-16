from abc import ABC, abstractmethod
import math
'''
FUNDAMENTOS DE PROGRAMACIÓN ORIENTADA A OBJETOS (OOP) EN PYTHON
'''

'''
PRINCIPIOS SOLID
S - SRP (Single Responsibility Principle): Una clase debe tener solo un papel dentro del sistema,
    y debe ser un uníco punto de cambio
'''
# Ejemplo sin SRP: Una clase que maneje pedidos de productos:
# - Cálculo de total
# - Persistencia en base de datos
# - Envío de notificación (email y SMS)

# Se vulnera el principio SRP: la clase cumple tres tareas distintas
class Pedidos:

    def __init__(self, idPedido:int, items):
        self.idPedido = idPedido
        self.items = items

    def calcularTotal(self):
        pass

    def guardar_en_bd(self):
        pass

    def notificar(self):
        pass

# Aplicando SRP: separamos responsabilidades, en 3 clases distintas

class Pedido:
    pass

class PersistenciaPedido:
    pass

class NotificacionPedido:
    pass


'''
O: OCP (Open-Closed Principle) - Prinicipio Abierto-Cerrado: En un buen diseño, las clases deben estar abiertas para extensión
                                 pero cerradas para modificación
'''
class PersistenciaPedido:
    def __init__(self):
        pass

    def persistenciaSQL(self):
        pass

    def persistenciaNoSQL(self):
        pass

    def persistenciaArchivoPlano(self):
        pass


'''
L: Liskov Substitution Principle (LSP): Una subclase debe poder reeemplazar a su clase padre sin vulnerar el diseño ni la implementación
'''

#superclase sin aplicar LSP
class Rectangulo_sinLSP(ABC):

    def __init__(this, ancho, alto):
        this.ancho = ancho
        this.alto = alto

class Cuadrado_sinLSP(Rectangulo_sinLSP):
    def __init__(this, lado):
        super().__init__(lado, lado)

    #creamos un setter que obliga a cambiar ambos atributos en la superclase:
    @Rectangulo_sinLSP.ancho.setter
    def ancho(this, val):
        this.ancho = this.alto

#SOLUCION: crear una jerarquía de figuras donde se generelicen los getters y los setters:

class Forma_LSP(ABC):

    #Los métodos abstractos no se implementan en la clase base
    @abstractmethod
    def calcularArea(self) -> float:
        pass

    @abstractmethod
    def calcularPerimetro(self) -> float:
        pass

class Rectangulo(Forma_LSP):
    
    def __init__(self, base, altura):
        super().__init__()
        self._base = base
        self._altura = altura

    def calcularArea(self) -> float:
        return self._altura * self._base
    
    def calcularPerimetro(self) -> float:
        return 2*self._base + 2 * self._altura

class Cuadrado_LSP(Forma_LSP):
    pass





'''
I: Interface Segregation Principle : Ninguna clase debe depender de métodos que no usa: deben separarse bien las funcionalidades
    abstractas en las interfaces que se necesitan.
'''

class PaymentMethod(ABC):

    def __init__(this, userId):
        this.userId = userId

    @abstractmethod
    def generateToken(this, userId) -> str:
        pass

    @abstractmethod
    def validateToken(this, userId, token) -> bool:
        pass

    @abstractmethod
    def registerPayment(this, userId, token) -> bool:
        pass


class PSE(PaymentMethod):
    pass


class CreditCard(PaymentMethod):
    pass


'''
D: Dependency Inversion: módulos de alto nivel no deben depender de módulos de bajo nivel
'''
#Vulnera el principio de Inversión de Dependencias:
class UserServices_Service_NoDI:
    def __init__(this):
        this.db = MySQLConnection()
        this.email = GmailSMTP()
        this.messages = RabbitMQ()


#Aplicacmos inyección de dependencias para que el módulo no dependa de otros módulos de bajo nivel

class DataBaseServer(ABC):
    pass

class MySQLConnection(DataBaseServer):
    pass


class UserServices_Service_SiDI:
    def __init__(this, db: DataBaseServer, email:EmailServer, messages:QueueService):
        this.db = db
        this.email = email
        this.messages = messages
