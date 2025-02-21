#CONCEPTOS BÁSICOS DE PROGRAMACION FUNCIONAL
#1. FUNCIONES SON CIUDADANOS DE PRIMER ORDEN
#la definición de una función puede ser asignada a una variable como una referencia

from functools import reduce

import math

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    if b != 0:
        return a/b
    
val1 = int(input("ingrese valor 1: "))
val2 = int(input("ingrese valor 2: "))
op = int(input("ingrese la operación: 1. suma 2. resta 3. multip. 4. div.: "))

if op == 1:
    operacion = suma
elif op == 2:
    operacion = resta
elif op == 3:
    operacion = multi
elif op == 4:
    operacion = div
else:
    print("Operación no válida")

#funcion de orden superior definida por el usuario:
def aplicar_operacion(operacion, operando1, operando2):
    return operacion(operando1, operando2)

print(f"El resultado es:{operacion(val1, val2)}")
#usando la función de orden superior:

print(f"El resultado es (aplicando mi función de orden superior):{aplicar_operacion(operacion,val1,val2)}")

# x = suma
# y = suma

# print(x(5,3))
# print(y(6,8))


#Ejemplo: una calculadora.



#2. FUNCIONES PURAS
#3. FUNCIONES ANÓNIMAS (LAMBDA)
num = int(input("Ingrese un número cualquiera:"))
es_par = lambda x: x % 2 == 0
print(es_par(27))
print(f"{num} es par?: {es_par(num)}")

#4. FUNCIONES DE ORDEN SUPERIOR
#Funciones que pueden recibir como parámetros, otras funciones
#O devolverla
# Funciones de Orden Superior típicas en Python:
#   map
#   filter
#   reduce

# 4.a MAP
#Ejemplo sin map: normalizar un conjunto de datos:
ciudades = ["Cali", "medellin", "BOGOTA", "bArrAnQuillA"]

#ES UNA FUNCIÓN PURA? SI
def normalizar_datos(lista_nombres):
    datos_norm = []
    for nombre in lista_nombres:
        datos_norm.append(nombre.capitalize())
    return datos_norm

#Usando map, sin función lambda:
def capitalizar(palabra):
    #retorna la palabra con la inicial en mayúscula
    return palabra.capitalize()

#una funcion que se va a mapear sobre cadenas
def capitalizar(palabra):
    return math.tan(palabra)

ciudades_norm2 = list(map( capitalizar, ciudades))


ciudades_norm = normalizar_datos(ciudades)
print(f"Datos sin normalizar:{ciudades}")
print(f"Datos normalizados:{ciudades_norm}")
print(f"Datos normalizados con map (sin lambda):{ciudades_norm2}")

#usando map, con lambda:
ciudades_norm3 = list(map ( lambda n: n.capitalize() ,ciudades  ))
print(f"Datos normalizados con map (con lambda):{ciudades_norm3}")


#uso de la función "filter":
#filter aplica una función booleana sobre una lista de objetos, y devuelve una lista más pequeña

edades = [12, 14, 18, 19, 24, 25, 28]

personas = [{"nombre":"Diego","edad":"38"},
            {"nombre":"Diana","edad":"34"},
            {"nombre":"Carolina","edad":"36"},
            {"nombre":"Pedro","edad":"28"}
           ]

print(personas[0]["nombre"])

print(f"\nEdades sin filtrar:{edades}")

#la funcion de filtro debe ser una función booleana:
def filtrar_mayores_edad(edad):
    return edad >= 18

def filtrar_personas_mayores(persona):
    return int(persona["edad"]) >= 18

mayores_edad = list(filter(filtrar_mayores_edad, edades))

#funciona?
personas_mayores = list(filter(filtrar_personas_mayores,personas))

#print(f"Mayores de edad:{mayores_edad}")
print(f"Mayores de edad:{personas_mayores}")

#la función reduce:
#consolida los elementos de una lista usando una función que se aplica por cada par de elementos:

#Generar una lista de números de 1 a 100:
numeros = list(range(1,101))

#sumarlos con un iterador:
sum = 0
for i in numeros:
    sum = sum + i

print(sum)

#sumar con reduce y una función lambda:
suma = reduce(lambda a,b:a+b, numeros)
print(suma)
