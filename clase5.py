#Using higher order functions: map, reduce, filter
import functools
import Module2 as M2

#creating a list from a range
lista_cop = list ( range (5000, 10000, 350  ))
print(lista_cop)

#napping a lambda function to a list
lista_usd = list(map(lambda x: x/4380, lista_cop))

print(lista_usd)

lista_nombres = ["Diego", "Diana", "Falkor", "Sabina", "Rodrigo"]

lista_nombres_mayus = list ( map( lambda x:  x.upper() , lista_nombres ))

#filtering a list with a lambda function
lista_nombres_fil = list (filter( lambda x: x.__len__() >= 7  ,lista_nombres ))

#reducing a list to a value using a lambda function
nombres =functools.reduce(lambda x,y: x+","+y, lista_nombres)


print(nombres)
print(lista_nombres_fil)
print(lista_nombres_mayus)
print(str(lista_nombres_mayus))

#Loading a list of dictionaries as a key/value dataset using a function in Module2
myFileName = input("Ingrese el nombre del archivo:")
DataBase1 = M2.loadDataCSV(myFileName)

#Filtering a list of dictionaries using higher order functions


#Filtering a list of dictionaries using list comprehension