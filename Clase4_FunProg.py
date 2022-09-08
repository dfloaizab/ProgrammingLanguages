#CLASE 4: FUNCIONES COMO OBJETOS DE PRIMER ORDEN

#Funciones de Ejemplo
from functools import reduce


def funcion1(x, y):
    return x+y

def funcion2(x,y):
    return x*y

#funciones de conversión de divisas:
def cop_2_usd(x):
    return x/4393

def cop_2_eur(x):
    return x/4380

def cop_2_stp(x):
    return x/5190

#(0) LAS FUNCIONES PUEDEN SER ALMACENADAS EN ESTRUCTURAS DE DATOS
lista_funciones = [funcion1, funcion2]
dic_funciones = {"suma":funcion1, "producto":funcion2}


# (1) LAS FUNCIONES PUEDEN SER RETORNADAS COMO VALORES
#Selector de funcion
def seleccionar_funcion():
    seleccion = input("Seleccione la operación ('S'=Suma, 'M' = Producto):")
    if seleccion == "S":
        #return funcion1
        #return lista_funciones[0]
        #return dic_funciones["suma"]
        return lambda x,y: x+y
    else:
        #return funcion2
        #return lista_funciones[1]
        #return dic_funciones["producto"]
        return lambda x,y: x*y

# (2) LAS FUNCIONES PUEDEN SER ASIGNADAS A VARIABLES
fun_ejecutar = seleccionar_funcion() 
print(type(fun_ejecutar))
#fun_ejecutar puede ser funcion1 o funcion2
result = fun_ejecutar(5,6)
print( f"resultado: {result}" )

#FUNCIONES DE ALTO ORDEN: FUNCIONES QUE OPERAN SOBRE OTRAS FUNCIONES

#conversión de divisas (sin map):
lista_cop = [ 108000.0, 8560.3, 9874.2, 54100.6, 47100.2 ]
lista_usd = []
for val in lista_cop:
    vlr_usd = val / 4393
    lista_usd.append(vlr_usd)

print(lista_usd)

# MAP 
#conversion de divisas 
#mapea la funcion "cop_2_usd" a cada elemento de lista_cop y devuelve
#un iterable que debe ser convertido a lista
result = map ( cop_2_usd, lista_cop  )
lista_usd = list(result)
print(lista_usd)

result2 = map(  lambda x: x/23 , lista_cop  )
print(list(result2))

# FILTER
print("lista original:")
print(lista_cop)
result3 = filter(  lambda a: a >50000.0, lista_cop  )
print("lista filtrada:")
print(list(result3))

total_usd = reduce (lambda x,y: x+y, lista_usd)
print(total_usd)
print(type(total_usd))










