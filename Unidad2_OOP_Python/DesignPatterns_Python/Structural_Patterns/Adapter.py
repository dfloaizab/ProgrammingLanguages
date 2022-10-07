#target
class Pdf_reader:
    def request(self) -> str:
        return "Lector: Lector PDF predeterminado"

#clase adaptada
class Document_word:
    def specific_request(self) -> str:
        return "parcial_2.docx"

#La clase adapter implementa el método que adapta la clase adaptada al target
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
