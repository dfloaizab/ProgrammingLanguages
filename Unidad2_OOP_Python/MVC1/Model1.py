import pandas as p

#La clase modelo define los datos y en este caso también la forma de cargarlos
class DataLoader:
    #atributo de clase, compartido entre todas las instancias
    #de la clase
    loads = 0

    #método de inicialización, invocado al crear un objeto
    def __init__(self, pFileName):
        
        #loads es un atributo de clase:
        DataLoader.loads += 1

        #fileName es una atributo de instancia
        self.fileName = pFileName

        #dataframes como atributos de instancia:
        df_csv = p.DataFrame()
        df_json = p.DataFrame()
        df_xml = p.DataFrame()

    #Métodos Get:
    @property
    def csv_data(self):
        return self.df_csv

    @property
    def json_data(self):
        return self.df_json

    @property
    def xml_data(self):
        return self.df_xml

    def loadCSV(self):
        df_csv = p.read_csv(self.fileName)        

    def loadJSON(self):
        df_json = p.read_json(self.fileName)

    def loadXML(self):
        df_xml = p.read_xml(self.fileName)

   

