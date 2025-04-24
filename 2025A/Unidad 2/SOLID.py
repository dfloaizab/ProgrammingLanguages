
from abc import ABC, abstractmethod

#SOLID PRINCIPLES
#1.S- SINGLE RESPONSIBILITY
#ESTA CLASE TIENE LA RESPONSABILIDAD ÚNICA DE GENERAR UN REPORTE CON BASE EN UNOS DATOS:
class ReportGenerator:
    
    #metodo de instanciación:
    #el self es como el "this", hace referencia a la instancia que se está creando
    def __init__(this,data):
        #self.data es un atributo de instancia:
        this.data = data

    #todos los métodos donde se use un atributo de instancia, debe tener como primer parámetro,    
    # una referencia a la instancia
    def generateReport(this):
        return f"Generando reporte:{this.data}"

#ESTA CLASE TIENE LA RESPONSABILIDAD ÚNICA DE GUARDAR UN REPORTE:
class ReportSaver:
    
    def saveToFile(this, report, filename):
        with  open(filename,"w") as reportFile:
            reportFile.write(report)


#ESTA CLASE TENDRÍA LA RESPONSABILIDAD ÚNICA DE IMPRIMIR EL REPORTE:
class ReportPrinter:
    pass


#¿CÓMO SE USAN?
reportData = ReportGenerator("Estos son los datos del reporte: sjdfjsdhjkashkashfkasfkjsfh").generateReport()
reportSaver = ReportSaver()
reportSaver.saveToFile(reportData,"nuevoReporte.txt")

#2. O- OPEN FOR EXTENSION / CLOSED FOR MODIFICATION

#clase abstracta Discount:
class Discount(ABC):

    @abstractmethod
    def applyDiscount(this,price):
        #se pone la instrucción "pass" porque una clase abstracta no implementa funcionalidades, 
        #lo hacen las clases hijas:
        pass

#Aplica un descuento del 20%:
class FrequentClientDiscount(Discount):
    def applyDiscount(this, price):
        this.discount = 0.8
        return super().applyDiscount(price*this.discount)
    

class VipDiscount(Discount):
    def applyDiscount(this, price):
        this.discount = 0.5
        return super().applyDiscount(price*this.discount)
    
#3. L - Liskov substitution principle: una clase derivada puede sustituir a una clase base sin afectar el comportamiento del sistema

# NO APLICA LSP: No se puede usar un square como un rectangle:

class Rectangle:
    
    def __init__(this,width, height):
        this.width = width
        this.height = height

    def calc_area(this):
        return this.width * this.height
    

class Square(Rectangle):

    def __init__(this, side):
        super.__init__(side, side)

    def setWidth(this, width): #VULNERA LSP
        this.width = width
        this.height = width

    def setHeight(this,height): #VULNERA LSP
        this.height = height
        this.width = height
    
# APLICA LSP:
class Shape(ABC):

    @abstractmethod
    #La implementación se le deja a las subclases:
    def calc_area(this):
        pass


class Rectangle(Shape):
    
    def __init__(this,width, height):
        this.width = width
        this.height = height

    def calc_area(this):
        return this.width * this.height


class Square(Shape):
    
    def __init__(this,side):
        this.side
        

    def calc_area(this):
        return this.side ** 2


# class Rectangle:

#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
    
#     def set_width(self, width):
#         self.width = width

#     def set_height(self, height):
#         self.height = height
    
#     def area(self):
#         return self.width * self.height
    
# class Square(Rectangle):

#     #VIOLA EL PRINCIPIO LSP:
#     def set_width(self, width):
#         self.height = width
#         self.width = width
    
#     def set_height(self, height):
#         self.height = height
#         self.width = height

# #no se puede usar Square en reemplazo de Rectangle, porque los métodos son distintos a los de la clase base:
# #la solución es implememtar una clase abstracta Shape, de la cual Square y Rectangle, hereden

# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass


# class Rectangle(Shape):

#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
    
#     def set_width(self, width):
#         self.width = width

#     def set_height(self, height):
#         self.height = height
    
#     def area(self):
#         return self.width * self.height
    
# def Square(Shape):

#     def __init__(this,side):
#         this.side = side

#     def area(this):
#         return this.side ** 2
    

#POR QUÉ RESPETA EL PRINCIPIO LSP?

# I - INTERFACE SEGREGATION PRINCIPLE (relación con el principip S, SRP, Single Responsibility)
# Clientes no deben depender de métodos que no usan
#tipos de impresion

#no aplica ISP

class Printer(ABC):

    @abstractmethod
    def print(this, document):
        pass

    @abstractmethod
    def fax(this, document):
        pass

    @abstractmethod
    def scan(this, document):
        pass

#Impresora moderna:
class HQPrinter(Printer):
    
    def print(this, document):
        return super().print(document)
    
    def scan(this, document):
        return super().scan(document)
    
    def fax(this, document): #VULNERA EL PRINCIPIO ISP
        raise NotImplementedError("Las impresoras modernas no envían fax")

#Impresora antigua, de baja calidad
class LQPrinter(Printer):
    
    def print(this, document):
        return super().print(document)
    
    def scan(this, document):
        return super().scan(document)
    
    def fax(this, document):
        return super().fax(document)


# si aplica ISP, solución: Segregar 

#Segrego las funcionalidades en dos interfaces o clases abstractas separadas, de 
#tal forma que las subclases solo implementen lo que vaya a usar el cliente
class Printer(ABC):

    @abstractmethod
    def print(this, document):
        pass

    @abstractmethod
    def scan(this, document):
        pass

class Fax(ABC):
    @abstractmethod
    def Fax(this, document):
        pass


class LQPrinter(Printer, Fax):

    def print(this, document):
        return super().print(document)
    
    def scan(this, document):
        return super().scan(document)
    
    def Fax(this, document):
        return super().Fax(document)
    
class HQPrinter(Printer):

    def print(this, document):
        return super().print(document)
    
    def scan(this, document):
        return super().scan(document)


# D. Dependency Inversion Principle
# 


#MALA APLICACIÓN DEL PRINCIPIO: Hay alto acoplamiento entra las dos clases
class FrontEnd:

    def __init__(this, back_end):
        this.back_end = back_end


    def show_data(this):
        data = this.back_end.getData()
        print(f"Mostrando info en el front end:{data}")

class BackEnd:

    def getData():
        return "Esta info viene de la base de datos..."
    


#Corrección: se separa el back end para segregar funcionalidades:
class FrontEnd:

    def __init__(this, dataSource):
        this.dataSource = dataSource


    def show_data(this):
        data = this.dataSource.getData()
        print(f"Mostrando info en el front end:{data}")
    

class DataSource(ABC):

    @abstractmethod
    def getData(this):
        pass


class SQLDataBase(DataSource):

    def getData(this):
        return "Datos de una base de datos relacional"
    

class DocumentDataBase(DataSource):

    def getData(this):
        return "datos de una base de datos documental"
    
class API(DataSource):

    def getData(this):
        return "Datos que vienen de una API"
  
