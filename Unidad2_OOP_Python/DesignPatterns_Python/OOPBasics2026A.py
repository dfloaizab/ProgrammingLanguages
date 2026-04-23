from abc import ABC, abstractmethod
import math
'''
FUNDAMENTOS DE PROGRAMACIÓN ORIENTADA A OBJETOS (OOP) EN PYTHON
- ABSTRACCIÓN
- ENCAPSULAMIENTO
- HERENCIA
- POLIMORFISMO
'''

# CLASES Y OBJETOS

'''
ENCAPSULAMIENTO
'''
class cuentaAhorros:

    #Porcentaje de sobregiro que se puede realizar (10% del saldo actual)
    #(como es un atributo de clase, es válido para todas las cuentas)
    cupoSobregiro = 0.1

    '''
    Función de inicialización:
    - crea los atributos de instancia _numeroCuenta y _saldoInicial y los inicializa
    - se obliga a que los valores de entrada sean str (cadena) y float (reales)
    '''
    def __init__(self, numeroCuenta:str, saldo:float):
        self._numeroCuenta = numeroCuenta
        self._saldo = saldo
        

    #Métodos de consulta (get), por defecto son públicos
    @property
    def getSaldo(self) -> float:
        return self._saldo
    
    @property
    def getNumeroCuenta(self) -> str:
        return self._numeroCuenta
    
    # Métodos de modificación (set):
    # (por defecto son públicos)
    def establecerSaldoInicial(self, saldoInicial:float):
        if saldoInicial >= 0:
            self._saldo = saldoInicial
        else:
            raise Exception("El saldo inicial no puede ser 0 o negativo")
        
    def depositar(self, valor:float):
        if valor > 0:
            self._saldo = self._saldo + valor
        else:
            raise Exception("El valor de depósito no puede ser negativo")
        
    
            
        
    #método privado para efectuar un sobregiro
    def __efectuarSobregiro(self):
        self._saldo = self._saldo * ( 1.0 + self.cupoSobregiro)
            

    #Modificar el método para que haga sobregiro si el valor a retirar es mayor al saldo:
    #debe llamar a la función privada "__efectuarSobregiro"
    def retirar(self, valor:float):
        if valor < 0:
            raise Exception("El valor de retiro no puede ser negativo o mayor al saldo disponible")
        elif valor > 0 and valor > self._saldo:
            self._efectuarSobregiro()
            self._saldo = self._saldo - valor
        
             

miCuenta = cuentaAhorros("777888-6",1500000.0)
miCuenta.depositar(500000.0)
miCuenta.retirar(800000.0)
print(f"Saldo de la cuenta:${miCuenta.getSaldo}")



# definición de una clase
class Persona:
    # Atributo de clase (son estáticos, comunes a todos los objetos de clase)
    codigo_pais = "CO"

    #definir método de inicialización:
    #Crea una instancia de clase
    #el primer parámetro siempre hace referencia a la instancia del objeto que se está creando:
    # (podemos ponerlo "this" o "self")
    def __init__(self, documento, nombre, rol):
        self._documento = documento
        self._nombre = nombre
        self._rol = rol

    
        
'''
ABSTRACCIÓN Y HERENCIA
1. ABSTRACCIÓN: USUALMENTE CUANDO SE IMPLEMENTA O SE DEFINE UNA CLASE, LO ESENCIAL ES EXPONER QUÉ HACE Y 
                NO LOS DETALLES
2. HERENCIA
'''

#Definimos una clase abstracta "Forma" que define una forma geométrica:
class Forma(ABC):

    #Los métodos abstractos no se implementan en la clase base
    @abstractmethod
    def calcularArea(self) -> float:
        pass

    @abstractmethod
    def calcularPerimetro(self) -> float:
        pass


class Circulo(Forma):
    def __init__(self, radio:float):
        self._radio = radio
        super().__init__()

    def calcularArea(self) -> float:
        return (self._radio ** 2 * math.pi)
    
    def calcularPerimetro(self):
        return (2 * math.pi * self._radio)
        
class Rectangulo(Forma):
    
    def __init__(self, base, altura):
        super().__init__()
        self._base = base
        self._altura = altura

    def calcularArea(self) -> float:
        return self._altura * self._base
    
    def calcularPerimetro(self) -> float:
        return 2*self._base + 2 * self._altura

class Triangulo(Forma):
    
    def __init__(self, base:float, altura:float, lado1:float, lado2:float, lado3:float):
        self._base = base
        self._altura = altura
        self._lado1 = lado1
        self._lado2 = lado2
        self._lado3 = lado3

    def calcularArea(self) -> float:
        return (self._base * self._altura) / 2
    
    def calcularPerimetro(self) -> float:
        return self._lado2 + self._lado1 + self._lado3


'''
POLIMORFISMO: capacidad de que unn objeto pueda responder de forma distinta a distintos mensajes (o llamados a funciones)
              capacidad de que un objeto exhiba distintos tipos de comportamientos
              * polimorfismo por herencia (clases abstractas o interfaces)
                -> sobrecarga de funciones o de operadores
              * 
              
'''

#Clase abstracta para cualquier elemento de texto de la clase Documento
class Elemento(ABC):
    @abstractmethod
    def renderizar(this) -> str:
        pass

class Titulo(Elemento):

    def __init__(this, texto: str, nivel: int=1):
        this.texto = texto
        this.nivel = nivel

    def renderizar(this)->str:
        prefijo = "#"*this.nivel
        return f"{prefijo}{this.texto}"
    

class Parrafo(Elemento):    
    #Implementar método init y método init que solo retorne el texto
    def __init__(self, texto:str):
        self.texto = texto

    def renderizar(this)->str:
        return this.texto
    
class Documento():
    def __init__(self):
        # elementos es un atributo de instancia que es de tipo "lista de Elemento"
        # y se inicializa con []
        self.elementos: list[Elemento] = []

    # *elems indica que puede recibir un número variable de valores de clase Elemento
    def agregar(self, *elems: Elemento)->"Documento":
        self.elementos.extend(elems) # el extend es un append de varios elementos a la lista (elems puede ser un solo Elemento o varios)
        return self
    
    def renderizar(self) -> str:
        pass


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


###### PATRONES DE DISEÑO

# PATRONES CREACIONALES: Determina cómo se instancian las clases en un módulo

# 1. Singleton: Solo se puede tener una instancia de una clase

# Cómo se implementa: 

class Singleton:

    #instancia de clase:
    _instance = None

    def __new__(cls):
        #crea la instancia solo si no existe.
        #no permite crear más instancias de la misma clase
        if cls._instance is None:
            print("Se crea nueva instancia...")
            cls._instance = super().__new__(cls)
        return cls._instance
    
    #Después agregamos más métodos o implementamos como clase abstracta...


instancia1 = Singleton()
instancia2 = Singleton()


# Cómo se usa:

