from functools import reduce

# función predefinida para usar con el reduce (ejemplo 1)
def MiSuma(a,b):
    return a+b
# generación de la lista de enteros de prueba desde 2 hasta 100, 
# con incrementos de 2
listaNumerosPares = list(range(2,101,2))
print(listaNumerosPares)

#cálculo de una sumatoria usando un iterador:
suma = 0
for i in listaNumerosPares:
    suma = suma + i

print(suma)

#una lista de cadenas, para usar otra función de "reducción":
# (concatenación)
listaCadenas = ["Muchos","años","después",",","frente","al","pelotón","de","fusilamiento"]

#serie sumatoria, usando la función reduce
#reduce usando la función suma predefinida
sumaTotalReduce = reduce(MiSuma, listaNumerosPares)
#reduce usando una función lambda suma:
sumaTotalReduce = reduce(lambda x,y: x+y,  listaNumerosPares  )
#otra función lambda de reducción (división):
productoTotalReduce = reduce( lambda x,y:x/y  , listaNumerosPares)
#reducción con concatenación:
inicioCienAniosSOledad = reduce(lambda x,y: x+" "+y, listaCadenas)
print(f"Suma con reduce:{sumaTotalReduce}")
print(f"Producto con reduce:{productoTotalReduce}")
print(inicioCienAniosSOledad)
