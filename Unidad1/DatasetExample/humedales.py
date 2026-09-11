# Generador "Eager": genera todo el dataset, haciendo esperar al consumidor:
def LoadData(fileName):
    dataset = []
    with open(fileName,encoding='utf-8') as f:
        for line in f: #iterar x cada renglón del archivo
            values = line.split(sep=';')
            registro = {"nombre":values[0],
                        "direccion":values[1],
                        "hectareas":float(values[2]),
                        "aves":int(values[3]),
                        "flora":int(values[4]),
                        "estado":values[5]}
            dataset.append(registro)    
    return dataset

# Generador "Lazy": genera un nuevo registro solo si se lo piden:
def LoadData_lazy(fileName):
    with open(fileName,encoding='utf-8') as f:
        for line in f: #iterar x cada renglón del archivo
            values = line.split(sep=';')
            registro = {"nombre":values[0],
                        "direccion":values[1],
                        "hectareas":float(values[2]),
                        "aves":int(values[3]),
                        "flora":int(values[4]),
                        "estado":values[5]}
            yield registro  

eager_eval = LoadData("dataset1.csv")
print("Todos los registros:\n",eager_eval)

lazy_eval = LoadData_lazy("dataset1.csv")
print("Primer registro: ", next(lazy_eval))
print("segundo registro: ", next(lazy_eval))
