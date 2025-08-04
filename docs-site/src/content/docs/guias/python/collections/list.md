---
title: 'Listas'
description: 'Guia para Listas'
---

## 1. Creación de Listas

Las listas se crean encerrando una secuencia de elementos entre corchetes `[]`, separados por comas. Una lista puede contener elementos de diferentes tipos de datos (enteros, flotantes, cadenas, booleanos, incluso otras listas).
**Ejemplos:**
```python
# Lista de números enteros
numeros = [1, 2, 3, 4, 5]
print(f"Lista de números: {numeros}")

# Lista de cadenas
frutas = ["manzana", "banana", "cereza"]
print(f"Lista de frutas: {frutas}")

# Lista con diferentes tipos de datos
mixta = [10, "hola", 3.14, True]
print(f"Lista mixta: {mixta}")

# Lista vacía
lista_vacia = []
print(f"Lista vacía: {lista_vacia}")

# Crear una lista a partir de un iterable (por ejemplo, una cadena)
letras = list("python")
print(f"Lista de letras: {letras}") # Salida: ['p', 'y', 't', 'h', 'o', 'n']
```
### 2. Acceso a Elementos de una Lista
Puedes acceder a elementos individuales de una lista utilizando su índice. Los índices en Python comienzan en `0` para el primer elemento. También puedes usar índices negativos para acceder a elementos desde el final de la lista (`-1` para el último elemento, `-2` para el penúltimo, etc.).
**Ejemplos:**
```python
frutas = ["manzana", "banana", "cereza", "dátil"]

# Acceder al primer elemento (índice 0)
print(f"Primera fruta: {frutas[0]}") # Salida: manzana

# Acceder al tercer elemento (índice 2)
print(f"Tercera fruta: {frutas[2]}") # Salida: cereza

# Acceder al último elemento (índice -1)
print(f"Última fruta: {frutas[-1]}") # Salida: dátil

# Acceder al penúltimo elemento (índice -2)
print(f"Penúltima fruta: {frutas[-2]}") # Salida: cereza

# Intentar acceder a un índice fuera de rango generará un IndexError
# print(frutas[10]) # Esto causaría un error
```
### 3. Slicing (Rebanado) de Listas
El slicing te permite obtener una sublista (una "rebanada") de una lista existente. Se especifica utilizando la notación `[inicio:fin:paso]`:
- `inicio`: El índice donde comienza la rebanada (incluido). Si se omite, se asume `0`.
- `fin`: El índice donde termina la rebanada (excluido). Si se omite, se asume el final de la lista.
- `paso`: El incremento entre los índices (opcional). Si se omite, se asume `1`.
**Ejemplos:**
```python
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Rebanada desde el índice 2 hasta el 5 (excluido)
print(f"numeros[2:5]: {numeros[2:5]}") # Salida: [2, 3, 4]

# Rebanada desde el principio hasta el índice 4 (excluido)
print(f"numeros[:4]: {numeros[:4]}") # Salida: [0, 1, 2, 3]

# Rebanada desde el índice 6 hasta el final
print(f"numeros[6:]: {numeros[6:]}") # Salida: [6, 7, 8, 9]

# Rebanada de toda la lista (crea una copia)
print(f"numeros[:]: {numeros[:]}") # Salida: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Rebanada con paso (cada 2 elementos)
print(f"numeros[::2]: {numeros[::2]}") # Salida: [0, 2, 4, 6, 8]

# Rebanada inversa ([::-1] es una forma común de invertir una lista)
print(f"numeros[::-1]: {numeros[::-1]}") # Salida: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Rebanada con inicio, fin y paso
print(f"numeros[1:8:3]: {numeros[1:8:3]}") # Salida: [1, 4, 7]
```
### 4. Métodos Comunes de Listas
Las listas tienen varios métodos integrados que te permiten realizar operaciones como agregar, eliminar, ordenar y obtener información sobre los elementos.
#### 4.1. `append()`
Agrega un elemento al final de la lista.

