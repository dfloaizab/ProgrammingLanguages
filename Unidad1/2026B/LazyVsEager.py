

'''
Evaluación hambrienta: Calcula el resultado completo inmediatamente y lo almacena completamente en la memoria. 
Este es el comportamiento predeterminado de Python para estructuras de datos estándar como listas, conjuntos y diccionarios. 
[1] (https://paths.grasp.study/modules/ec733c04-c287-47f5-88b3-6af6687e98c4/lessons/2eb9f0b3-f126-4038-977b-f33b7d01605f), 
[2] (https://khaisastudio.medium.com/eager-vs-lazy-approach-0b4b7ba63c90), 
[3] (https://levelup.gitconnected.com/evaluation-strategy-in-python-22eb454202e2), 
[4] (https://www.youtube.com/watch?v=9o6KhLWVmnQ)

Evaluación perezosa: Pospone el cálculo hasta el momento exacto en que se solicita o se necesita un valor específico. 
Esto te permite procesar datos como un flujo continuo, elemento por elemento, sin cargar todo en memoria de una vez.
'''


#Función para un consumidor hambriento:
def eager():
    numbers = []
    for i in range(10000):
        numbers.append(i)
    return numbers

#--- Función perezosa: genera valores, bajo demanda.
def lazy_generator():
    for i in range(100000):
        yield i #Yield hace esto: 1. genera i 2. suspende la ejecución del ciclo 3. espera que le pidan el siguiente valor con next


# (1) ----- Consumo con "evaluación hambrienta":
# nuevos_numeros = eager()
# print(nuevos_numeros)

# (2) ----- Consumo con evaluación perezosa:
gen = lazy_generator()


try:
    while True:
        print(next(gen))
except StopIteration:
    print("El generador ya no tiene más números")
