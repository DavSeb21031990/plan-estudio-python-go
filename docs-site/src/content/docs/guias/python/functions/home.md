---
title: 'Funciones'
description: 'Guia para funcioneas'
---

En programación, una **función** es como una "mini-programa" o una "receta" reusable. Es un bloque de código organizado y con un nombre que realiza una tarea específica cuando se le llama. Las funciones son esenciales por varias razones:

1. **Reusabilidad:** Escribes el código una vez y puedes usarlo muchas veces en diferentes partes de tu programa, o incluso en otros programas.
    
2. **Modularidad:** Dividen tu programa en partes más pequeñas y manejables, lo que facilita la lectura, el entendimiento y el mantenimiento.
    
3. **Abstracción:** Puedes usar una función sin necesidad de saber exactamente cómo funciona internamente. Solo necesitas saber qué hace y qué información necesita.
## Definición
---
En Python, defines una función usando la palabra clave **`def`**, seguida del nombre de la función, paréntesis `()` y dos puntos `:`. El cuerpo de la función (el código que realiza la tarea) debe estar **indentado**.
#### Sintaxis Básica
```python
def nombre_de_la_funcion():
    # Bloque de código de la función
    # (Todo lo que está indentado aquí pertenece a la función)
    print("¡Hola desde mi primera función!")

# Línea de código fuera de la función (no indentada)
print("Esto está fuera de la función.")
```
#### Llamar a una Función
Una vez que has definido una función, no hace nada por sí misma. Tienes que **"llamarla"** o **"invocarla"** por su nombre seguido de paréntesis para que se ejecute.
```python
def saludar():
    print("¡Hola a todos!")

# Llamando a la función
saludar()
saludar() # Puedes llamarla múltiples veces
```
_Salida:_
```
¡Hola a todos!
¡Hola a todos!
```
---
### Parámetros y Argumentos: Pasando Información a las Funciones
Una de las características más potentes de las funciones es su capacidad para aceptar información desde el exterior. Aquí es donde entran los **parámetros** y los **argumentos**.
- **Parámetros:** Son los **nombres de las variables** que se listan dentro de los paréntesis en la **definición** de la función. Actúan como "espacios de llenado" o "marcadores de posición" para la información que la función necesita para trabajar.
- **Argumentos:** Son los **valores reales** que se pasan a la función cuando se la **llama**. Estos valores son los que llenan los "espacios" definidos por los parámetros.
#### Ejemplo
```python
# 'nombre' y 'mensaje' son PARÁMETROS
def saludar_personalizado(nombre, mensaje):
    print(f"Hola, {nombre}. {mensaje}")

# 'Ana' y 'Bienvenida al curso.' son ARGUMENTOS
saludar_personalizado("Ana", "Bienvenida al curso.")

# 'Pedro' y 'Que tengas un buen día.' también son ARGUMENTOS
saludar_personalizado("Pedro", "Que tengas un buen día.")
```
_Salida:_
```
Hola, Ana. Bienvenida al curso.
Hola, Pedro. Que tengas un buen día.
```
En este ejemplo:
- Cuando llamamos `saludar_personalizado("Ana", "Bienvenida al curso.")`, el valor `"Ana"` se asigna al parámetro `nombre` y `"Bienvenida al curso."` al parámetro `mensaje` dentro de la función.
- Luego, la función usa esos valores para construir el mensaje.
---
### Tipos de Argumentos (y sus Parámetros correspondientes)
Python ofrece flexibilidad en cómo pasas los argumentos a una función:
1. **Argumentos Posicionales (Obligatorios):** Son los más comunes. Los argumentos se asignan a los parámetros en el orden en que aparecen. Si no pasas un argumento para un parámetro posicional, Python generará un error.
    ```python
    def describir_persona(nombre, edad):
        print(f"{nombre} tiene {edad} años.")
    
    describir_persona("Luis", 25) # "Luis" va a 'nombre', 25 a 'edad'
    # describir_persona(30, "María") # Funcionaría, pero la semántica sería incorrecta
    # describir_persona("Carlos") # TypeError: missing 1 required positional argument: 'edad'
    ```
2. **Argumentos de Palabra Clave (Keyword Arguments):** Puedes pasar argumentos especificando el nombre del parámetro. Esto mejora la legibilidad y te permite cambiar el orden.
    ```python
    def describir_producto(nombre, precio, stock):
        print(f"Producto: {nombre}, Precio: ${precio}, Stock: {stock} unidades.")
    
    describir_producto(nombre="Laptop", stock=50, precio=899.99) # El orden no importa
    ```
3. **Parámetros con Valores por Defecto:** Puedes asignar un valor predeterminado a un parámetro en la definición de la función. Si no se proporciona un argumento para ese parámetro al llamar la función, se usará su valor por defecto. Los parámetros con valor por defecto deben ir después de los posicionales.
    ```python
    def saludar_con_idioma(nombre, idioma="Español"): # 'idioma' tiene un valor por defecto
        if idioma == "Español":
            print(f"Hola, {nombre}!")
        elif idioma == "Inglés":
            print(f"Hello, {nombre}!")
        else:
            print(f"Idioma no reconocido para {nombre}.")
    
    saludar_con_idioma("Elena")           # Usa el idioma por defecto: Español
    saludar_con_idioma("John", "Inglés")  # Sobrescribe el idioma por defecto
    ```
    _Salida:_
    ```
    Hola, Elena!
    Hello, John!
    ```
---
### La Sentencia `return`: Devolver un Valor
Las funciones no solo realizan acciones, sino que también pueden **devolver un valor** al lugar donde fueron llamadas. Esto se hace con la sentencia **`return`**. Cuando `return` se ejecuta, la función termina inmediatamente y el valor especificado es el "resultado" de la función.
```python
def sumar(a, b):
    resultado = a + b
    return resultado # La función devuelve el valor de 'resultado'

def es_par(numero):
    if numero % 2 == 0:
        return True # Devuelve True si es par
    else:
        return False # Devuelve False si es impar

# Capturando el valor devuelto
suma_total = sumar(10, 5)
print(f"La suma es: {suma_total}") # Salida: La suma es: 15

# Usando el valor devuelto en una condición
if es_par(4):
    print("4 es un número par.")
else:
    print("4 es un número impar.")
```
_Salida:_
```
La suma es: 15
4 es un número par.
```
Si una función no tiene una sentencia `return` explícita, o si solo tiene un `return` sin un valor, Python devuelve implícitamente `None`.
Las funciones son bloques de construcción esenciales en Python que te permiten escribir código más organizado, eficiente y fácil de mantener.