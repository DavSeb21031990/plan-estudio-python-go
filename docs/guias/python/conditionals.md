## Concepto de condición
Una condición en programación es una expresión que se evalúa como **verdadera (`True`)** o **falsa (`False`)**. Para crear estas condiciones, usamos los **operadores de comparación** que vimos antes (como ` == `, `!=`, `<`, `>`, `<=`, `>=`) y a veces los **operadores lógicos** (`and`, `or`, `not`).
**Ejemplos de condiciones:**
- `edad >= 18` (¿La edad es mayor o igual a 18?)
- `temperatura < 0` (¿La temperatura es menor que cero?)
- `nombre == "Juan"` (¿El nombre es exactamente "Juan"?)
- `es_dia_laboral and hora_actual < 17` (¿Es día laboral Y la hora es antes de las 5 PM?)
---
## Sentencia `if` (Si)
La sentencia `if` es la más básica y significa: "Si esta condición es verdadera, entonces haz esto".
### Sintaxis
```python
if condicion:
    # Código a ejecutar si la condición es True
    # (Este código debe estar indentado)
```
### ¿Cómo funciona?
1. Python evalúa la `condicion`.
2. Si la `condicion` es `True`, el bloque de código indentado debajo del `if` se ejecuta.
3. Si la `condicion` es `False`, el bloque de código indentado se salta y el programa continúa con la siguiente línea después del bloque `if`.
### Ejemplo
```python
puntuacion = 75

if puntuacion >= 60:
    print("¡Felicidades! Has aprobado el examen.")
```
_Salida:_
```
¡Felicidades! Has aprobado el examen.
```
Si `puntuacion` fuera `50`, la condición `puntuacion >= 60` sería `False`, y el mensaje no se imprimiría.

---
## Sentencia `else` (Si no / De lo contrario)
La sentencia `else` se usa junto con `if` para definir un bloque de código que se ejecutará **cuando la condición del `if` sea falsa**. Es decir, "Si la condición es verdadera, haz esto; **de lo contrario**, haz aquello".
### Sintaxis
```python
if condicion:
    # Código si la condición es True
else:
    # Código si la condición es False
    # (Este código también debe estar indentado)
```
### ¿Cómo funciona?
1. Python evalúa la `condicion` del `if`.
2. Si la `condicion` es `True`, se ejecuta el bloque del `if`.
3. Si la `condicion` es `False`, se ejecuta el bloque del `else`.
4. Solo uno de los dos bloques (o el `if` o el `else`) se ejecutará.
### Ejemplo
```python
edad = 16

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
```
_Salida:_
```
Eres menor de edad.
```
---
## Sentencia `elif` (Si no, si / De lo contrario, si)
La sentencia `elif` (abreviatura de "else if") se utiliza para verificar **múltiples condiciones** de forma secuencial. Te permite encadenar varias pruebas lógicas. Se usa cuando tienes más de dos posibles caminos que tu programa puede tomar.
### Sintaxis
```python
if primera_condicion:
    # Código si la primera_condicion es True
elif segunda_condicion:
    # Código si la primera_condicion fue False Y la segunda_condicion es True
elif tercera_condicion:
    # Código si la primera y segunda fueron False Y la tercera_condicion es True
else:
    # Código si ninguna de las condiciones anteriores fue True
```
### ¿Cómo funciona?
1. Python evalúa la **primera `condicion`** del `if`.
2. Si es `True`, su bloque se ejecuta y el resto de la cadena `elif`/`else` se ignora.
3. Si la primera `condicion` es `False`, Python pasa a evaluar la **primera `elif`**.
4. Si esta es `True`, su bloque se ejecuta y el resto se ignora.
5. Este proceso continúa para cada `elif`.
6. Si **ninguna** de las condiciones (`if` o `elif`) es `True`, entonces el bloque del `else` (si existe) se ejecuta.
7. Solo uno de los bloques dentro de una cadena `if-elif-else` se ejecutará.
### Ejemplo
```python
calificacion = 85

if calificacion >= 90:
    print("Calificación: A")
elif calificacion >= 80:
    print("Calificación: B")
elif calificacion >= 70:
    print("Calificación: C")
else:
    print("Calificación: F")
```
_Salida:_
```
Calificación: B
```
En este ejemplo, `calificacion >= 90` es `False`. Luego, `calificacion >= 80` es `True`, por lo que se imprime "Calificación: B" y el resto de los `elif` y el `else` se ignoran.

---

⬅️[Inicio](../../../README.md)