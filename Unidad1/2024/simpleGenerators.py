def gen1():
    for i in range(1,101):
        yield i

gen_fun = gen1()

#obtener primeros 2 valores:
print(next(gen1()))
print(next(gen1()))

print("de ciclo:\n")
try:
    #obtener próximos números:
    for i in range(1,80):
        print(next(gen_fun))
    #obtener los próximos 10 con list comprehension:
    some_more = [next(gen1()) for _ in range(10)]

except StopIteration:
    pass
