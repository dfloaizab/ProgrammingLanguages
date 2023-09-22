#Conceptos centrales de la P.O.O.:

#1. Abstracción
#2. Encapsulamiento
#   Modificadores de acceso (atributos de instancia)
#   a) private
#   b) public 
#3. Polimorfismo
#   capacidad de que las clases/funciones/operadores adopten
#   distintos comportamientos
#4. Herencia

#2. encapsulamiento
class ProductoInvestigacion:

    #se invoca al instanciar un nuevo objeto
    def __init__(esteObjeto,pTitulo, pAutores):
        esteObjeto.titulo = pTitulo
        esteObjeto.__autores = pAutores

    #método de instancia, público
    def eliminarAutor(esteObjeto,pAutor):
        pass

    #método de instancia, privado
    def __eliminarAutor(pAutor):
        pass        

class ArticuloRevista(ProductoInvestigacion):

   def __init__(this,pTitulo, pAutores,pIssn, pVol, pNum, pAnio):
       super().__init__(pTitulo, pAutores)
       this.issn = pIssn
       this.vol = pVol
       this.num = pNum
   
class Libro(ProductoInvestigacion):

    def __init__(esteObjeto, pTitulo, pAutores):
        super().__init__(pTitulo, pAutores)
    

class RegistroSoftware(ProductoInvestigacion):

    def __init__(esteObjeto, pTitulo, pAutores):
        super().__init__(pTitulo, pAutores)

        
    
