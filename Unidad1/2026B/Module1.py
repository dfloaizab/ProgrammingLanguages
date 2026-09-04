#Es una función pura?
#NO es pura
#Cómo la hacemos pura?
def agregar(lista, elemento):
    lista.append(elemento)
    return lista

#Es una función pura
#TAMPOCO ES PURA
#Cómo la hacemos pura?
def eliminar(lista, elemento):
    lista.remove(elemento)
    return lista

def buscar(lista, elemento):
    pass

#Es una función pura?
#SÍ
def duplicar(x):
    return x*2

#Vamos a hacer una versión "función pura"
#de la función agregar elemento a lista:
def agregar_pura(lista, elemento):
    #copia = lista #NO CREA COPIA DE LA LISTA, NO ES PURA
    #copia = lista.copy() # SÍ CREA UNA COPIA, HACE LA FUNCIÓN PURA
    copia = list(lista) # OTRA FORMA DE CREAR UNA COPIA DE UNA LISTA
    copia.append(elemento)
    return copia

def eliminar_pura(lista, elemento):
    nueva_lista = lista.copy()
    nueva_lista.remove(elemento)
    return nueva_lista

# recibe lista = [2,4,6,8] y mult = 3
# retorna 6, 12, 18, 24
def mult_pura(lista, mult):
    #Quiero que la función multiplique cada valor de la lista por el multiplicador
    # List comprehension
    return [ elemento * mult for elemento in lista ]

# definir tres funciones de exponenciación:
def cuadrado(num):
    return num ** 2

def cubo(num):
    return num ** 3

def pow(num, n):
    return num ** n

def suma(a,b):
    return a+b

# Función de orden superior que aplica una determinada funcion a un valor y devuelve un número:
def aplicar_funcion(funcion, valor, pot):
    # Validar si la funcion es cuadrado, cubo, o pow:
    # is, isInstance, type
    if funcion is cuadrado:
        return cuadrado(valor)
    elif funcion is cubo:
        return cubo(valor)
    elif funcion is pow:
        return pow(valor, pot)


def corregir(palabra):
    return palabra.capitalize()

def reducir_lista_palabras(palabra1, palabra2):
    return palabra1 + " " + palabra2

def es_impar(numero):
    return numero % 2 != 0
    #Hay una forma más compacta de hacerlo...
    # if numero % 2 == 0:
    #     return False
    # else:
    #     return True

def convert_f_to_c(temp):
    return (temp - 32)*(5/9)

def filtrar_mayores(temp):
    return temp > 32
