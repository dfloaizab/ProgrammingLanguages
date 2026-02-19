def pedir_datos():
    print("Hola Mundo")
    nombre = "Diego"
    edad = 30
    estatura = 1.60
    temperatura = 36.5
    salario = 1500000.0
    fuma = False
    Mascotas = ["Kira","Sabina","Falkor","Pitufa"] #Lista
    Curso1 = {"Nombre":"Lenguajes de Prog","Creditos":3,"NotaFinal":5.0,"Habilita":False} #Diccionario
    Curso2 = {"Nombre":"Bases de Datos","Creditos":4,"NotaFinal":4.8,"Habilita":False} #Diccionario
    Cursos = [Curso1, Curso2] #Lista
    direccion_domicilio = input("Ingrese su domicilio:")
    peso = float(input("Ingrese su peso aproximado:"))
    casado = bool(input("Es casado?"))

    print(type(nombre))
    print(type(edad))
    print(type(Mascotas))
    print(type(salario))
    print(type(fuma))
    print(type(Curso1))
    print(type(Cursos))
    print(type(peso))
    print(type(casado))

    print(f"El estudiante {nombre} tiene {edad} años, mide {estatura} m. Es casado?:{casado}")

