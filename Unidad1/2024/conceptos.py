def op1(a,b):
    return a+b

def op2(a, b):
    return a*b

def op3(a, b):
    return a**b

def op4(a,b):
    return a-b

operacion = int(input("qué operacion? 1-suma, 2-multip, 3-potencia, 4: resta: "))
val1 = int(input("ingrese valor 1: "))
val2 = int(input("ingrese valor 2: "))

# 1a versión: como en algoritmos 1
# if operacion == "1":
#     print(f"el resultado es: {op1(val1,val2)}")
# elif operacion == "2":
#     print(f"el resultado es: {op2(val1,val2)}")
# elif operacion == "3":
#     print(f"el resultado es: {op3(val1,val2)}")
# elif operacion == "4":
#     print(f"el resultado es: {op4(val1,val2)}")
# else:
#     print("funcion no definida")

#version 2: guardamos en f referencia a la funcion elegida:
# if operacion == "1":
#     f = op1
# elif operacion == "2":
#     f = op2
# elif operacion == "3":
#     f = op3
# elif operacion == "4":
#     f = op4
# else:
#     print("funcion no definida")

#version 3: con funciones lambda (anónimas)
# if operacion == "1":
#     f = lambda x,y: x+y
# elif operacion == "2":
#     f = lambda x,y: x*y
# elif operacion == "3":
#     f = lambda x,y: x**y
# elif operacion == "4":
#     f = lambda x,y: x-y
# else:
#     print("funcion no definida")

#version 4: con listas de funciones:
list_func = [op1, op2, op3, op4]

#version 5: con arreglo de lambdas:
#                         f[0]             f[1]             f[2]             f[3]
list_func_lambda = [lambda x,y: x+y, lambda x,y: x*y, lambda x,y: x**y, lambda x,y: x-y]

#aplicar la funcion que está almacenada en la lista:
print(f"el resultado es: {list_func[operacion-1](val1,val2)}")

#version 6: usando map
list_func_map = list(map(lambda f:f(x,y), list_func))

