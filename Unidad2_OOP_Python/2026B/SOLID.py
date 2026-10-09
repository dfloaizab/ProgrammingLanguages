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

class DescuentoTutor(Descuento):
    def calcular(self, valor_base):
        #Debe implementar lógica propia para cada tipo de descuento
        return super().calcular(valor_base)

class DescuentoMatriculaHonor(Descuento):
    def calcular(self, valor_base):
        #Debe implementar lógica propia para cada tipo de descuento
        return super().calcular(valor_base)


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
