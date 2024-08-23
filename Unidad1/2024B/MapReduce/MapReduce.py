#ejemplo del uso del map, filter y reduce:

from functools import reduce


listaNombres = [
    "Diego",
    "Catalina",
    "Clara",
    "Pedro",
    "Luis",
    "Concepción"
    ]

#-----  map: mapea una función a los elementos de un objeto iterable
#obtener las longitudes de los nombres:

def longCadena(c):
    return len(c)

#obtener nueva lista con las longitudes de los nombres:
longitudes = list(map(longCadena, listaNombres))
longitudes = list(map(lambda s: len(s),listaNombres))
print(f"Resultado de aplicar map sobre la lista \n{listaNombres}: \n{longitudes}")

#----  filtrar longitudes mayores a 5:
longitudes_mayores = list(filter(  lambda n: n > 5 , longitudes    ))

cadenas_mayores = list(filter( lambda s: len(s) > 5, listaNombres))
print(f"nombres con longitud >= 5:\n{cadenas_mayores}")

#----- sumar todos los valores de la lista:

long_totales = reduce(lambda x,y: x+y, longitudes_mayores)
print(f"Longitud total de las cadenas con longitud > 5: {long_totales}")
