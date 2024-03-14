#uso de funciones de orden superior: map, filter, reduce

from functools import reduce

#funcion para el filter:
def es_par(x):
    return x%2 == 0

#funcion para el reduce:
def suma(a,b):
    return a+b

def concat(a,b):
    return a+" "+b

lista = list(range(1,1001,1))
print(lista)


lista_pares = list (filter (  es_par   ,lista    )    )
print(lista_pares)

lista_pares_lambda = list (filter(  lambda x: x%2 == 0    ,lista     ))
print(lista_pares_lambda)

sumatoria = reduce( suma, lista_pares)
producto = reduce( lambda x,y: x*y, lista_pares)
print(sumatoria)
print(producto)

#Ejercicio:
lista_palabras = ["muchos","años","después,","frente","al","pelotón","de",
         "fusilamiento","el","coronel","Aureliano","Buendía"]

texto = reduce( lambda x,y: x+" "+y, lista_palabras   )
print(texto)