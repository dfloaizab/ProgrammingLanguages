#función "impaciente" para generación de una lista de n múltiplos de m:
def mult(n, m):
    mults=[   n for n in range(n+1) if n%m == 0 ]
    return mults

#funcion "perezosa" para generación de números múltiplos de m:
def mult_lazy(n, m):
    num = 0
    while True:
        if num % m == 0:
            yield num
        num += 1

# m = int(input("Ingrese m:"))
# n = int(input("Ingrese el número de términos:"))
# mults = mult(n,m)
# gen_mult = mult_lazy(n,m)

# first_100 = [  next(gen_mult) for _ in range(100)   ]
# print(f"Primeros 100:\n{first_100}")
# next_100 = [ next(gen_mult) for _ in range(100)]
# print(f"Siguientes 100:\n{next_100}")
# print(mults)

def lazy_sum(n):
    sum = 0.0 
    i = 0.0    
    while True:
        i += 1.0
        sum += 1/i
        yield sum

n = int(input("ingrese n:"))

#al usar el next sobre una función generadora que itera con un for, debe usarse  un
#bloque try_except para manejar el 
try:
    gen_sum = lazy_sum(n)
    list_aprox1 = [ next(gen_sum) for _ in range(n) ]
    aprox1 =  sum(list_aprox1)  

    list_aprox2 = [ next(gen_sum) for _ in range(n) ]
    aprox2 = sum(list_aprox2)
    print(f"Aproximación con los primeros {n}  = {aprox1}")
    print(f"Aproximación con los siguientes {n}  = {aprox2}")

except StopIteration:
    pass