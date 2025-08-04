---
title: 'Listas Comprehensions'
description: 'Guia para Listas Comprehensions'
---

Las **List Comprehensions** (comprensiones de lista) son una de las características más elegantes y potentes de Python para **crear listas de forma concisa**. Te permiten construir una nueva lista aplicando una expresión a cada elemento de un iterable existente, y opcionalmente, filtrando esos elementos. Son una alternativa más corta y a menudo más legible que un bucle `for` tradicional para la creación de listas.

Imagina que quieres crear una lista a partir de otra lista, pero con alguna modificación en cada elemento, o solo incluyendo algunos elementos que cumplen una condición. Las List Comprehensions hacen esto de una manera muy compacta.

---
### La Estructura Básica
La sintaxis general de una List Comprehension es la siguiente:
```python
[expresión for elemento in iterable if condición]
```
Desglosemos cada parte:
- **`expresión`**: Es lo que se va a evaluar para cada `elemento`. El resultado de esta expresión será un elemento en la nueva lista.
- **`for elemento in iterable`**: Esta es la parte del bucle `for` que itera sobre los elementos de un `iterable` (como una lista, tupla, cadena, rango, etc.).
- **`if condición` (opcional)**: Es una condición opcional que filtra los `elementos`. Solo los elementos para los cuales la `condición` es `True` serán incluidos en la nueva lista.
---
### Ejemplos Prácticos
Veamos cómo las List Comprehensions simplifican el código:
#### 1. Transformación de Elementos
**Problema:** Queremos crear una lista de los cuadrados de los números del 1 al 5.
**Con un bucle `for` tradicional:**
```python
cuadrados = []
for numero in range(1, 6):
    cuadrados.append(numero ** 2)
print(f"Cuadrados (bucle for): {cuadrados}")
# Salida: Cuadrados (bucle for): [1, 4, 9, 16, 25]
```
**Con List Comprehension:**
```python
cuadrados_lc = [numero ** 2 for numero in range(1, 6)]
print(f"Cuadrados (List Comp.): {cuadrados_lc}")
# Salida: Cuadrados (List Comp.): [1, 4, 9, 16, 25]
```
¡Mucho más conciso! La expresión es `numero ** 2`, el elemento es `numero`, y el iterable es `range(1, 6)`.
#### 2. Filtrado de Elementos
**Problema:** Queremos crear una lista de solo los números pares del 1 al 10.
**Con un bucle `for` tradicional:**
```python
numeros_pares = []
for numero in range(1, 11):
    if numero % 2 == 0:
        numeros_pares.append(numero)
print(f"Números pares (bucle for): {numeros_pares}")
# Salida: Números pares (bucle for): [2, 4, 6, 8, 10]
```
**Con List Comprehension:**
```python
numeros_pares_lc = [numero for numero in range(1, 11) if numero % 2 == 0]
print(f"Números pares (List Comp.): {numeros_pares_lc}")
# Salida: Números pares (List Comp.): [2, 4, 6, 8, 10]
```
Aquí, la expresión es simplemente `numero`, la condición es `if numero % 2 == 0`.
#### 3. Transformación y Filtrado Combinados
**Problema:** Queremos una lista de los cuadrados de los números impares del 1 al 10.
**Con List Comprehension:**
```python
cuadrados_impares_lc = [numero ** 2 for numero in range(1, 11) if numero % 2 != 0]
print(f"Cuadrados de impares (List Comp.): {cuadrados_impares_lc}")
# Salida: Cuadrados de impares (List Comp.): [1, 9, 25, 49, 81]
```
#### 4. Con Cadenas de Texto
**Problema:** Queremos una lista de las longitudes de las palabras en una lista de cadenas, solo para palabras que tengan más de 5 letras.
```python
palabras = ["manzana", "platano", "kiwi", "fresa", "uva", "naranja"]
longitudes_grandes = [len(palabra) for palabra in palabras if len(palabra) > 5]
print(f"Longitudes de palabras grandes: {longitudes_grandes}")
# Salida: Longitudes de palabras grandes: [7, 7, 7] (manzana, platano, naranja)
```
#### 5. List Comprehension Anidada (Para matrices, por ejemplo)
También puedes anidar List Comprehensions para manejar estructuras más complejas como matrices.
**Problema:** Crear una matriz 3x3 donde cada elemento es la suma de su índice de fila y columna.
```python
matriz = [[i + j for j in range(3)] for i in range(3)]
print(f"Matriz 3x3: {matriz}")
# Salida: Matriz 3x3: [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
```
---
### Ventajas de Usar List Comprehensions
- **Concisión:** Reducen el número de líneas de código, haciendo el programa más compacto.
- **Legibilidad:** Una vez que te familiarizas con su sintaxis, suelen ser más fáciles de leer y entender que los bucles `for` equivalentes, especialmente para transformaciones y filtrados simples.
- **Eficiencia:** A menudo, las List Comprehensions son más rápidas que los bucles `for` tradicionales para el mismo propósito, ya que están optimizadas internamente en CPython.
### Cuándo NO Usar List Comprehensions
Aunque son muy útiles, hay situaciones en las que un bucle `for` tradicional es más apropiado:
- **Lógica compleja:** Si la lógica dentro de la comprensión de lista se vuelve demasiado compleja (varias condiciones `if`, expresiones muy largas, múltiples operaciones), es mejor usar un bucle `for` para mantener la legibilidad.
- **Efectos secundarios:** Si necesitas realizar operaciones que no solo crean la lista (como imprimir mensajes, modificar variables externas, etc.), un bucle `for` es más adecuado. Las List Comprehensions están diseñadas para _producir_ una nueva lista.