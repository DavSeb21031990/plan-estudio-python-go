---
title: 'Ámbiente de Variables'
description: 'Guia para Ámbito de Variables'
---

El **ámbito (scope)** de una variable se refiere a la región del programa donde esa variable es accesible y puede ser utilizada. En Python, el ámbito es fundamental para entender cómo tus variables se comportan y para evitar errores comunes. Principalmente, distinguimos entre variables **locales** y **globales**.

---
### 1. Variables Locales
Una variable es **local** cuando se define **dentro de una función**. Su ámbito está restringido a esa función; solo puede ser accedida o modificada desde dentro de la función donde fue creada. Fuera de esa función, la variable simplemente "no existe".
#### Características:
- **Creación:** Se crean al momento de llamar a la función.
- **Visibilidad:** Solo visibles y accesibles dentro de la función donde fueron definidas.
- **Tiempo de vida:** Se destruyen una vez que la función termina su ejecución.
- **Aislamiento:** Permiten que diferentes funciones usen el mismo nombre de variable sin que haya conflictos entre ellas.
#### Ejemplo:
```python
def mi_funcion():
    mensaje = "Soy una variable local" # 'mensaje' es local a mi_funcion
    print(mensaje)

# Intentamos acceder a 'mensaje' fuera de la función
mi_funcion()
# print(mensaje) # Esto generaría un NameError porque 'mensaje' no existe aquí
```
_Salida:_
```
Soy una variable local
```
Si des comentas la línea `print(mensaje)` fuera de la función, obtendrías un `NameError` porque `mensaje` solo vive dentro de `mi_funcion`.

---
### 2. Variables Globales
Una variable es **global** cuando se define **fuera de cualquier función**, directamente en el cuerpo principal del script. Su ámbito es todo el programa, lo que significa que puede ser accedida desde cualquier parte del código, incluyendo dentro de las funciones.
#### Características:
- **Creación:** Se crean cuando se ejecuta la parte principal del script.
- **Visibilidad:** Accesibles desde cualquier parte del código (dentro y fuera de las funciones).
- **Tiempo de vida:** Existen mientras el programa se esté ejecutando.
- **Uso:** Generalmente se usan para datos que necesitan ser compartidos o accesibles en muchas partes del programa.
#### Ejemplo:
```python
nombre_global = "Soy una variable global" # 'nombre_global' es global

def otra_funcion():
    print(nombre_global) # Accedemos a la variable global desde dentro de la función

print(nombre_global) # Accedemos a la variable global desde fuera de la función
otra_funcion()
```
_Salida:_
```
Soy una variable global
Soy una variable global
```
---
### El Dilema de Modificar Variables Globales desde Funciones: La palabra clave `global`
Aquí es donde la cosa se pone un poco más interesante y, a veces, confusa para los principiantes.
- **Leer una variable global:** Puedes leer el valor de una variable global desde dentro de una función sin problemas, como en el ejemplo anterior.
- **Modificar una variable global:** Si intentas **asignar un nuevo valor** a una variable global desde dentro de una función, Python por defecto no modifica la variable global. En su lugar, **crea una nueva variable local con el mismo nombre** dentro de la función. Esto se debe a la regla de que, a menos que se le indique lo contrario, las asignaciones dentro de una función crean variables locales.
Para **modificar explícitamente una variable global** desde dentro de una función, debes usar la palabra clave **`global`** antes del nombre de la variable.
#### Ejemplo de Modificación:
```python
contador = 0 # Variable global

def incrementar_contador_incorrecto():
    contador = 1 # ¡ERROR! Esto crea una NUEVA variable LOCAL llamada 'contador'
    print(f"Dentro de la función (local): {contador}")

def incrementar_contador_correcto():
    global contador # Declara que queremos usar la variable GLOBAL 'contador'
    contador += 1
    print(f"Dentro de la función (global): {contador}")

print(f"Antes de llamar (global): {contador}") # Salida: 0

incrementar_contador_incorrecto()
print(f"Después de incorrecto (global): {contador}") # Salida: 0 (La global no cambió)

incrementar_contador_correcto()
print(f"Después de correcto (global): {contador}") # Salida: 1 (La global sí cambió)
```
_Salida:_
```
Antes de llamar (global): 0
Dentro de la función (local): 1
Después de incorrecto (global): 0
Dentro de la función (global): 1
Después de correcto (global): 1
```
**Es generalmente una buena práctica limitar el uso de `global`**. Modificar variables globales directamente desde funciones puede hacer que el código sea más difícil de entender, depurar y mantener, ya que los cambios pueden tener efectos secundarios inesperados en otras partes del programa. Es preferible pasar los valores como **argumentos** y devolver los resultados.

---
### Resumen Rápido:
- **Variable Local:** Creada y visible **dentro de una función**.
- **Variable Global:** Creada y visible **fuera de cualquier función**, accesible desde cualquier lugar.
- Para **leer** una variable global dentro de una función, no necesitas nada especial.
- Para **modificar** una variable global dentro de una función, debes usar la palabra clave `global`.