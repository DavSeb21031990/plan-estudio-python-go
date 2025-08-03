## Tipos de operadores
Python tiene varios tipos de operadores, cada uno para un propósito diferente:
### Operadores matemáticos
Se usan para realizar operaciones matemáticas comunes.

- **`+` (Suma):** Suma dos valores.
    ```python
    resultado = 10 + 5  # resultado es 15
    ```
- **`-` (Resta):** Resta el segundo valor del primero.
    ```python
    resultado = 10 - 5  # resultado es 5
    ```
- **`*` (Multiplicación):** Multiplica dos valores.
    ```python
    resultado = 10 * 5  # resultado es 50
    ```
- **`/` (División):** Divide el primer valor por el segundo. Siempre devuelve un **número flotante** (con decimales).
    ```python
    resultado = 10 / 3  # resultado es 3.333...
    ```
- **`%` (Módulo/Resto):** Devuelve el resto de una división.
    ```python
    resultado = 10 % 3  # resultado es 1 (porque 10 dividido 3 es 3 con un resto de 1)
    ```
- **`**` (Exponenciación):** Eleva el primer valor a la potencia del segundo.
    ```python
    resultado = 2 ** 3  # resultado es 8 (2 elevado a la 3)
    ```
- **`//` (División Entera):** Divide y devuelve solo la parte entera del resultado (redondea hacia abajo).
    ```python
    resultado = 10 // 3 # resultado es 3
    ```
### Operadores de asignación
Se usan para asignar valores a variables. Ya conoces el ` = ` básico.

- **` = ` (Asignación):** Asigna el valor de la derecha a la variable de la izquierda.
    ```python
    x = 10
    ```
- **`+=` (Suma y Asigna):** Suma el valor de la derecha al de la variable y asigna el resultado a la misma variable. Es un atajo para `x = x + 5`.
    ```python
    x = 10
    x += 5      # x ahora es 15
    ```
- **`-=` (Resta y Asigna):** `x = x - 5`
    ```python
    x = 10
    x -= 5      # x ahora es 5
    ```
- **`*=` (Multiplica y Asigna):** `x = x * 5`
    ```python
    x = 10
    x *= 5      # x ahora es 50
    ```
- **`/=` (Divide y Asigna):** `x = x / 5`
    ```python
    x = 10
    x /= 5      # x ahora es 2.0
    ```
    
- Y así sucesivamente con `%=`, `**=`, `//=` para el resto de operadores aritméticos.
### Operadores de comparación (o relacional)
Se usan para comparar dos valores y siempre devuelven un valor **booleano** (`True` o `False`).

- **` == ` (Igual a):** Comprueba si dos valores son iguales.
    ```python
    print(5 == 5)   # True
    print(5 == 10)  # False
    ```
- **`!=` (Diferente de):** Comprueba si dos valores son diferentes.
    ```python
    print(5 != 10)  # True
    print(5 != 5)   # False
    ```
- **`>` (Mayor que):**
    ```python
    print(10 > 5)   # True
    ```
- **`<` (Menor que):**
    ```python
    print(5 < 10)   # True
    ```
- **`>=` (Mayor o igual que):**
    ```python
    print(10 >= 10) # True
    ```
- **`<=` (Menor o igual que):**
    ```python
    print(5 <= 10)  # True
    ```
### Operadores lógicos
Se usan para combinar expresiones condicionales.

- **`and` (Y lógico):** Devuelve `True` si **ambas** condiciones son verdaderas.
    ```python
    print(True and True)    # True
    print(True and False)   # False
    ```
- **`or` (O lógico):** Devuelve `True` si **al menos una** de las condiciones es verdadera.
    ```python
    print(True or False)    # True
    print(False or False)   # False
    ```
- **`not` (Negación lógica):** Invierte el valor booleano. `not True` es `False`, `not False` es `True`.
    ```python
    print(not True)         # False
    ```
### Operadores de identidad
Comparan si dos variables **apuntan al mismo objeto** en la memoria.

- **`is`:** Devuelve `True` si ambas variables se refieren al mismo objeto.
- **`is not`:** Devuelve `True` si las variables no se refieren al mismo objeto.
    
    ```python
    lista1 = [1, 2, 3]
    lista2 = [1, 2, 3]
    lista3 = lista1 # lista3 ahora apunta al mismo objeto que lista1
    
    print(lista1 is lista2) # False (son objetos diferentes, aunque tengan el mismo contenido)
    print(lista1 is lista3) # True (apuntan al mismo objeto en memoria)
    ```
### Operadores de pertenencia
Se usan para verificar si un valor o una secuencia de valores está **presente en una secuencia** (como una cadena de texto, una lista, una tupla o un diccionario).

- **`in`:** Devuelve `True` si el valor está presente.
- **`not in`:** Devuelve `True` si el valor no está presente.
    
    ```python
    mi_cadena = "Hola Mundo"
    mi_lista = [10, 20, 30, 40]
    
    print("Mundo" in mi_cadena)     # True
    print("Python" not in mi_cadena) # True
    print(20 in mi_lista)           # True
    print(50 in mi_lista)           # False
    ```
## Orden de Precedencia
Al igual que en matemáticas, los operadores en Python tienen un orden de precedencia. Esto determina qué operación se realiza primero en una expresión compleja. Por ejemplo, la multiplicación y la división se realizan antes que la suma y la resta. Puedes usar **paréntesis `()`** para anular la precedencia y forzar un orden específico.

```python
resultado = 10 + 5 * 2 # 5 * 2 se hace primero (10), luego 10 + 10 = 20
print(resultado)       # Salida: 20

resultado_parentesis = (10 + 5) * 2 # (10 + 5) se hace primero (15), luego 15 * 2 = 30
print(resultado_parentesis) # Salida: 30
```

---

⬅️[Inicio](../../../README.md)