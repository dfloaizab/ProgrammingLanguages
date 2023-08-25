from LoadData import *

#función que será usada como filtro:
def filtroAves(humedal):
    return humedal["aves"] > 100

# nombreArchivo = input("Qué archivo vamos a leer?")
# miDataSet = LoadData(nombreArchivo)
# print(miDataSet)

# #filtrar humedales con especies de aves mayores a 30 (con una función ya definida):
# dataSetFiltrado = list(filter(filtroAves, miDataSet))

# #uso de filter con una función anónima (lambda):
# #                               funcion anónima  parámetro  retorno
# dataSetFiltrado2 = list(filter (lambda           x :        x["hectareas"]>4.0, miDataSet) )
# print(f"Humedales filtrados {len(dataSetFiltrado2)} \n")
# print(dataSetFiltrado2)

#dato tipo diccionario para la información de UN humedal
# como pares key:value:
# humedal1 = {  "nombre":"Lago de las garzas",
#               "direccion":"carrera 127 con calle 16A",
#               "hectareas":4.7,
#               "especies de aves":149,
#               "especies florales":148,
#               "estado":"en conservación"  }
# #elemento del dataset
# print(humedal1["nombre"])


registro = {"nombre":"PAMPALINDA",
            "direccion":"Calle 5a 62-00",
            "hectareas":20.0,
            "aves":54,
            "flora":37,
            "estado":"En conservación"}

campo_mayus = registro["nombre"].lower()
print(campo_mayus)

#Ejercicio : map y filter:
#1. definir una función map para convertir el campo nombre de cada estado a minúsculas
#2. aplicar con map al dataset
#3. definir una función filter para filtrar humedales con estado = "En recuperación"
#4. aplicar filtro
