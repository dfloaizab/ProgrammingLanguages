from functools import reduce

# función predefinida para usar con el reduce (ejemplo 1)
def MiSuma(a,b):
    return a+b
# generación de la lista de prueba desde 1 hasta 1, con increment
# de 1
listaNumerosPares = list(range(1,101,1))
print(listaNumerosPares)

#cálculo de una usando un iterador:
suma = 0
for i in listaNumerosPares:
    suma = suma + i

print(suma)

listaCadenas = ["Muchos","años","después",",","frente","al","pelotón","de","fusilamiento"]

#serie sumatoria, usando la función reduce
#sumaTotalReduce = reduce(MiSuma, listaNumerosPares)
sumaTotalReduce = reduce(lambda x,y: x+y,  listaNumerosPares  )
productoTotalReduce = reduce( lambda x,y:x/y  , listaNumerosPares)
inicioCienAniosSOledad = reduce(lambda x,y: x+" "+y, listaCadenas)
print(f"Suma con reduce:{sumaTotalReduce}")
print(f"Producto con reduce:{productoTotalReduce}")
print(inicioCienAniosSOledad)