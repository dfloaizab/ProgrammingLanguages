"""
Ejercicio: Programación funcional sobre datos de humedales de Cali.
Completar cada función marcada con # TODO.
No usar bucles for/while explícitos dentro de las funciones (sí se permiten
dentro de comprensiones, ya que no cuentan como bucle explícito).
"""

from functools import reduce


def LoadData(fileName):
    dataset = []
    with open(fileName, encoding='utf-8') as f:
        for line in f:  # iterar x cada renglón del archivo
            values = line.split(sep=';')
            registro = {"nombre": values[0],
                        "direccion": values[1],
                        "hectareas": float(values[2]),
                        "aves": int(values[3]),
                        "flora": int(values[4]),
                        "estado": values[5].strip()}
            dataset.append(registro)
    return dataset


def LoadData_lazy(fileName):
    with open(fileName, encoding='utf-8') as f:
        for line in f:  # iterar x cada renglón del archivo
            values = line.split(sep=';')
            registro = {"nombre": values[0],
                        "direccion": values[1],
                        "hectareas": float(values[2]),
                        "aves": int(values[3]),
                        "flora": int(values[4]),
                        "estado": values[5].strip()}
            yield registro


# ---------------------------------------------------------------------------
# Punto 1
def filtrar_por_estado(dataset, estado):
    """Retorna los registros cuyo 'estado' coincide con el parámetro dado
    (comparación insensible a mayúsculas/minúsculas y espacios)."""
    # TODO: usar filter()
    pass


# ---------------------------------------------------------------------------
# Punto 2
def extraer_nombres(dataset):
    """Retorna una lista solo con los nombres de los humedales."""
    # TODO: usar map()
    pass


# ---------------------------------------------------------------------------
# Punto 3
def total_hectareas(dataset):
    """Retorna la suma total de hectáreas de todos los humedales."""
    # TODO: usar functools.reduce()
    pass


# ---------------------------------------------------------------------------
# Punto 4
def promedio_biodiversidad(dataset):
    """Retorna el promedio de (aves + flora) por humedal, usando reduce
    (no usar sum() directamente)."""
    # TODO: usar functools.reduce()
    pass


# ---------------------------------------------------------------------------
# Punto 5
def extraer_estados(dataset):
    """Función de apoyo: retorna el conjunto (set) de estados distintos
    presentes en el dataset."""
    # TODO: usar map() + set()
    pass


def resumen_por_estado(dataset):
    """Retorna un diccionario {estado: cantidad_de_humedales_en_ese_estado},
    construido con una comprensión de diccionarios."""
    # TODO: usar comprensión de diccionarios, apoyándose en extraer_estados
    pass


# ---------------------------------------------------------------------------
# Punto 6
def humedales_criticos_lazy(fileName, hectareas_min):
    """Retorna un GENERADOR (no una lista) con los humedales cuyo estado es
    'Deteriorado' o cuyas hectáreas son menores a hectareas_min.
    Debe usar LoadData_lazy y filter(), conservando la evaluación perezosa."""
    # TODO: usar LoadData_lazy(fileName) + filter()
    pass


# ---------------------------------------------------------------------------
# Punto 7 (bonus)
def componer(*funciones):
    """Retorna una nueva función que aplica las funciones recibidas en
    cadena, de derecha a izquierda: componer(f, g)(x) == f(g(x))."""
    # TODO: implementar composición de funciones con reduce
    pass


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    dataset = LoadData("dataset1.csv")

    print("Humedales en estado Deteriorado:")
    print(filtrar_por_estado(dataset, "deteriorado"))

    print("\nNombres de todos los humedales:")
    print(extraer_nombres(dataset))

    print("\nTotal de hectáreas:", total_hectareas(dataset))

    print("\nPromedio de biodiversidad (aves+flora):", promedio_biodiversidad(dataset))

    print("\nResumen por estado:")
    print(resumen_por_estado(dataset))

    print("\nGenerador perezoso (humedales críticos, hectareas_min=3.0):")
    gen = humedales_criticos_lazy("dataset1.csv", 3.0)
    print(next(gen))
    print(next(gen))

    # Punto 7 (bonus): pipeline con composición de funciones
    # pipeline = componer(sorted, extraer_nombres,
    #                      lambda d: filtrar_por_estado(d, "bueno"))
    # print("\nNombres de humedales en buen estado, ordenados:")
    # print(pipeline(dataset))
