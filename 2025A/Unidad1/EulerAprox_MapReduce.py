from functools import reduce
from math import *

lim = int(input("Ingrese el numero de términos:"))

nums = list(range(0,lim+1))
print(nums)

#función para calcular cada término de la serie de McLaurin que aproxima e1:
def fun_map_e1(n):
    return (1/factorial(n))

#función para calcular cada término de la serie de Maclaurin para la aproximación de e^x:
def fun_map_ex(n, x):
    return (x**n/factorial(n))

#función que calcula la sumatoria de toda la lista sumando los términos por pares:
def fun_redux(a,b):
    return a+b

#--- Aproximación de e^1 con map-reduce:
#aplica la función dentro de la sumatoria a cada término de 0 a lim:
terminos1 =  list(map(fun_map_e1, nums))
#aproxima e^1 sumando todos los términos:
aprox = reduce(  fun_redux, terminos1 )

print(f"Aproximación de e^1 con {lim} términos:{aprox}")

#cómo aproximar e^x?
#--- Aproximación de e^x con map-reduce:
x = int(input("Ingrese x:"))
#calcula cada término de la serie con map:
terminos2 =  list(map(lambda n:fun_map_ex(n,x), nums))
#reduce usando la suma con reduce:
aprox2 = reduce(fun_redux, terminos2)

print(f"Aproximación de e^{x}:{aprox2}")
