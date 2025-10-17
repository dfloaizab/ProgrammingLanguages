from abc import ABC, abstractmethod

# 1. Patrones Creacionales
# (a) - Singleton
#       Permite u obliga a que se use solo una instancia de clase como único punto de acceso a una operación lógica
#       del sistema

#Clase no singleton:
class Persona():

    def __init__(self, nombre):
        self.nombre = nombre

class naive_singleton():

    #atributo de clase que almacena la instancia creada
    _instance_ = None

    #se va a lanzar error cuando se llame, para obligar a llamar al método create_instance
    def __init__(self):
        raise RuntimeError("use create_instance method instead")
    
    #Se usa este método en vez del inicializador para garantizar que se cree una sola instancia
    #classmethod garantiza que el método sea estático
    #cls se usa aquí como el self
    @classmethod 
    def create_instance(cls):
        #si no existe la instancia, la crea
        if cls._instance_  is None:
            # El método new también crea una instancia
            cls._instance_ = cls.__new__(cls)
        #retorna la instancia
        return cls._instance_
    
#Creamos objetos con el método que valida que no se creen más instancias
object1 = naive_singleton.create_instance()
object2 = naive_singleton.create_instance()

Persona1 = Persona("Diego")
Persona2 = Persona("Diana")

print( f"Son el mismo objeto?:{object1 is object2}")
print( f"Son el mismo objeto?:{Persona1 is Persona2}")

#ejercicio: usar el patrón singleton para simular el manejo de sesión de usuario de una plataforma de SW
#           con la funcionalidad de autenticación (login) (simulada) con usuario y contraseña, y (logout).


# (b) Factory Method: provee formas de crear objetos en una superclase (interfaz), pero son las subclases las que 
#                     deciden cómo crearlos

#Producto (clase de objetos) a crear 
class ITransporte(ABC):

    @abstractmethod
    def realizar_entrega(this):
        pass

#Las clases concretas quedan con la responsabilidad de definir el comportamiento específico
class Terrestre_Camion(ITransporte):
    
    def realizar_entrega(this):
        return "entrega en camión"

class Terrestre_Motocicleta(ITransporte):
    
    def realizar_entrega(this):
        return "entrega en moto"

class Aereo(ITransporte):
    def realizar_entrega(this):
        return "entrega aérea"

#Clase creadora - se le delega la creación a esta clase (tiene el "factory method")
class LogisticaEntrega(ABC):

    @abstractmethod
    def crear_metodoEntrega(self):
        pass

    #Se puede parametrizar la creación de las subclases:
    def planificarEntrega(self):
        tipoTransporte = self.crear_metodoEntrega()
        return tipoTransporte.realizar_entrega()
    
#Uso de las clases concretas:
class entregaTerrestre_Camion(LogisticaEntrega):

    def crear_metodoEntrega(self):
        return Terrestre_Camion()


class entregaTerrestre_Motocicleta(LogisticaEntrega):

    def crear_metodoEntrega(self):
        return Terrestre_Motocicleta()
    

#USO: 
entrega_c = entregaTerrestre_Camion() #La creación de la clase concreta se delega a la clase creadora
print(entrega_c.planificarEntrega())
entrega_m = entregaTerrestre_Motocicleta() 


# (c) Abstract Factory: Permite crear familias de objetos sin definir sus implementaciones concretas

# (d) Adapter (estructural): Permite que dos objetos con interfaces distintas, se puedan comunicar
#target
class Pdf_reader:
    def request(self) -> str:
        return "Lector: Lector PDF predeterminado"

#clase adaptada
class Document_word:
    def specific_request(self) -> str:
        return "parcial_2.docx"

##### La clase adapter implementa el método que adapta la clase adaptada al target
class Adapter(Pdf_reader, Document_word):

   def request(self) -> str:
        #función dummy que devuelve el formato correctto, devuelve el dato en el formato del target
        string = self.specific_request().replace(".docx", ".pdf") ###
        return f"Documento cambiado: {string}"

#client code
def client_code(lector: "Pdf_reader") -> None:
    print(lector.request())

if __name__ == "__main__":

    print("Client: Sólo trabajo con documentos pdf:")
    lector = Pdf_reader() #target
    client_code(lector) 
    print("\n")

    adaptee = Document_word() #adaptada
    print("Client: Este documento no es un pdf\n"
          "Mira, no puedo leerlo:")
    print(f"Document: {adaptee.specific_request()}")

    print("Client: Puedo cambiar el formato de este documento:")
    
    #adptador:
    adapter = Adapter()
    client_code(adapter)

# (e) Strategy (Comportamiento): Permite que un conjunto de clases puedan exponer distintas formas de implementar
#                                una funcionalidad

#Estrategia base:
class PaymentStrategy(ABC):
    @abstractmethod
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

# Patrón Estructural "Decorator"
# Permite extiende funcionalidades a un objeto o clase sin modificar el comportamiento ya existente
# Principio SOLID "O" y "S"

class Movie:
    def showMovieInfo(this):
        return this.name

class MovieDecorator:
    def __init__(this, movie: Movie):
        this.movie = movie

    def showMovieInfo(this):
        this.movie.showMovieInfo()

class showSubtitlesDecorator(MovieDecorator):    
    #función "decorada", o con extensión:
    def showMovie(this):
        return f"{MovieDecorator.showMovieInfo()} + [Subtítulos en Inglés]"

class showAudioDecorator(MovieDecorator):
    #función "decorada", o con extensión
    def showMovie(this):
        return f"{MovieDecorator.showMovieInfo()} + [Audio en Español]"





