## Salida de datos (Output)
La forma más común de sacar datos en Python es usando la función **`print()`**. Esta función te permite mostrar texto, números, el contenido de variables y casi cualquier cosa en la consola o terminal donde se ejecuta tu programa.
### Cómo funciona `print()`
- **Mostrar texto simple:**
    ```python
    print("¡Hola, mundo!")
    ```
    _Salida:_
    ```python
    ¡Hola, mundo!
    ```
    
- **Mostrar el valor de una variable:**
    ```python
    nombre = "Ana"
    print(nombre)
    ```
    _Salida:_
    ```python
    Ana
    ```
- **Mostrar múltiples elementos:** Puedes pasarle varios elementos a `print()`, y los separará con un espacio por defecto.
    ```python
    edad = 30
    print("Mi nombre es", nombre, "y tengo", edad, "años.")
    ```
    _Salida:_
    ```python
    Mi nombre es Ana y tengo 30 años.
    ```
- **Controlar el separador (`sep`) y el final (`end`):**
    - El argumento `sep` (separador) te permite cambiar el carácter que se usa entre los elementos que imprimes (por defecto es un espacio).
    - El argumento `end` (final) te permite cambiar lo que se imprime al final de la línea (por defecto es un salto de línea `\n`).
    ```python
    print("Manzana", "Pera", "Uva", sep="-")
    print("Esto está en la misma línea", end=".")
    print("Continuación")
    ```
    _Salida:_
    ```python
    Manzana-Pera-Uva
    Esto está en la misma línea.Continuación
    ```
- **Cadenas f-string (f-strings):** A partir de Python 3.6, las f-strings son una forma muy popular y legible de formatear cadenas, permitiéndote insertar variables directamente dentro de una cadena de texto.
    ```python
    producto = "Laptop"
    precio = 1200.50
    print(f"El {producto} tiene un precio de ${precio:.2f}.") # :.2f formatea a 2 decimales
    ```
    _Salida:_
    ```python
    El Laptop tiene un precio de $1200.50.
    ```
---
## Entrada de Datos (Input)
Para que tu programa pueda "escuchar" y recibir información del usuario, usamos la función **`input()`**. Esta función pausa la ejecución del programa, espera a que el usuario escriba algo y presione Enter, y luego devuelve lo que el usuario escribió como una **cadena de texto (string)**.
### Cómo funciona `input()`
- **Capturar entrada básica:**
    ```python
    pregunta = input("¿Cuál es tu nombre? ")
    print("Hola,", pregunta)
    ```
    _Ejemplo de interacción:_
    ```python
    ¿Cuál es tu nombre? [El usuario escribe] Pedro
    Hola, Pedro
    ```
- **Recordar que `input()` siempre devuelve un string:** Este es un punto **muy importante**. Si esperas que el usuario ingrese un número para hacer cálculos, debes **convertir** explícitamente ese string a un tipo numérico (entero o flotante).
    ```python
    edad_str = input("Ingresa tu edad: ")
    # Intentar sumar directamente aquí daría un error si edad_str no es un número
    # edad_en_5_años = edad_str + 5 # Esto fallaría!
    
    # Convertir a entero (int)
    edad_num = int(edad_str)
    edad_en_5_años = edad_num + 5
    print(f"En 5 años tendrás {edad_en_5_años} años.")
    ```
    _Ejemplo de interacción:_
    ```python
    Ingresa tu edad: [El usuario escribe] 25
    En 5 años tendrás 30 años.
    ```
    Si el usuario ingresa algo que no se puede convertir a número (ej. "veinticinco"), el programa daría un error (`ValueError`).
- **Convertir a flotante (float):** Si esperas un número decimal:
    ```python
    altura_str = input("Ingresa tu altura en metros (ej. 1.75): ")
    altura_num = float(altura_str)
    print(f"Tu altura es {altura_num} metros.")
    ```

---

⬅️[Inicio](../../../README.md)