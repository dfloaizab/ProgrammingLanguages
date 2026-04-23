from abc import ABC, abstractmethod
#PATRONES CREACIONALES
#1. SINGLETON
#2. Abstract Factory
'''
Proporciona una interfaz para crear familias de objetos relacionados o interdependientes 
sin especificar clases concretas
Ejemplo: UI para distintos sistemas operativos:
ESTRUCTURA:
- AbstractFactory: crea las clases concretas
- ConcreteFactoryA, ConcreteFactoryB, ....
- AbstractProductA, AbstractProductB, ...
- ConcreteProductA, ConcreteProductB, ...
- Client
'''

#ProductosAbstractos: familia de productos:
class Button(ABC):
    @abstractmethod
    def render(this): pass

class Checkbox(ABC):
    @abstractmethod
    def render(this): pass

#ProductosConcretos: 
class WindowsButton(Button):
    def render(this):
        return "Boton estilo Windows"

class MacButton(Button):
    def render(this):
        return "Boton estilo Mac"

class WindowsCheckbox(Checkbox):
    def render(this):
        return "checkbox estilo windos"

#Fábrica Abstracta (crea cualquier familia de objetos):
class UIFactory(ABC):
    @abstractmethod
    def createButton(this):
        pass

    def createCheckbox(this):
        pass

#Fábricas concretas:
class WindowsFactory(UIFactory):
    def createButton(this):
        return WindowsButton()

    def createCheckBox(this):
        return WindowsCheckbox()

class MacFactory(UIFactory):
    def createButton(this):
        return MacButton()

    def createCheckbox
        return MacCheckbox()

#Ejemplo de uso (con un cliente):
# El cliente no conoce clases concretas, solo la fábrica abstracta
# De cierto modo, usa Inversión de Dependencias (solo depende de abstracciones)
def renderUI(factory: UIFactory):
    btn = factory.createButton()
    chk = factory.createCheckbox()
    btn.render()
    chk.render()

# PATRONES ESTRUCTURALES
# 1. DECORATOR: añade responsabilidades o características a una clase sin modificarla

# Ejemplo, texto con formato

#Clase abstracta que modela la entidad base a decorar:
class Texto(ABC):
    @abstractmethod
    def render(this) -> str:
        pass

# Clases base a decorar
class TextoPlano(Texto):
    def __init__(this, contenido: str):
        this.contenido = contenido

    def render(this) -> str:
        return this.contenido #Retorna el mismo texto plano

# decorador abstracto
class DecoradorTexto(Texto):
    def __init__(this, texto: Texto):
        this.texto = texto

# decorador concreto
class Negrita(DecoradorTexto):
    def render(this) -> str:
        return f"<b>{this.texto.render()}</b>"

class Cursiva(DecoradorTexto):
    def render(this) -> str:
        return f"<i>{this.texto.render()}</i>"

textoPlano = TextoPlano("texto de prueba del decorator")
textoFormateado = Negrita(Cursiva(textoPlano))
print(textoFormateado)

# PATRONES DE COMPORTAMIENTO

# 1. STRATEGY:

# 2. OBSERVER:
# beneficios: baja el acoplamiento entre objetos, permite crear sistemas reactivos
# contras: no es posible seguir la traza de notificaciones, puede crear cascada de notificaciones
class Observer(ABC):
    @abstractmethod
    def update(this, data):
        pass

#clase que debe recibir las notificaciones:
class Usuario(Observer):
    def update(this, data):
        # Se puede crear una colección de notificaciones
        this.data = data
        print(f"Notificación recibida:{this.data}")

# El sujeto que sufre los cambios y debe notificar
class Sujeto:
    def __init__(this):
        this.observers = []

    def suscribir(this, o: Observer):
        this.observers.append(o)

    def notificar(this, data):
        for o in this.observers:
            o.update(data)

# Ejemplo: alertas para inversiones en acciones:

class Accion(Sujeto):
    def __init__(this):
        pass

    # Método que puede generar una notificación
    def set_precio(this, p):
        pass

class Inversor(Observer):
    def update(this, data):
        pass


# Strategy: define familias de algoritmos o estrategias de solución de problemas 
# Ventaja: evita estructuras condicionales complejas para la lógica de ciertos programas que pueden 
#           tener soluciones variadas a ciertos problemas
class EstrategiaPagos(ABC):
    @abstractmethod 
    def pagar(this, monto):
        pass


class Tarjeta(EstrategiaPagos):
    def pagar(this, monto):
        return f"Pago con tarjeta de {monto}"

class PSE(EstrategiaPagos):
    return f"Pago con PSE de {monto}"

class Contexto:
    def __init__(this, estrategia: EstrategiaPago):
        this.estrategia = estrategia

    def ejecutarPago(this, monto):
        return this.estrategia.pagar(monto)

