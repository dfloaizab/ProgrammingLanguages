from Model import *
from View import *

class ProductCatalogController:

    def __init__(this, model:ProductModel, view:ProductView):
        this.model = model
        this.view = view

    #Obtener información de la vista para actualizar el modelo
    # (mejorar con un Observer?)
    def addNewProduct(this):
        name, price = this.view.addNewProduct()        
        this.model.addProduct(Product(name, price))

    #actualizar la vista con información del modelo:
    def showProducts(this):
        catalog = this.model.getCatalog()
        this.view.displayCatalog(catalog)