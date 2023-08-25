#Función para crear un "dataset" como una lista de diccionarios
#a partir de un archivo plano
#param: la ruta del archivo plano
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
