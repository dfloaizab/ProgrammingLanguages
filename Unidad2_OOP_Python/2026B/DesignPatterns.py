from abc import ABC, abstractmethod
from dataclasses import dataclass, field

@dataclass
class Pedido:
    cliente: str
    items: list = field(default_factory=list)   # tuplas (nombre, precio, cantidad)
    direccion: str | None = None
    cupon: str | None = None
    notas: str = ""

    @property
    def total(self) -> float:
        return sum(precio * cant for _, precio, cant in self.items)

# 1. SINGLETON: permite solo una instancia de una clase

class Configuracion:

    _INSTANCIA = None
    def __new__(cls):
        if cls._INSTANCIA is None:
            #Usamos un método de instanciación genérico de objetos en Python:
            cls._INSTANCIA = super().__new__(cls)
            #Definimos atributos de instancia:
            cls._INSTANCIA.moneda = "COP"
            cls._INSTANCIA.IVA = 0.19
        return cls._INSTANCIA

    def cambiarIVA(this, nuevoIva):
        this._INSTANCIA.IVA = nuevoIva

    def consultarIVA(this):
        return this._INSTANCIA.IVA

    #Implementar un método que cambie el valor de un atributo (IVA):

    #Implementar un método que consulte el valor de un atributo (IVA):

#Realizamos una prueba:
Config_cliente1 = Configuracion()
Config_cliente2 = Configuracion()

Config_cliente2.cambiarIVA(18)
Config_cliente1.cambiarIVA(17)

#Cómo sabemos si son el mismo objeto?
print(Config_cliente1 is Config_cliente2)

#Qué valor imprime?
print(f"El iva quedó en: {Config_cliente2.consultarIVA()}")

# 2. FACTORY METHOD
class Notificador(ABC):
    @abstractmethod
    def Enviar(this, destino: str, mensaje: str) -> None:
        pass

class NotificacionEmail(Notificador):
    def Enviar(self, destino, mensaje):
        print(f"Se le envío el email {mensaje} a {destino}") 

class NotificacionSMS:
    pass

#PUEDO AGREGAR NUEVOS CANALES DE NOTIFICACIÓN EN EL REGISTRO
_CANALES_NOTIF = {"email":NotificacionEmail, "SMS":NotificacionSMS}

#CLASE FACTORY
class CrearNotificador():
    # FactoryMethod
    def crear_notificador(canal:str) -> Notificador:
        try:
            #retornamos instancia de la clase correspondiente:
            return _CANALES_NOTIF[canal]()
        except KeyError:
            raise ValueError("El valor no existe")

#CÓMO USAR EL FACTORY METHOD?
CrearNotificador().crear_notificador("email").Enviar("dfloaiza@gmail.com","Pedido en camino")

# 3. Builder: permite construir un objeto con partes de los atributos de la clase: parte por parte
class PedidoBuilder:
    def __init__(self, cliente: str):
        self._pedido = Pedido(cliente)

    def agregar_item(self, nombre, precio, cantidad=1):
        self._pedido.items.append((nombre, precio, cantidad))
        return self

    def con_direccion(self, direccion):
        self._pedido.direccion = direccion
        return self

    def con_cupon(self, cupon):
        self._pedido.cupon = cupon
        return self

    def construir(self) -> Pedido:
        if not self._pedido.items:
            raise ValueError("Un pedido necesita al menos un ítem")
        return self._pedido

pedido = (PedidoBuilder("Ana")
          .agregar_item("Teclado", 40.0, 1)
          .agregar_item("Mouse", 15.0, 2)
          .con_direccion("Calle 5 #10-20")
          .construir())
print(pedido.total)  # 70.0
