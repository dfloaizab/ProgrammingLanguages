class Product:

    def __init__(this, name, price):
        this.name = name
        this.price = price


class ProductModel:

    def __init__(this):
        this.catalog = []

    def addProduct(this, product: Product):
        this.catalog.append(product)

    def getCatalog(this):
        return this.catalog
    