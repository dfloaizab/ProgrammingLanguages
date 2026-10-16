from abc import ABC, abstractmethod
'''
PRINCIPIOS SOLID APLICADOS A LA PROGRAMACIÓN ORIENTADA A OBJETOS
'''

# S - SINGLE RESPONSIBILITY PRINCIPLE (SRP)
# O - OPEN / CLOSED (OPEN FOR EXTENSION / CLOSED FOR MODIFICATION) (OCP)

# aplicar estos dos ejemplos a la implementación de un módulo que pueda liquidar el valor a pagar de matrícula
# con distintos tipos de desccuento.

# PRIMERA VERSIÓN:


class Estudiante:
    def __init__(self, nombre, codigo, tipo_descuento):
        self.nombre = nombre
        self.tipo_descuento = tipo_descuento

    def liquidar_matricula(self, valor_base):

        pass

# MEJORAS:
# 1a Mejora
# 1. SEPARAR RESPONSABILIDADES


# class Estudiante:
#     pass

# class LiquidacionMatricula:
#     pass

# 2a. Mejora:
# 2. PERMITIR EXTENSIÓN, PERO NO MODIFICACIÓN
class Descuento(ABC):
    @abstractmethod
    def calcular(self, valor_base):
        pass

class ValidacionElegibilidad(ABC):
    @abstractmethod
    def validar_elegible(self, estudiante:Estudiante):
        pass


class DescuentoTutor(Descuento, ValidacionElegibilidad):
    def calcular(self, valor_base):
        #Debe implementar lógica propia para cada tipo de descuento
        return super().calcular(valor_base)

class DescuentoHijo(Descuento, ValidacionElegibilidad):
    def calcular(self, valor_base):
        #Debe implementar lógica propia para cada tipo de descuento
        return super().calcular(valor_base)

class DescuentoMatriculaHonor(Descuento, ValidacionElegibilidad):
    def calcular(self, valor_base):
        #Debe implementar lógica propia para cada tipo de descuento
        return super().calcular(valor_base)

class DescuentoTerremoto(Descuento):
    pass


class Estudiante:
    def __init__(self, nombre, codigo, descuento:Descuento):
        self.nombre = nombre
        self.codigo = codigo
        self.descuento = descuento

class LiquidacionMatricula:
    def liquidar(self, estudiante:Estudiante, valor_base):
        #Qué pasa si se pueden acumular descuentos?
        #Qué pasa cuando no hay descuento?
        pass

# LSP (Liskov Substitution Principle)

descuentos = [
    DescuentoMatriculaHonor(), 
    DescuentoTutor(),
    DescuentoHijo()
]

# Se podría iterar por la lista de descuentos y aplicarlos de forma acumulativa, sin problemas


# ISP (Interface Seggregation Principle: ninguna clase debe depender de métodos que no usa)
   

# ¿QUÉ PASA SI NO TODOS LOS DESCUENTO DEBEN VALIDAR ELEGIBILIDAD?
# SEPARO LA VALIDACIÓN DE LA ELEGIBILIDAD EN OTRA CLASE ABSTRACTA  O INTERFAZ:


# Dependency Inversion Principle DIP: Un módulo de alto nivel solo debe depender de abstracciones


# Sistema de notificaciones:
# NO APLIICA BIEN EL PRINCIPIO DIP

class EmailSender:
    def sendEmail(self, message):
        print(f"Enviando notificación{message}")

class SMSSender:
    pass

class WhatsappSender:
    pass


class NotificationService:
    def __init__(self):
        #Ya estoy "amarrando" la funcionalidad a una implementación concreta
        self.sender = EmailSender

    def sendNotification(self, message):
        self.snder.sendEmail(message)


#CÓMO LO SOLUCIONAMOS:
#creamos una interfaz que define el contrato de las notificaciones
class INotificationSender(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailSender(INotificationService):
    def send(self, message):
        print(f"Enviando notificación:{message}, por email")

class SMSSender(INotificationService):
    def send(self, message):
        print(f"Enviando notificación:{message}, por email")     

class WhatsappSender(INotificationService):
    def send(self, message):
        print(f"Enviando notificación:{message}, por email")

#ESTA ES LA CLASE DE ALTO NIVEL QUE DEPENDE DE LA ABSTRACCIÓN (LA INTERFAZ):
class NotificationService:
    #Aquí aplicamos inyección de dependencias:
    def __init__(self, sender:INotificationSender):
        self.sender = sender

    def sendNotification(self, message):
        self.sender.send(message)

sender_via_sms = SMSSender()
myNotificationService = NotificationService(sender_via_sms)
myNotificationService.send("Hola! Ya llegó el pedido")
        


