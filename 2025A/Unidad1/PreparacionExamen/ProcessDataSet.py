from functools import reduce

#lector de datos de un csv que funciona como un generador para un evaluador perezoso:
def loadData(filePath):
    with open(filePath,mode="r",encoding="utf-8") as file:
        headers = file.readline().strip().split(",") #leer encabezado como las claves del diccionario
        for line in file:
            values = line.strip().split(",")
            record = dict(zip(headers, values))
            yield record

#función de conversión con la tasa como un literal en la implementación
def USD_to_COP(registro):
    registro["Salario"] = int(registro["Salario"])*4100
    return registro



def filter7Mill():
    pass
    
def sumAll(x,y):
    pass

dataStream = loadData("data.csv")
#Consumir tres registros y mostrarlos por pantalla:
dataLocal = []
dataLocal.append(next(dataStream))
dataLocal.append(next(dataStream))
dataLocal.append(next(dataStream))

print(dataLocal)

#Convertir campo "Salario" de USD to COP mapeando una función de conversión de divisas:
#{'ID': '1', 'Nombre': 'Ana', 'Edad': '25', 'Salario': '3000', 'Departamento': 'Ventas'}
listaSalarioPesos = list(map(USD_to_COP,dataLocal))
#Filtrar aquellos que tengan un salario mayor a $COP 7'000.000:
listaMayores = list(filter(filter7Mill, listaSalarioPesos))
#Sumar el total de salario de esas personas con reduce:
sumaTotal = reduce(sumAll,listaMayores)
