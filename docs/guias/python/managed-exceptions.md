En programación, un **error** es algo que impide que tu programa se ejecute correctamente y se detenga abruptamente. Una **excepción** es un tipo específico de error que ocurre durante la ejecución de un programa (a diferencia de un error de sintaxis, que ocurre antes de que el programa empiece a correr).
El manejo de excepciones te permite **anticipar** y **controlar** estos errores para que tu programa no se bloquee. En lugar de detenerse, puedes "atrapar" la excepción y decidir qué hacer con ella, permitiendo que tu programa continúe funcionando o termine de forma más controlada. Esto hace que tu código sea más robusto y amigable para el usuario.
El manejo de excepciones en Python se realiza principalmente con los bloques `try` y `except`.

---
### El Bloque `try`
El bloque `try` es donde colocas el código que **potencialmente podría causar una excepción**. Python intentará ejecutar este código.
### El Bloque `except`
El bloque `except` es donde colocas el código que se ejecutará **si ocurre una excepción** dentro del bloque `try`. Este bloque actúa como un "salvavidas" para tu programa.
#### Sintaxis Básica
```python
try:
    # Código que podría generar una excepción
except:
    # Código que se ejecuta si ocurre CUALQUIER excepción en el bloque try
```
#### ¿Cómo funciona?
1. Python comienza a ejecutar el código dentro del bloque `try`.
2. Si **no ocurre ninguna excepción**, el código dentro del bloque `except` se omite y el programa continúa con la línea siguiente al bloque `except`.
3. Si **ocurre una excepción** dentro del bloque `try`, Python detiene la ejecución del `try`, salta al bloque `except` y ejecuta el código que contiene. Después de que el `except` termina, el programa continúa normalmente desde la línea siguiente al bloque `except`.
---
### Tipos Específicos de Error (`ValueError`, `TypeError`)
Aunque puedes usar un `except` genérico, es una **muy buena práctica especificar qué tipo de excepción esperas atrapar**. Esto evita que tu programa "trague" errores inesperados que podrían indicar un problema más grave que no quieres ignorar.
Aquí te presento dos de los tipos de errores más comunes que querrías manejar:
- **`ValueError`**: Ocurre cuando una operación o función recibe un argumento del tipo correcto, pero con un **valor inapropiado**.
    - **Ejemplo:** Intentar convertir una cadena de texto que no es un número a un tipo numérico (como `int("abc")`).
- **`TypeError`**: Ocurre cuando una operación o función es aplicada a un objeto de un **tipo inapropiado**.
    - **Ejemplo:** Intentar sumar un número y una lista (`5 + [1, 2]`) o llamar a un método que no existe en un tipo de dato.
#### Sintaxis con Tipo Específico
```python
try:
    # Código que podría generar una excepción
except TipoDeError:
    # Código que se ejecuta si ocurre SOLO ese TipoDeError
except OtroTipoDeError:
    # Código que se ejecuta si ocurre SOLO este OtroTipoDeError
except:
    # Opcional: Bloque genérico para cualquier otra excepción no especificada
    # (Usar con precaución y solo si sabes por qué lo necesitas)
```
#### Ejemplos Prácticos
1. **Manejo de `ValueError` (Entrada de usuario no válida)**
    ```python
    try:
        edad_str = input("Por favor, ingresa tu edad: ")
        edad_num = int(edad_str) # Esto puede lanzar ValueError si no es un número
        print(f"Tu edad es: {edad_num}")
    except ValueError:
        print("¡Error! Debes ingresar un número entero válido para la edad.")
    
    print("Programa continúa...")
    ```
    - **Si el usuario ingresa "25":**
        ```
        Por favor, ingresa tu edad: 25
        Tu edad es: 25
        Programa continúa...
        ```
    - **Si el usuario ingresa "veinticinco":**
        ```
        Por favor, ingresa tu edad: veinticinco
        ¡Error! Debes ingresar un número entero válido para la edad.
        Programa continúa...
        ```
        
2. **Manejo de `TypeError` (Operaciones con tipos incompatibles)**
    ```python
    def sumar_numeros(a, b):
        try:
            resultado = a + b
            print(f"La suma es: {resultado}")
        except TypeError:
            print(f"¡Error! No se pueden sumar '{type(a).__name__}' y '{type(b).__name__}'. Ambos deben ser números.")
    
    sumar_numeros(10, 5)        # Salida: La suma es: 15
    sumar_numeros(10, "hola")   # Salida: ¡Error! No se pueden sumar 'int' y 'str'. Ambos deben ser números.
    sumar_numeros([1], [2])     # Salida: La suma es: [1, 2] (TypeError no ocurre para listas, se concatenan)
    ```
3. **Manejo de Múltiples Tipos de Excepciones**
    Puedes tener varios bloques `except` para manejar diferentes tipos de errores. Python intentará atrapar la excepción con el primer `except` que coincida.
    ```python
    def dividir_numeros():
        try:
            num1_str = input("Ingresa el primer número: ")
            num1 = int(num1_str)
    
            num2_str = input("Ingresa el segundo número: ")
            num2 = int(num2_str)
    
            resultado = num1 / num2 # Podría causar ZeroDivisionError si num2 es 0
            print(f"El resultado de la división es: {resultado}")
    
        except ValueError:
            print("¡Error de entrada! Asegúrate de ingresar solo números enteros.")
        except ZeroDivisionError:
            print("¡Error de operación! No se puede dividir por cero.")
        except Exception as e: # Captura cualquier otra excepción no especificada
            print(f"Ocurrió un error inesperado: {e}")
            # Es buena práctica imprimir el error original con 'as e' para depuración
        finally: # Bloque opcional, se ejecuta siempre (ver explicación abajo)
            print("Intento de división terminado.")
    
    dividir_numeros()
    # Pruebas:
    # - num1="diez", num2="2" -> ValueError
    # - num1="10", num2="0"  -> ZeroDivisionError
    # - num1="10", num2="2"  -> Éxito
    ```
---
### Conceptos Adicionales (Breve mención)
- **`else` en `try-except`**: Puedes agregar un bloque `else` que se ejecuta **solo si el bloque `try` se completa sin ninguna excepción**.
    ```python
    try:
        # código
    except:
        # maneja error
    else:
        # código que se ejecuta SOLO si NO hubo excepción en el try
    ```
    
- **`finally`**: Un bloque `finally` se ejecuta **siempre**, independientemente de si ocurrió una excepción o no. Es útil para limpiar recursos (cerrar archivos, conexiones a bases de datos).
```python
try:
    f = open("mi_archivo.txt", "r")
    # ... operaciones con el archivo ...
except FileNotFoundError:
    print("El archivo no fue encontrado.")
finally:
    if 'f' in locals() and not f.closed: # Asegurarse de que f existe y no está cerrado
        f.close()
        print("Archivo cerrado.")
```
El manejo de excepciones es esencial para crear aplicaciones robustas y amigables. Te permite controlar los imprevistos y proporcionar una mejor experiencia al usuario, en lugar de que tu programa se bloquee.

---

⬅️[Inicio](../../../README.md)