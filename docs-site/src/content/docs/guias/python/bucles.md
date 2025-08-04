---
title: 'Bucles'
description: 'Guia para bucles'
---

Los **bucles** son otra herramienta fundamental en programación, tan importantes como las sentencias condicionales. Permiten que tu programa **repita un bloque de código** varias veces, lo que es increíblemente útil para tareas repetitivas, procesar colecciones de datos o esperar a que se cumpla una condición. Python ofrece dos tipos principales de bucles: `for` y `while`.

---
### Bucle `for`: Iteración sobre Secuencias
El bucle `for` se utiliza para **iterar** (recorrer) elementos en una **secuencia** (como listas, tuplas, cadenas de texto, rangos, etc.) o cualquier objeto "iterable". En cada iteración, una variable toma el valor del siguiente elemento de la secuencia.
#### Sintaxis
```python
for variable_iteracion in secuencia:
    # Código a ejecutar en cada iteración
    # (Este código debe estar indentado)
```
#### ¿Cómo funciona?
1. Python toma el primer elemento de la `secuencia` y lo asigna a `variable_iteracion`.
2. Ejecuta el bloque de código indentado.
3. Toma el segundo elemento, lo asigna a `variable_iteracion`, y repite el proceso.
4. Esto continúa hasta que se han procesado todos los elementos de la `secuencia`.
#### Ejemplos
- **Recorriendo una lista:**
    ```python
    frutas = ["manzana", "banana", "cereza"]
    for fruta in frutas:
        print(f"Me gusta comer {fruta}.")
    ```
    _Salida:_
    ```
    Me gusta comer manzana.
    Me gusta comer banana.
    Me gusta comer cereza.
    ```
- **Recorriendo una cadena de texto:**
    ```python
    saludo = "Hola"
    for letra in saludo:
        print(letra)
    ```
    _Salida:_
    ```
    H
    o
    l
    a
    ```
- **Usando `range()` para un número específico de repeticiones:** La función `range()` es muy común con los bucles `for` para generar una secuencia de números.
    - `range(5)` genera números del 0 al 4 (5 números en total).
    - `range(1, 6)` genera números del 1 al 5.
    - `range(0, 10, 2)` genera números pares del 0 al 8 (paso de 2).
    ```python
    for i in range(3): # Repite 3 veces (i tomará valores 0, 1, 2)
        print("Iteración número", i)
    
    for numero in range(1, 5): # Del 1 al 4
        print(f"El número es {numero}")
    ```
    _Salida:_
    ```
    Iteración número 0
    Iteración número 1
    Iteración número 2
    El número es 1
    El número es 2
    El número es 3
    El número es 4
    ```
---
### Bucle `while`: Repetir mientras una Condición sea Verdadera
El bucle `while` se utiliza para **repetir un bloque de código mientras una condición específica sea verdadera**. Es decir, el bucle continúa ejecutándose hasta que la condición se vuelve falsa.
#### Sintaxis
```python
while condicion:
    # Código a ejecutar mientras la condición sea True
    # (Este código debe estar indentado)
```
#### ¿Cómo funciona?
1. Python evalúa la `condicion`.
2. Si la `condicion` es `True`, el bloque de código indentado se ejecuta.
3. Después de ejecutar el bloque, Python vuelve a evaluar la `condicion`.
4. Si sigue siendo `True`, el bloque se ejecuta de nuevo.
5. Este proceso se repite hasta que la `condicion` se vuelve `False`.
6. Si la `condicion` es `False` desde el principio, el bloque de código nunca se ejecuta.
#### Ejemplos
- **Contador simple:**
    ```python
    contador = 0
    while contador < 5:
        print("El contador es", contador)
        contador += 1 # Es crucial actualizar la condición para evitar un bucle infinito
    ```
    _Salida:_
    ```
    El contador es 0
    El contador es 1
    El contador es 2
    El contador es 3
    El contador es 4
    ```
    **¡Cuidado con los bucles infinitos!** Si la condición de un bucle `while` nunca se vuelve `False`, el programa se ejecutará indefinidamente, lo que puede bloquear tu sistema. Asegúrate siempre de que haya una forma de que la condición se evalúe a `False` en algún momento.
- **Validación de entrada de usuario:**
    ```python
    contrasena = ""
    while contrasena != "secreto":
        contrasena = input("Introduce la contraseña: ")
        if contrasena != "secreto":
            print("Contraseña incorrecta. Inténtalo de nuevo.")
    print("¡Acceso concedido!")
    ```
    _Ejemplo de interacción:_
    ```
    Introduce la contraseña: hola
    Contraseña incorrecta. Inténtalo de nuevo.
    Introduce la contraseña: mundo
    Contraseña incorrecta. Inténtalo de nuevo.
    Introduce la contraseña: secreto
    ¡Acceso concedido!
    ```
---
### Sentencias de Control de Bucle: `break` y `continue`
Dentro de los bucles, puedes usar dos sentencias especiales para alterar su flujo normal: `break` y `continue`.
#### `break`: Romper el Bucle
La sentencia `break` se usa para **terminar inmediatamente el bucle** en el que se encuentra. Tan pronto como Python encuentra `break`, sale del bucle y el programa continúa con la primera línea de código después del bucle.
```python
for numero in range(1, 10):
    if numero == 5:
        print("Encontré el 5. ¡Rompiendo el bucle!")
        break # Sale del bucle for
    print(numero)

print("El bucle ha terminado.")
```
_Salida:_
```
1
2
3
4
Encontré el 5. ¡Rompiendo el bucle!
El bucle ha terminado.
```
#### `continue`: Saltar a la Siguiente Iteración
La sentencia `continue` se usa para **saltar el resto del código en la iteración actual del bucle** y pasar directamente a la siguiente iteración. El bucle no termina; simplemente omite las sentencias restantes para la iteración actual.
```python
for i in range(1, 6):
    if i % 2 == 0: # Si el número es par
        print(f"Saltando el número par: {i}")
        continue # Pasa a la siguiente iteración sin imprimir la línea de abajo
    print(f"Procesando número impar: {i}")
```
_Salida:_
```
Procesando número impar: 1
Saltando el número par: 2
Procesando número impar: 3
Saltando el número par: 4
Procesando número impar: 5
```