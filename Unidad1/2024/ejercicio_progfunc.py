 from functools import reduce


# estudiantes = [
#     {"nombre": "Kevin", "edad": 22, "notas": [3.5, 3.8, 4.7]},
#     {"nombre": "Sebastián", "edad": 21, "notas": [3.6, 3.7, 4.8]},
#     {"nombre": "Brayan", "edad": 18, "notas": [4.5,3.8, 4.5]},
#     {"nombre": "Moisés", "edad": 23, "notas": [4.4, 3.6, 4.7]}
# ]

# #usar map para calcular promedio de notas de cada estudiante:
# lista = [3.0, 5.0, 4.5]
# suma_lista = sum(lista)
# prom_lista = suma_lista / len(lista)
# print(suma_lista)
# print(prom_lista)

# promedios = list(map(lambda record: sum(record["notas"])/len(record["notas"]), estudiantes     )     )
# print(promedios)

# #usar filter para obtener lista de estudiantes de cierta edad:
# edad = int(input("Ingrese la edad para filtrar:\n"))
# lista_filtrada = list(filter(  lambda rec: rec["edad"] >= edad     ,estudiantes    )  )
# print(lista_filtrada)

# #usar reduce para obtener promedio de notas de todos los estudiantes:
# promedio_general = reduce( lambda x,y: x+y  ,promedios) / len(promedios)
# print(promedio_general)

# ##### RECURSION EN EL PARADIGMA FUNCIONAL
 lista_test = list(range(1,10,1))

def fun_sumalista_iter(lista):
    suma=0
    for n in lista:
         suma = suma +n
     return suma

# #función recursiva 
def fun_sumalista_rec(lista):
     if not lista:
         return 0
     else:
         return lista[0] + fun_sumalista_rec(lista[1:])
    
 def fun_sumalista_rec_ht(lista):
     if not lista:
         return 0
     else:
         #separa la lista en un elemento inicial y el resto:
         head, *tail = lista
         return head + fun_sumalista_rec_ht(tail)
    
 print(fun_sumalista_iter(lista_test))
 print(fun_sumalista_rec(lista_test))
 print(fun_sumalista_rec_ht(lista_test))

 #filtrar lista con los elementos > a limite
def filtra_lista(lista, limite):
     if not lista:
         return []
     else:
         #
         head, *tail = lista


#EJERCICIO:
        
#INVERTIR UNA LISTA DE OBJETOS
        



#INVERTIR UNA CADENA DE CARACTERES  


#FIBONACCI
        
def fibonacci_rec( N  ):
    if N <= 1:
        return N
    else:
        return fibonacci_rec(N-1) + fibonacci_rec(N-2)
    
ene = int(input("Ingrese el termino:"))
print(fibonacci_rec(ene))


def reverse_list(lst_str):
    if not lst_str:
        return []
    else:
        head,*tail = lst_str
        return reverse_list(tail) + [head]
    

def distinct_cars(str):
    if not str:
        return 0
    else:
        h,*t = str
        if h in t:
            return distinct_cars(t)
        else:
            return 1 + distinct_cars(t)


#EJERCICIO PREPARACION

records_humedales = [
    {"nombre":"panamericano","area":200,"especies_a":[     
            {"nombre":"iguana","ejemplares":200},
            {"nombre":"garzas","ejemplares":250}
    ],"estado_conserv":"bueno"},
    {"nombre":"lago de la babilla","area":200,"especies_a":[     
            {"nombre":"babilla","ejemplares":8},
            {"nombre":"garzas","ejemplares":100}
    ],"estado_conserv":"bueno"}    
]    

#CALCULAR, USANDO MAP, REDUCE, FILTER:

# (1) área total de los humedales
# (2) filtrar humedales con un total de ejemplares animales > 150
# (3) promedio de número de ejemplares de los humedales

        
    
print(reverse_list(["D","i","e","g","o"]))



    

        







