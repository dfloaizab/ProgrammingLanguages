from functools import reduce
from Module1 import *
import random

#Salida por consola:
# print("Hola, Mundo")

#Petición de datos por consola:

#Tipado dinámico (como javascript) vs. tipado estático de otros lenguajes (C, C#, Java)

#------- Tipos de datos en Pyton:
'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType ("null")
'''

# current_year = 2026
# tallest_person_height = 2.3
# name = input("Cuál es tu nombre?:\n")
# #OJO CON EL INPUT: siempre devuelve un dato de tipo str, debo convertirlo al tipo que quiero asignar
# #a mi variables:
# b_year = int(input("Cuál es tu año de nacimiento?:\n"))
# height = float(input("Cuál es tu estatura?:\n"))

# age = current_year - b_year
# height_difference = (tallest_person_height - height)*100

#Cómo redondeamos a 1 decimal?


#Impresión con formato:
#comentar en bloque: ctrl + K + C
#descomentar en bloque: ctrl + K + U
# print(f" Te llamas {name}  y tienes {age} años. Bienvenido a lenguajes de programación  ")
# print(f"La persona más alta, te lleva {height_difference} cm.")

#----- COLECCIONES DE DATOS:
# (en otros lenguajes existen arreglos, matrices, etc)

# 1. Listas [] (mutable)
# empty_list = []
# empty_list.append(1)
# empty_list.append("Uno")
# empty_list.append(1.0)
# empty_list.append(True)


# not_empty_list = empty_list


# reversed_list = not_empty_list.reverse() #¿?

# print(f"La lista quedó así: {not_empty_list}")
# print(f"La lista al revés:{reversed_list}")

# 2. Tuplas (,) - *,* (datos inmutables)

# coord_1 = 1,5
# coord_2 = (8,5)
# students = ("Jhon Stiven","Gabriela","Andrea") #Tupla (es inmutable, los valores no se pueden cambiar)
# students_list = ["Jhon Stiven","Gabriela","Andrea"]
# print( f"\nPrimero se matriculó: {students[0]}")
# print(f"\nLuego se matriculó: {students[1]}")
# print(f"\nFinalmente se matriculó: {students[2]}")

# ¡¡¡
#students[1] = "Gabriela Rico" # NO SE PUEDE ALTERAR EL VALOR DE UNA TUPLA:
# students_list[1] = "Gabriela Rico"
# students_list = agregar(students_list, "Diego")

# print("Con el elemento eliminado:")
# print(students_list)

####   UNIDAD 1: PROGRAMACIÓN FUNCIONAL EN PYTHON
'''
Ayuda a escribir código 
* más limpio, 
* fácil de probar y 
* libre de errores ocultos al tratar las "funciones como elementos principales" 
(FUNCIONES COMO CIUDADANOS DE PRIMER ORDEN) y evitar cambios en los datos (INMUTABILIDAD Y FUNCIONES PURAS).
'''
# CONCEPTOS BÁSICOS DE PROGRAMACIÓN FUNCIONAL EN PYTHON (EN PAUSA, VOLVEMOS A LAS 8:40 PM)

# 1. FUNCIONES COMO OBJETOS O CIUDADANOS DE PRIMER ORDEN:

#menu condicional para elegir que función operar sobre la lista:

# nombre_curso = "Lenguajes de Programacion"

# while True:
#     opcion = int(input("Qué operación desea aplicar? 1. Agregar 2. Eliminar 3. Salir: "))
#     if opcion == 1:
#         funcion = agregar #FUNCION COMO OBJETO DE PRIMER ORDEN 
#     elif opcion == 2:
#         funcion = eliminar 
#     else:
#         break

#     valor = input("Ingrese el valor que desea agregar o eliminar: ")
#     students_list = funcion(students_list,valor)
#     print(students_list)


#EJERCICIO: vamos a agregar la función "BUSCAR"

#Agosto 27, 2026
# 2. FUNCIONES PURAS: 
'''
Una función pura es un bloque de código que siempre produce el mismo resultado 
si recibe los mismos argumentos y no causa efectos secundarios (es decir, no modifica 
variables globales, no altera los datos de entrada ni realiza operaciones de entrada/salida 
como print o escritura en archivos).

public class Persona
{
    //atributos y métodos:
    float salario;
    String nombre;
    int identificador;

