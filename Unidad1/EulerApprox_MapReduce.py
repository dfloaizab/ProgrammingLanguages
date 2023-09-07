#An approximation of the euler number
#using a series with map and reduce
#(according to pdf)
from functools import reduce

#definition of factorial:
def factorial(N):
    res = 1
    for x in range(1,N+1):
        res = res*x
    return res

#get the number of terms of the series
num_terms = int(input("Cuántos elementos debe tener la serie?"))
terms = list(range(0,num_terms+1))

#create list of 1/n! :
terms2 = list(map(  lambda x: 1/factorial(x)  ,terms))

print(terms2)

#sums the new list:
result = reduce(lambda x,y:x+y, terms2)
print(f"número de euler aproximado con {limit} términos: {result}")


