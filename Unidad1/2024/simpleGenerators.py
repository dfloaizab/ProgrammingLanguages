def gen1():
    for i in range(1,101):
        yield i

gen_fun = gen1()

print(next(gen1()))
print(next(gen1()))

print("de ciclo:\n")
try:
    for i in range(1,101):
        print(next(gen_fun))
except StopIteration:
    pass