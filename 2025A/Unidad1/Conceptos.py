#CONCEPTOS BÁSICOS DE PROGRAMACION FUNCIONAL
#1. FUNCIONES SON CIUDADANOS DE PRIMER ORDEN
#la definición de una función puede ser asignada a una variable como una referencia

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    if b != 0:
        return a/b
    
val1 = int(input("ingrese valor 1"))
val2 = int(input("ingrese valor 2"))
op = int(input("ingrese la operación: 1. suma 2. resta 3. multip. 4. div."))

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

print(f"El resultado es:{operacion(val1, val2)}")

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

ciudades_norm2 = list(map( capitalizar, ciudades))


ciudades_norm = normalizar_datos(ciudades)
print(f"Datos sin normalizar:{ciudades}")
print(f"Datos normalizados:{ciudades_norm}")
print(f"Datos normalizados con map (sin lambda):{ciudades_norm2}")

#usando map, con lambda:
ciudades_norm3 = list(map ( lambda n: n.capitalize() ,ciudades  ))
print(f"Datos normalizados con map (con lambda):{ciudades_norm3}")

#Ejemplo con una función de orden superior: map

