#generador perezoso de múltiplos de m
#(genera uno a la vez: yield lo retorna y espera a que le pidan el siguiente)
def multM(m):
    num = 0
    while True:
        if num % m == 0:
            #el productor entrega un dato y espera a que le pidan más (perezoso)
            yield num
        num = num +1


generadorMultiplos = multM(7)

#el consumidor también es "perezoso", pide un dato a la vez
print(next(generadorMultiplos))
print(next(generadorMultiplos))
print(next(generadorMultiplos))

#al usar un generador en un ciclo, se debe usar un try catch:
try:
    pass
    for _ in range(100):
        print(next(generadorMultiplos))
except StopIteration:
    print("Se ha producido un error consumiendo datos del generador")