```python
colores = ["rojo", "verde"]
colores.append("azul")
print(f"Después de append('azul'): {colores}") # Salida: ['rojo', 'verde', 'azul']
```
#### 4.2. `insert()`
Inserta un elemento en una posición específica de la lista. Toma dos argumentos: el índice donde insertar y el elemento a insertar.
```python
animales = ["perro", "gato"]
animales.insert(1, "conejo") # Inserta "conejo" en el índice 1
print(f"Después de insert(1, 'conejo'): {animales}") # Salida: ['perro', 'conejo', 'gato']
```
#### 4.3. `remove()`
Elimina la primera aparición de un valor específico de la lista. Si el valor no se encuentra, genera un `ValueError`.
```python
frutas = ["manzana", "banana", "cereza", "banana"]
frutas.remove("banana")
print(f"Después de remove('banana'): {frutas}") # Salida: ['manzana', 'cereza', 'banana']
```
#### 4.4. `pop()`
Elimina y devuelve el elemento en un índice específico. Si no se especifica un índice, `pop()` elimina y devuelve el último elemento de la lista.
```python
numeros = [10, 20, 30, 40, 50]

# Eliminar y obtener el elemento en el índice 2
elemento_eliminado = numeros.pop(2)
print(f"Elemento eliminado con pop(2): {elemento_eliminado}") # Salida: 30
print(f"Lista después de pop(2): {numeros}") # Salida: [10, 20, 40, 50]

# Eliminar y obtener el último elemento
ultimo_elemento = numeros.pop()
print(f"Último elemento eliminado con pop(): {ultimo_elemento}") # Salida: 50
print(f"Lista después de pop(): {numeros}") # Salida: [10, 20, 40]
```
#### 4.5. `sort()`
Ordena los elementos de la lista en su lugar (modifica la lista original). Por defecto, ordena en orden ascendente. Puedes usar `reverse=True` para ordenar en orden descendente.
```python
numeros = [3, 1, 4, 1, 5, 9, 2]
numeros.sort()
print(f"Lista ordenada ascendente: {numeros}") # Salida: [1, 1, 2, 3, 4, 5, 9]

letras = ["c", "a", "b"]
letras.sort(reverse=True)
print(f"Lista ordenada descendente: {letras}") # Salida: ['c', 'b', 'a']

# Nota: sort() funciona con elementos del mismo tipo de datos o que sean comparables
```
#### 4.6. `len()` (Función incorporada, no un método de lista)
La función `len()` se utiliza para obtener la longitud (número de elementos) de una lista.

```python
frutas = ["manzana", "banana", "cereza"]
longitud = len(frutas)
print(f"Longitud de la lista de frutas: {longitud}") # Salida: 3

lista_vacia = []
print(f"Longitud de la lista vacía: {len(lista_vacia)}") # Salida: 0
```
### Otros Métodos Comunes (Bonus)
- `count()`: Devuelve el número de veces que un valor específico aparece en la lista.
    ```python
    numeros = [1, 2, 2, 3, 2, 4]
    conteo_dos = numeros.count(2)
    print(f"El número 2 aparece {conteo_dos} veces.") # Salida: 3
    ```
- `index()`: Devuelve el índice de la primera aparición de un valor específico. Si el valor no se encuentra, genera un `ValueError`.
    ```python
    frutas = ["manzana", "banana", "cereza"]
    indice_banana = frutas.index("banana")
    print(f"El índice de 'banana' es: {indice_banana}") # Salida: 1
    ```
- `extend()`: Agrega los elementos de un iterable (como otra lista) al final de la lista actual.
    ```python
    lista1 = [1, 2]
    lista2 = [3, 4]
    lista1.extend(lista2)
    print(f"Lista después de extend: {lista1}") # Salida: [1, 2, 3, 4]
    ```
- `reverse()`: Invierte el orden de los elementos de la lista en su lugar.
    ```python
    numeros = [1, 2, 3, 4]
    numeros.reverse()
    print(f"Lista invertida: {numeros}") # Salida: [4, 3, 2, 1]
    ```
- `clear()`: Elimina todos los elementos de la lista, dejándola vacía.
    ```python
    frutas = ["manzana", "banana"]
    frutas.clear()
    print(f"Lista después de clear: {frutas}") # Salida: []
    ```