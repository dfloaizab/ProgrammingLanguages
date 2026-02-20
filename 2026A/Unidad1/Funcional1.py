# SISTEMA DE HABILIDADES DE UN RPG (ROLE PLAYING GAME):

# 1. Definicion de funciones puras para manejo de health-points (hp):
# (funciones que no alteran el valor de los parámetros)
def curar(hp_actual):
    new_hp = hp_actual + 10
    return new_hp

def recibir_danio(hp_actual):
    new_hp = hp_actual - 10
    return new_hp

def ayuda_divina(hp_actual):
    new_hp = hp_actual + 25
    return new_hp

# 2. funciones como objetos:
# lista de funciones:
habilidades = [curar, recibir_danio, ayuda_divina]

#Aplica "curar","recibir_danio","ayuda divina" o "ataque critico"
# y retorna un valor:
def aplicar_habilidad(hp_actual, indice_funcion):
    return habilidades[indice_funcion](hp_actual)

# retorna una funcion
def devolver_habilidad(indice_funcion):
    return habilidades[indice_funcion]

# una función que retorna otra función:
def crear_hechizo(puntos):
    #funciones "inline":
    def hechizo(hp_actual):
        return hp_actual + puntos    
    return hechizo

# ejemplo de la función "crear_hechizo":
hechizo_pequenio = crear_hechizo(5)
hechizo_grande = crear_hechizo(15)

# vamos a agregar una nueva habilidad a la lista de habilidades: "ataque_critico", como una función lambda
habilidades.append(lambda hp_actual: hp_actual - 30)

#Aplicación de las habilidades o funcionalidades de los health-points:
if __name__ == "__main__":

    print("--- SIMULADOR DE HABILIDADES DE RPG BÁSICO ---")

    my_healthPoints = 100
    print(f"\nMis health points iniciales:{my_healthPoints}")
    print("Habilidades:\n")
    # Estas 4 están en el arreglo de habilidades:
    print("\n0. Curar")
    print("\n1. recibir danio.")
    print("\n2. Ayuda divina")
    print("\n3. Ataque crítico")

    #...estas no están en el arreglo
    print("\n4. Aplicar hechizo pequeño")
    print("\n5. Aplicar hechizo grande")

    cual_habilidad = int(input("¿Qué funcionalidad desea aplicar?") )

    # Devuelve una función...
    if cual_habilidad >= 0 and cual_habilidad < 4:
        nuevoHealthPoints = aplicar_habilidad(my_healthPoints,cual_habilidad)      
    elif cual_habilidad == 4:
        nuevoHealthPoints = hechizo_pequenio(my_healthPoints)
    elif cual_habilidad == 5:
        nuevoHealthPoints = hechizo_grande(my_healthPoints)

    print(f"Nuevo health-points:{nuevoHealthPoints}")
    print(f"Health points originales:{my_healthPoints}")
