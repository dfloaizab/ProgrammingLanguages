def transformar(lista, funcion):
    #esta función aplica una función a una lista de elementos sin modificar la lista original:
    nuevaLista = [] #creamos una lista vacía

    #se adiciona a la nueva lista, un elemento al que se le aplica la función que se recibe por parámetro:

    #ciclos en python:
    for elemento in lista:
        nuevaLista.append(funcion(elemento))

    return nuevaLista

def multiplicar(n):
    return n*5

#convierte con la tasa de conversión a pesos:
def USD_to_COP(x):
    return x*3667

# Ya la función la aplica a un item que tiene nombre y precio:
def USD_to_COP_Producto(x):
    #va a recibir un par llave/valor
    nuevoElemento = {"producto":x["producto"],"precio":x["precio"]*3667}
    return nuevoElemento

#convierte con la tasa de conversión a libras esterlinas:
def USD_to_STP(x):
    return x*0.73

#convierte de dolares a euros:
def USD_to_EUR(x):
    return x*0.84

#define las instrucciones del bloque que sigue, como el punto de entrada del programa:
if __name__ == "__main__":
    listaPrueba = [1,2,3,4,5]
    nuevaLista = transformar(listaPrueba,multiplicar)
    print(f"Lista con la función aplicada:{nuevaLista}")
    print(f"Lista original:{listaPrueba}")

    #ejemplo con conversión de divisas:
    listaPrecios_USD = [80, 25, 30, 45, 14]

    #listas de precios convertidas a otras divisas:
    #pesos
    listaPrecios_COP = transformar(listaPrecios_USD,USD_to_COP)

    #euros:
    listaPrecios_EUR = transformar(listaPrecios_USD,USD_to_EUR)

    #libras esterlinas:
    listaPrecios_Libras = transformar(listaPrecios_USD, USD_to_STP)

    #usd to yuan:
    # 1 usd = 6.9 yuan
    # creamos una función en una línea y la llamamos USD_to_YUAN
    # "lambda" es la palabra clave que usamos para definir la función:
    #   x es el parámetro
    #   x * 6.9 es la implementación y el valor que retorna
    USD_to_YUAN = lambda x : x *6.9
    listaPrecios_Yuans = transformar(listaPrecios_USD,USD_to_YUAN)

    #el segundo parámetro sigue siendo una función, en este caso, lambda, definida en una línea:
    lista_con_impuestos = transformar(listaPrecios_USD,    lambda x: x*1.15    )

    #Mostrar:
    print(f"Precios en pesos:{listaPrecios_COP}")
    print(f"Precios en euros:{listaPrecios_EUR}")
    print(f"Precios en libras:{listaPrecios_Libras}")
    print(f"Lista de precios original:{listaPrecios_USD}")

    #TAREA 1:
    # Crear funciones de conversión de precios para los precios de esta lista de productos
    # PISTA: lo que recibe la función que se va a aplicar ya no es un número, sino un par llave/valor

    listaProductos = [ {"producto":"Mouse","precio":20}, {"producto":"Teclado","precio":35},{"producto":"Pantalla","precio":500}   ]

    #Así se accede a un atributo de un par llave/valor (diccionario)
    productoNuevo = {"producto":"MemoriaRam","precio":1500}
    print(f"Precio de la RAM:{productoNuevo['precio']}")

    listaProductos.append(productoNuevo)

    #como acceder al precio de un producto:

    #primero se accede al índice la lista y luego al valor de la llave:
    # precio del producto 2
    precioPantalla = listaProductos[2]["precio"]
    print(f"Precio de la pantalla:{precioPantalla}")

    
