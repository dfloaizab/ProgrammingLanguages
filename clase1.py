
#Hands on introduction to python:
# 1 Function definition
# 2 Dynamic types and type conversion

def validar_edad_pension(s):
    if s >= 65:
        return True
    else:
        return False
        

#Se puede hacer cast:
edad_s = float(input("Cuál es tu edad?: "))
se_pensiona = validar_edad_pension(edad_s)
print(se_pensiona)


# print("hola mundo")
# #Input siempre devuelve un dato de tipo "str"
# nombre = input("Cómo te llamas?")
# #Se puede hacer cast:
# edad_s = float(input("Cuál es tu edad?: "))
# sem_cotizadas = int(input("Cuántas semanas cotizadas tienes?:"))

# #Otras funciones de cast:
# #  float, complex, bool, list, dict, 

# print(type(edad_s))

# #print con formato, para mostrar el valor de la variable edad_s
# print(f"Tu edad es: {edad_s}")

# #Validar si se pensiona por las semanas cotizadas:
 
# if sem_cotizadas >= 1400:
#     print("Ya puedes reclamar tu pensión")
# else:
#     print("Aún no puedes pensionarte. A seguir laburando!")




