#DESIGN PATTERNS

#CREATIONAL PATTERNS: 
#cómo se crean los objetos
#1. Singleton: permite que se cree solo una instancia de objeto

from abc import ABC, abstractmethod


class NoSingleton:
    pass

#MI MEJOR IMPLEMENTACIÓN DE SINGLETON HASTA AHORA (ABRIL 3, 2025):
class Singleton:

    #atributo de clase que guarda una referencia a la instancia
    #una vez se cree
    _instance = None

    def __new__(cls,user,password):
        if cls._instance is None:
            #crea una sola instancia de clase si esta no existe:
            cls._instance = super(Singleton, cls).__new__(cls)
            #creo los dos nuevos atributos del objeto, los inicializo una sola vez
            cls._instance.__setattr__("user",user)
            cls._instance.__setattr__("password",password)
        return cls._instance               

    def getUser(this):
        return this.user
    
    def getPassword(this):
        return this.password   


#Ejemplo con un objeto que maneja sesion:

sesion1 = Singleton("Diego","abcd1234")
sesion2 = Singleton("Diego2","abcd456")
print(f"{sesion1.getUser()}")
print(f"{sesion2.getUser()}")

#EJERCICIOS: CREE UN LOGGER O BITACORA DE EVENTOS QUE USE EL PATRÓN SINGLETON

# objeto1 = Singleton()
# objeto2 = Singleton()

# objeto3 = NoSingleton()
# objeto4 = NoSingleton()

#Objeto 1 y Objeto 2 son la misma instancia de clase, es decir, son el mismo objeto
# print(f"Objeto 1 es objeto 2?: {objeto1 is objeto2}")
# print(f"El objeto 1 es: {objeto1}")
# print(f"El objeto2 2 es:{objeto2}")

# print(f"Objeto 1 es objeto 2?: {objeto3 is objeto4}")
# print(f"El objeto 3 es: {objeto3}")
# print(f"El objeto2 4 es:{objeto4}")



#Ejercicio: cómo usarlo para guardar información de una sesión de usuario? (username y password)


#2. Abstract Factory:
# permite crear familias de objetos relacionados sin especificar las subclases
#Ejemplo: abstract factory para crear elementos de GUI:
# class Button(ABC):
#     @abstractmethod
#     def click(this):
#         pass

# class Menu(ABC):
#     @abstractmethod
#     def Open(this):
#         pass

# #implementación de las clases concretas (Windows):
# class WindowsUIButton(Button):
#     def click(this):
#         return "Me comporto como un botón de windows"
    
# class WindowsUIMenu(Menu):
#     def Open(this):
#         return "Me comporto como un menu de windows"


# class LinuxUIButton(Button):
#     def click(this):
#         return "Me comporto como un botón de Linux"
    
# class LinuxUIMenu(Menu):
#     def Open(this):
#         return "Me comporto como un menu de Linux"


# #CREAR UNA SOLA ABSTRACT FACTORY:
# #ES LA QUE DEFINE CÓMO SE CREAN LAS SUBCLASES
# class GUIAbstractFactory(ABC):

#     @abstractmethod
#     def createButton(this) -> Button:
#         pass

#     @abstractmethod
#     def createMenu(this) -> Button:
#         pass

# #SE CREA UNA "CONCRETE FACTORY" PARA CADA CASO DE USO:
# class WindowsFactory(GUIAbstractFactory):
#     def createButton(this) -> Button:
#         return WindowsUIButton()
    
#     def createMenu(this) -> Menu:
#         return WindowsUIMenu()
    
# class LinuxFactory(GUIAbstractFactory):
#     def createButton() -> Button:
#         return LinuxUIButton()
    
#     def createMenu() -> Menu:
#         return LinuxUIMenu()
    

# #CLASE CLIENTE CONSUME EL ABSTRACT FACTORY
# def GUI_FactoryClient(os_type: str) -> GUIAbstractFactory:
#     if os_type=="Windows":
#         return WindowsFactory
    
#     elif os_type=="Linux":
#         return LinuxFactory
#     else:
#         raise ValueError("Sistema Operativo no válido")
    
# #Uso del patrón Abstract Factory:
# factory = GUI_FactoryClient("Windows")  # Cambia a "Windows" para otra interfaz
# button = factory.createButton()
# menu = factory.createMenu()

#EJERCICIO: Abstract Factory para crear enemigos en un videojuego: easy, middle, nightmare


#STRUCTURAL
#cómo se relacionan, de forma estructura
#3. Adapter

#es un patrón que permite adaptar la comunicación entre objetos que tienen interfaces distintas
#Ejemplo:

#Clase incompatible que necesitamos adaptar:
class CelsiusTemperatureSensor:

    def __init__(this,temp):
        this.temp = temp

    def getTempCelsius(this):
        return this.temp
    
