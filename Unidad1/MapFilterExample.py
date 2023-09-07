def convertirAAnios(x):
    return {
        x["nombre"].lower(),
        x["Edad"]/12,
        x["Vegetariano"]
    }

def filtrarVegetarianos(x):
    x["Vegetariano"] = True

listaEstudiantes = [ 
    {"nombre":"Diego","Edad":552,"Vegetariano":False},
    {"nombre":"Diana","Edad":480,"Vegetariano":False},
    {"nombre":"Camila","Edad":312,"Vegetariano":True}
]

listaEdadAnios = list(map(convertirAAnios,listaEstudiantes))
print(listaEdadAnios)

listaVegetarianos = list(filter(lambda x:x["Vegetariano"]==True,listaEstudiantes))
listaEdadAnios = list(map(convertirAAnios,listaVegetarianos))
print(listaEdadAnios)