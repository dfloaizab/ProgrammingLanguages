from functools import reduce
from math import *

lim = int(input("Ingrese el numero de términos:"))

nums = list(range(0,lim+1))
print(nums)

#función para calcular cada término de la serie de McLaurin que aproxima e:
def fun_map(n):
    return (1/factorial(n))

def fun_map_1(n, x):
    return (x**n/factorial(n))

#función que calcula la sumatoria de toda la lista sumando los términos por pares:
def fun_redux(a,b):
    return a+b

#aplica la función dentro de la sumatoria a cada término de 0 a lim:
terminos1 =  list(map(fun_map, nums))

#aproxima e^1 sumando todos los términos:
aprox = reduce(  fun_redux, terminos1 )

print(f"Aproximación de e^1 con {lim} términos:{aprox}")

#cómo aproximar e^x?
x = int(input("Ingrese x:"))

terminos2 =  list(map(lambda n:fun_map_1(n,x), nums))
aprox2 = reduce(fun_redux, terminos2)

print(f"Aproximación de e^{x}:{aprox2}")
