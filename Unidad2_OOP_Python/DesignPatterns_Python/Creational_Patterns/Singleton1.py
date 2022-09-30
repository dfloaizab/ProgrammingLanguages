#esta implementación "naive" reemplaza el método constructor por defecto por un
#método propio de instanciación
class naive_singleton():
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
            cls._instance_ = cls.__new__(cls)
        #retorna la instancia
        return cls._instance_

#ambos objetos SON la misma instancia de la clase
printer_pool1 = naive_singleton.create_instance()
printer_pool2 = naive_singleton.create_instance()

print(printer_pool1)
print(printer_pool2)

#Debe mostrar si printer_pool1 y printer_pool2 corresponden a la misma instancia de clase (en este caso, es VERDADERO):
print(f"Son la misma instancia?: {printer_pool1 is printer_pool2}")
