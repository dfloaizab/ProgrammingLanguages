# Ejercicio: Programación funcional sobre datos de humedales de Cali (parte 1)

## Contexto

Partiendo de las funciones `LoadData` (evaluación *eager*) y `LoadData_lazy`
(evaluación *lazy*, mediante `yield`) que ya cargan el archivo
`dataset1.csv` en memoria como una lista de diccionarios, se pide extender
ese código aplicando **conceptos básicos de programación funcional**:
funciones de orden superior, funciones puras, comprensión de listas,
composición de funciones y evaluación perezosa.

Cada registro del dataset tiene esta forma:

```python
{"nombre": "Humedal El Retiro",
 "direccion": "Comuna 22, zona sur de Cali",
 "hectareas": 3.5,
 "aves": 42,
 "flora": 60,
 "estado": "Regular"}
```

## Objetivos de aprendizaje

- Usar `map`, `filter` y `functools.reduce` en lugar de bucles `for` explícitos.
- Distinguir cuándo conviene una comprensión de listas frente a `map`/`filter`.
- Escribir funciones puras (sin efectos secundarios, sin modificar el dataset original).
- Comprender la diferencia práctica entre evaluación *eager* y *lazy* al encadenar transformaciones.
- Componer funciones pequeñas para construir un pipeline de procesamiento de datos.

## Instrucciones

Completar cada función marcada con `# TODO` en `plantilla.py`. No está
permitido usar bucles `for`/`while` explícitos dentro de las funciones del
ejercicio (sí se pueden usar dentro de comprensiones, que no cuentan como
bucle explícito). El archivo `dataset1.csv` debe cargarse con las funciones
ya existentes (`LoadData` / `LoadData_lazy`), sin modificarlas.

### Punto 1 — `filtrar_por_estado(dataset, estado)`
Usando `filter`, retornar únicamente los registros cuyo campo `"estado"`
coincida (ignorando mayúsculas/minúsculas y espacios) con el parámetro
`estado`.

### Punto 2 — `extraer_nombres(dataset)`
Usando `map`, retornar una lista solo con los nombres de los humedales.

### Punto 3 — `total_hectareas(dataset)`
Usando `functools.reduce`, calcular la suma total de hectáreas de todos
los humedales del dataset.

### Punto 4 — `promedio_biodiversidad(dataset)`
Usando `functools.reduce` (no `sum()` directamente), calcular el promedio
de `aves + flora` por humedal.

### Punto 5 — `resumen_por_estado(dataset)`
Usando **comprensión de diccionarios**, construir un diccionario donde
cada clave sea un `estado` distinto presente en el dataset y cada valor
sea la cantidad de humedales en ese estado. (Pista: puede apoyarse en
`extraer_estados` con `map` + `set` para obtener las claves).

### Punto 6 — `humedales_criticos_lazy(fileName, hectareas_min)`
Usando `LoadData_lazy` y `filter` (no `LoadData`), retornar un **generador**
que produzca únicamente los humedales cuyo estado sea `"Deteriorado"` **o**
cuyas hectáreas sean menores a `hectareas_min`. La función no debe recorrer
ni convertir el generador a lista dentro de su propio cuerpo — la pereza
(*laziness*) debe conservarse para quien la consuma.

Verificar el comportamiento perezoso con:

```python
gen = humedales_criticos_lazy("dataset1.csv", 3.0)
print(next(gen))   # solo procesa hasta encontrar el primer resultado
print(next(gen))
```

### Punto 7 (bonus) — `componer(*funciones)`
Escribir una función `componer` que reciba una cantidad variable de
funciones de un solo argumento y retorne una nueva función que las aplique
en cadena, de derecha a izquierda (como la composición matemática
`f(g(x))`). Usarla para construir, en una sola línea, un pipeline que:
1. filtre humedales con `estado == "Bueno"`,
2. extraiga sus nombres,
3. los ordene alfabéticamente.

## Preguntas de reflexión (responder en 3-5 líneas cada una)

1. Si `dataset1.csv` tuviera 2 millones de registros, ¿qué diferencia de
   rendimiento y de uso de memoria esperarías entre resolver el Punto 6 con
   `LoadData` (eager) contra `LoadData_lazy` (lazy)?
2. ¿Por qué se considera que `filtrar_por_estado` y `extraer_nombres` son
   funciones puras? ¿Qué las haría dejar de serlo?
3. `map`/`filter` retornan objetos iteradores en Python 3, no listas. ¿Qué
   implicación tiene esto si se intenta iterar dos veces sobre el mismo
   resultado de un `map`?

## Criterios de evaluación

| Criterio | Puntos |
|---|---|
| Puntos 1 a 5 correctos y sin bucles explícitos | 50% |
| Punto 6 (generador realmente perezoso, verificado con `next`) | 25% |
| Punto 7 (bonus) | hasta 10% adicional |
| Respuestas de reflexión, justificadas y correctas | 25% |

## Archivos entregados

- `dataset1.csv`: dataset de ejemplo (humedales de Cali).
- `plantilla.py`: código base con las funciones a completar.
- `LoadData` y `LoadData_lazy` deben mantenerse sin modificaciones.
