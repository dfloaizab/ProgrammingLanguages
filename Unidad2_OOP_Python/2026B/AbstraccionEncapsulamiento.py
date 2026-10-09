
from abc import ABC, abstractmethod

#----------------------- (1) ABSTRACCIÓN ---------------------------
# INTRODUCCIÓN AL ABSTRACCIÓN:
#Clase abstracta que define un método de pago:
class MetodoPago(ABC):
    @abstractmethod
    #los métodos que empiecen con una referencia a this, o self, son
    #métodos de instancia
    def procesar_pago(this, monto:float):
        pass


#Clases concretas: métodos de pago, específicos:
# Se implementan los métodos abstractos
class TarjetaCredito(MetodoPago):
    def procesar_pago(this, monto):
        #return super().procesar_pago(monto)
        print("Procesando pago con tarjeta de crédito por el monto: ", monto)

class PagoMercadoPago(MetodoPago):
    def procesar_pago(this, monto):
        print("Procesando pago Mercado Pago por: ", monto)

#------------------- (2) ENCAPSULAMIENTO ---------------------------
# INTRODUCCIÓN AL ENCAPSULAMIENTO:
class CuentaBancaria:

    #El primer parámetro del método init hace referencia a la instancia del objeto:
    def __init__(this, titular:str, numero:int, saldo_inicial:float):
        #Todos los atributos de "this", "self", son atributos de instancia:
        this.titular = titular
        this.numero = numero
        this._saldo = saldo_inicial

    def obtener_saldo(this):
        return this.saldo

    def _hacer_deposito(this, valor:float):
        if valor > 0:
            this._saldo +=  valor

    def _hacer_retiro(this, valor:float):
        if valor > 0 and this._saldo >= valor:
            this._saldo -= valor

#----------------- (3) HERENCIA -----------------------------

class Empleado(ABC):
    def __init__(this, nombre:str, id:str, salario_base:float):
         #completar
         pass

    @abstractmethod
    def liquidar_pago(this):
         pass

class Administrativo(Empleado):
    #El empleado administrativo tiene un atributo adicional: bono:
    def __init__(this, nombre:str, id:str, salario_base:float, bono:float):
        pass

    def liquidar_pago(this):
        #Liquidar pago con el bono:
        return super().liquidar_pago()


class Docente(Empleado):

   def __init__(this, nombre:str, id:str, salario_base:float):
       pass

   def liquidar_pago(this):
       #Liquidar pago sin el bono:
       return super().liquidar_pago()



#--------- EJERCICIO PARA LA PRÓXIMA SEMANA : ------------------
# SISTEMA DE GESTIÓN DE UNA BIBLIOTECA:
# A) LIBROS FÍSICOS
# B) E-BOOKS
# C) AUDIOLIBROS

# 1. ABSTRACCIÓN: QUÉ CLASE ABSTRACTA MODELA EL RECURSO BIBLIOGRÁFICO (título, autor, año)
# 2. HERENCIA: CADA TIPO DE PUBLICACIÓN TIENE SUS ATRIBUTOS PROPIOS
# 3. CADA PUBLICACIÓN TIENE SUS ATRIBUTOS PRIVADOS: USUARIO EN PRÉSTAMO, FECHA DE ENTREGA
# 4. POLIMORFISMO: CADA TIPO DE PUBLICACIÓN TIENE SU PROPIA FORMA DE GESTIONAR PRÉSTAMO