class FahrenheitTemperatureSensor:
    def getTempFahr(this):
        pass

#CLASE ADAPTADOR ENTRE LAS DOS CLASES:
#Se recibe como parámetro la clase A LA cual se va a adaptar la información de 
# la clase incompatible
class TemperatureAdapter(FahrenheitTemperatureSensor):

    #Se inicializa con la clase incompatible
    def __init__(this, sensor):
        this.sensor = sensor

    #FUNCION QUE ADAPTA DESDE LA CLASE NO COMPATIBLE PARA QUE EL CLIENTE LA PUEDA CONSUMIR
    def getTempFahr(this):
        #Código que adapta desde la clase no compatible:
        celsius = this.sensor.getTempCelsius()

        return celsius * (9/5) + 32
    
#EJEMPLO DE USO DE LA CLASE ADAPTADORA:
sensor = CelsiusTemperatureSensor(23)
adaptador = TemperatureAdapter(sensor)
print(f"La temperatura convertida es {adaptador.getTempFahr()} °F")


#4. Decorator
#Permite agregar funcionalidades o modifica funcionalidad de forma dinámica a un objeto sin modificar su estructura
class Text:
    def __init__(this,text):
        this.text = text

    def render(this) -> str:
        return this.text
    
#decorador base:
class BaseDecorator:
    def __init__(this, component):
        this._component = component

    def render(this):
        return this._component.render()
    
#decoradores concretos
class BoldDecorator(BaseDecorator):    
    def render(this):
        return f"<b>{super().render()}</b>"

class ItalicDecorator(BaseDecorator):
    def render(this):
        return f"<i>{super().render()}</i>"

class UnderlineDecorator(BaseDecorator):
    def render(this):
        return f"<u>{super().render()}</u>"
    
#Uso:
texto = Text("Lenguajes de Programación 2025A")
decorado = UnderlineDecorator(BoldDecorator(ItalicDecorator(texto)))
print(decorado.render())



#BEHAVIORAL PATTERNS
#cómo se comportan entre ellos, y en el sistema. identifica patrones de
#comunicación entre objetos.

#5. Strategy

#Estrategia base:
class PaymentStrategy():
    def pay(this,value):
        pass

#Estrategias concretas:
class CreditCard(PaymentStrategy):
    def pay(this, value):
        print(f"payment made by credit card. Amount:{value}")

class Paypal(PaymentStrategy):
    def pay(this,value):
        print(f"payment made by Paypal. Amount:{value}")

class CryptoCurrenct(PaymentStrategy):
    def pay(this,value):
        print(f"payment made by CryptoCurrency. Amount:{value}")


#contexto uso:
class OnlineStore:

    def __init__(this,strategy:PaymentStrategy):
        this._strategy = strategy

    def checkout(this, value):
        this._strategy.pay(value)

#Uso:
OnlineStore_Session = OnlineStore(CreditCard)
OnlineStore_Session.checkout(150)

OnlineStore_Session._strategy = Paypal
OnlineStore_Session.checkout(230)

#DIFERENCIA ENTRE STRATEGY Y DECORATOR:
# --->   STRATEGY  PERMITE ELEGIR UNA FORMA DE SOLUCIONAR UN PROBLEMA (ELIGE UN ALGORITMO)
# --->   DECORATOR AÑADE FUNCIONALIDADES A UN OBJETO EXISTENTE SIN MODIFICARLO

#6. Command
# Encapsula una petición de una funcionalidad como un objeto, permitiendo parametrizar
# las solicitudes de acuerdo a los clientes, y manejar peticiones como objetos (historia, cola de peticiones, etc)

# Receptor del comando:
class Light:

    def on(this):
        print("Light is on")

    def off(this):
        print("Light is off")

#Comando base:
class Command:
    def exec_command(this):
        pass

#Comandos concretos:
class TurnLightOn(Command):
    # cada comando concreto se instancia determinando también qué objeto recibe el comando
    # y la operación a ejecutar
    def __init__(this, light:Light):
        this._light = light

    def exec_command(this):
        this._light.on()

class TurnLightOff(Command):
    def __init__(this, light:Light):
        this._light = light

    def exec_command(this):
        this._light.off()

#Invocador:
class LightRemoteControl:

    def __init__(this):
        this._command = None

    def setCommand(this, command: Command):
        this._command = command

    def pushButton(this):
        this._command.exec_command()

#Uso:
bedroomLight = Light()
turnOn = TurnLightOn(bedroomLight)
turnOff = TurnLightOff(bedroomLight)

remoteControl = LightRemoteControl()
remoteControl.setCommand(turnOn)
remoteControl.pushButton()

remoteControl.setCommand(turnOff)
remoteControl.pushButton()