    //métodos
    public Persona(){}
    public float getSalario(){}
    public void setSalario(){}
    public void aplicarAumento(float porc){}
    public void aplicarBonific(float valor){}
    
}
'''
#Ejemplo:
valor_usuario = int(input("Ingrese un entero cualquiera:"))
# valor_usuario = duplicar(valor_usuario)
# print(f"El valor duplicado es: {duplicar(valor_usuario)}")
# #Funciona como una función pura?
# lista_1 = [1,2,3,4]
# lista_2 = agregar_pura(lista_1,6)

# 3. FUNCIONES DE ORDEN SUPERIOR (PUEDEN RECIBIR COMO PARÁMETRO OTRAS FUNCIONES)
'''
Las funciones de orden superior son aquellas 
que pueden recibir otras funciones como argumentos o devolver una función como resultado.
'''
# operacion = int(input("Qué operación desea aplicar? 1. cuadrado 2. cubo 3. potencia n: "))
# if operacion == 1:
#     print(f"resultado:{aplicar_funcion(cuadrado, valor_usuario,0)}")
# elif operacion == 2:
#     print(f" resultado: {aplicar_funcion(cubo, valor_usuario,0)}")
# elif operacion == 3:
#     pot = int(input("A qué potencia desea elevar su número?:"))
#     print(f"resultado: {aplicar_funcion(pow, valor_usuario, pot)}")

# 3.1 MAP, REDUCE, FILTER: FUNCIONES DE ORDEN SUPERIOR ESPECIALES, PARA PROCESAMIENTO DE DATOS.
# 3.1.1. MAP
# Supongamos que tenemos la lista [0,2,3,4,5,6,7,8,9,10,...,999]
list1000 = list(range(1000))
print(list1000)
#Vamos a elevar todos los elementos de la lista, al cuadrado:
lista_cuadrados = list(map(cuadrado, list1000))
print(f"Lista de cuadrados:{lista_cuadrados}")

# --------- EJERCICIO:
lista_palabras = ["muchos","AÑOS","DESPUÉS","frente","AL","PeLoTÓN","De","FUSiLAMiENTO,","eL","CORONEL"]

# 1. Vamos a mapear una función que permita crear una lista con las palabras con las mayúsculas correctas:
lista_palabras_corregida = list(map(corregir,lista_palabras))
print(f"Lista de palabras capitalizadas: {lista_palabras_corregida}")

# 2. "reduce" la lista usando una función de concatenación, para armar la primera oración de la palabra:
#-----------------------------------------------------------------------------------------------------------
oracion1_CADS = reduce(reducir_lista_palabras,lista_palabras_corregida)
print(f"Primera oración de Cien Años de Soledad, de Gabriel García Márquez:{oracion1_CADS}")

#3.1.2 la función "REDUCE", reduce o consolida una lista:
# Aplica la función suma por pares de elementos, hasta que sume todos los números de la lista
#suma_numeros = reduce( suma, list1000 )
suma_numeros = reduce(lambda x,y:x+y, list1000)
print(f"la suma total de los números es {suma_numeros}")


#3.1.3 la función "FILTER" aplica una función booleana sobre una lista de elementos, y genera una nueva lista con
#       con los elementos que cumplan con la condición de la función de filtro
lista_impares1000 = list(filter(es_impar, list1000))
print(f"Primeros 1000 números impares:{lista_impares1000}")

#EJERCICIO EN CLASE:
#1. Tenemos una lista de temperaturas capturadas desde un sensor, pero vienen en °F.
# generar un solo número aleatorio: 
numero_float = random.uniform(0.0,100.0)
random_temps_f = []
# generar una lista de varios números aleatorios (100):
for _ in range(10):
    random_temps_f.append(random.uniform(50.0,100.0))


print(f"\nTemperaturas aleatorias °F:\n{random_temps_f}")
#2. Vamos a convertir a °C
#temps_c = list(map(convert_f_to_c, random_temps_f))
temps_c = list(map(lambda f:(f - 32)*(5/9), random_temps_f))
print(f"\nTemperaturas aleatorias °C:\n{temps_c}")

#3. Vamos a filtrar aquellas que sean mayores a 32.0° C
#temps_M_32 = list(filter( filtrar_mayores, temps_c  ))
temps_M_32 = list(filter( lambda t: t > 32, temps_c  ))

suma_temps = reduce(lambda x,y:x+y, temps_M_32)
print(f"suma de temperaturas:{suma_temps}")
# ¿FUNCIONA?

# 4. FUNCIONES ANÓNIMAS (LAMBDA)
# Una función lambda en Python es una pequeña función ("abstracción de una función")
# anónima (sin nombre) que se define en una sola línea utilizando la palabra reservada lambda
# se define como:
# lambda argumentos: expresión

# SEPTIEMBRE 3: EJERCICIO MAP, FILTER, REDUCE, LAMBDA 
producto1 = {"nombre":"Camisa","precio":150000 }
producto2 = {"nombre":"Par de Zapatos","precio":250000}

#Lista de productos, con precios en dólares:
productos = [
    {"nombre": "Camisa", "precio": 30},
    {"nombre": "Zapatos", "precio": 120},
    {"nombre": "Gorra", "precio": 15},
    {"nombre": "Pantalón", "precio": 80},
    {"nombre": "Calcetines", "precio": 10},
]
print("\nProductos con precio en dólares:",productos)

print("\n--- 1. MAP ---")
#Conversión de dólares a pesos:
productos_pesos = list(
    map(
        lambda p:{
            "nombre":p["nombre"],
            "precio":round(p["precio"]*3200.0,2)
        },
        productos 
    )
)
print("\nProductos con precio en pesos:",productos_pesos)
#Aplicar un descuento del 10%
productos_con_descuento_10 = list(
    map(
        lambda p:{
            "nombre":p["nombre"],
            "precio":round(p["precio"]*0.9,2)
        },
        productos_pesos
    )
)
print("\nProductos en pesos con descuento del 10%",productos_con_descuento_10)
print("\n--- 1. FILTER ---")
#VAMOS A FILTRAR PRODUCTOS CON PRECIO > 50000:
productos_caros = list(
    filter(
        lambda producto:producto["precio"]>50000,
        productos_con_descuento_10
    )
)
print("\nProductos caros:",productos_caros)

total_carrito = reduce(
    lambda acum,p:acum + p["precio"],
    productos_caros,
    0 
)
print("\nEl total del carrrito de compras es", total_carrito)

#Septiembre 10
#------------------------ 5. FLUJOS DE DATOS (STREAMS) Y "LAZY EVALUATION" (EVALUACIÓN PEREZOSA) ("Eager Evaluación")


#Septiembre 17
#----------------------- Ejercicio de Repaso

